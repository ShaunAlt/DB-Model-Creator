# =============================================================================
# Database Model Creator - Testing File Reading
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Testing File Reading
-
Contains all of the objects that are used for testing the ability of this
package to read and process database models being read from a file.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for automatic testing
import pytest

# used for creating the database models
from src.db_model_creator_py import (
    Database,
    LangDb,
    LangOrm,
    MethodType,
    ObjComp_Constant,
    ObjComp_Method,
    ObjComp_MethodParam,
    ObjComp_Property,
    ORM_Column,
    ORM_Table,
    ORM_View,
)


# =============================================================================
# Target Database Model
# =============================================================================
TARGET_MODEL = Database('placeholder.json')
''' Database model that the reading tests should re-create. '''
TARGET_MODEL._lang_db = LangDb.MSSQL
TARGET_MODEL._lang_orm = LangOrm.PYTHON_SQLALCHEMY
TARGET_MODEL._tables = [
    ORM_Table(
        name = 'DB_Status',
        tablename = 'Statuses',
        title = 'Statuses Table',
        desc = 'Contains all of the statuses (e.g. \'active\', \'archived\') in the application.',
        trigger_update = True,
        cols = [
            ORM_Column(
                name = 'status_id',
                type_ = 'tinyint',
                title = 'Primary Key ID',
                desc = 'Primary Key ID for the Status.',
                pk = True,
                identity = True
            ),
            ORM_Column(
                name = 'status_name',
                type_ = 'nvarchar(50)',
                title = 'Status Name',
                desc = 'The name of the status.',
                nullable = False,
                unique = True
            ),
        ],
        constants = [
            ObjComp_Constant(
                name = 'STATUS_ACTIVE',
                type_ = 'str',
                title = 'Active Status',
                desc = 'Name of the `active` status in the application.'
            ),
        ],
        methods = [
            ObjComp_Method(
                name = 'DB_Status',
                type_ = 'None',
                desc = 'Creates a new database `Statuses` row object.',
                title = 'Constructor',
                methodtype = MethodType.INSTANCE,
                params = [
                    ObjComp_MethodParam(
                        name = 'id',
                        type_ = 'int',
                        desc = 'ID of the new Status.'
                    ),
                    ObjComp_MethodParam(
                        name = 'name',
                        type_ = 'str',
                        desc = 'Name of the new Status.'
                    ),
                ],
                flag_constructor = True
            ),
            ObjComp_Method(
                name = 'GetStatus',
                type_ = 'DB_Status',
                desc = 'Get the status that matches the given status name.',
                title = 'Get Status from Name',
                methodtype = MethodType.CLASS,
                params = [
                    ObjComp_MethodParam(
                        name = 'name',
                        type_ = 'str',
                        desc = 'Name of the status to get.'
                    ),
                ]
            ),
        ],
        props = [
            ObjComp_Property(
                name = 'id',
                type_ = 'int',
                desc = 'ID of the current status.',
                title = 'Status ID',
                readonly = True
            ),
            ObjComp_Property(
                name = 'name',
                type_ = 'str',
                desc = 'Name of the current status.',
                title = 'Status Name',
                readonly = True
            ),
        ]
    ),
    ORM_Table(
        name = 'DB_User',
        tablename = 'Users',
        title = 'Users Table',
        desc = 'Contains all of the users within the application.',
        trigger_update = True,
        cols = [
            ORM_Column(
                name = 'user_id',
                type_ = 'bigint',
                title = 'Primary Key ID',
                desc = 'Primary Key ID for the User.',
                pk = True,
                identity = True
            ),
            ORM_Column(
                name = 'user_name_first',
                type_ = 'nvarchar(50)',
                title = 'User\'s First Name',
                desc = 'First name of the user.',
                nullable = False
            ),
            ORM_Column(
                name = 'user_name_last',
                type_ = 'nvarchar(50)',
                title = 'User\'s Last Name',
                desc = 'Last name of the user.',
                nullable = False
            ),
            ORM_Column(
                name = 'status_id',
                type_ = 'tinyint',
                title = 'User Status',
                desc = 'Status of the user.',
                fk = 'Statuses.status_id',
                nullable = False
            ),
        ],
        constants = [],
        methods = [
            ObjComp_Method(
                name = 'DB_User',
                type_ = 'None',
                desc = 'Creates a new database `Users` row object.',
                title = 'Constructor',
                methodtype = MethodType.INSTANCE,
                params = [
                    ObjComp_MethodParam(
                        name = 'id',
                        type_ = 'int',
                        desc = 'ID of the new User.'
                    ),
                    ObjComp_MethodParam(
                        name = 'name_first',
                        type_ = 'str',
                        desc = 'First name of the new User.'
                    ),
                    ObjComp_MethodParam(
                        name = 'name_last',
                        type_ = 'str',
                        desc = 'Last name of the new User.'
                    ),
                    ObjComp_MethodParam(
                        name ='status',
                        type_ = 'DB_Status',
                        desc = 'Status of the new User.'
                    ),
                ],
                flag_constructor = True
            ),
            ObjComp_Method(
                name = 'GetView',
                type_ = 'VW_Table_User',
                desc = 'Gets the table view row corresponding to the current user.',
                title = 'Get Table View',
                methodtype = MethodType.INSTANCE,
                params = [],
                default = 'None'
            ),
        ],
        props = [
            ObjComp_Property(
                name = 'id',
                type_ = 'int',
                desc = 'ID of the current user.',
                title = 'User ID',
                readonly = True
            ),
            ObjComp_Property(
                name = 'name_first',
                type_ = 'str',
                desc = 'First name of the current user.',
                title = 'User\'s First Name'
            ),
            ObjComp_Property(
                name = 'name_full',
                type_ = 'str',
                desc = 'Full name of the current user.',
                title = 'User\'s Full Name',
                readonly = True
            ),
            ObjComp_Property(
                name = 'name_last',
                type_ = 'str',
                desc = 'Last name of the current user.',
                title = 'User\'s Last Name'
            ),
            ObjComp_Property(
                name ='status',
                type_ = 'DB_Status',
                desc = 'Status of the current user.',
                title = 'User Status'
            ),
        ]
    ),
    ORM_Table(
        name = 'DB_Order',
        tablename = 'Orders',
        title = 'Orders Table',
        desc = 'Contains all of the orders within the application.',
        trigger_update = True,
        cols = [
            ORM_Column(
                name = 'order_id',
                type_ = 'bigint',
                title = 'Primary Key ID',
                desc = 'Primary Key ID for the Order.',
                pk = True,
                identity = True
            ),
            ORM_Column(
                name = 'order_code',
                type_ = 'nvarchar(100)',
                title = 'Order Code',
                desc = 'Unique code for the order.',
                unique = True,
                nullable = True
            ),
            ORM_Column(
                name = 'status_id',
                type_ = 'tinyint',
                title = 'Order Status',
                desc = 'Status of the order.',
                fk = 'Statuses.status_id',
                nullable = False
            )
        ],
        constants = [],
        methods = [
            ObjComp_Method(
                name = 'DB_Order',
                type_ = 'None',
                desc = 'Creates a new database `Orders` row object.',
                title = 'Constructor',
                methodtype = MethodType.INSTANCE,
                params = [
                    ObjComp_MethodParam(
                        name = 'id',
                        type_ = 'int',
                        desc = 'ID of the new Order.'
                    ),
                    ObjComp_MethodParam(
                        name = 'status',
                        type_ = 'DB_Status',
                        desc = 'Status of the new Order.'
                    ),
                    ObjComp_MethodParam(
                        name = 'code',
                        type_ = 'str | None',
                        desc = 'Code of the new Order.',
                        default = 'None'
                    ),
                ],
                flag_constructor = True
            ),
        ],
        props = [
            ObjComp_Property(
                name = 'id',
                type_ = 'int',
                desc = 'ID of the current Order.',
                title = 'Order ID',
                readonly = True
            ),
            ObjComp_Property(
                name ='status',
                type_ = 'DB_Status',
                desc = 'Status of the current Order.',
                title = 'Order Status'
            ),
            ObjComp_Property(
                name = 'code',
                type_ = 'str | None',
                desc = 'Code of the current Order.',
                title = 'Order Code'
            ),
        ]
    ),
    ORM_Table(
        name = 'DB_UserOrder',
        tablename = 'UsersOrders',
        title = 'Users and Orders Linking Table',
        desc = 'Contains a list of all orders associated with all of the required users.',
        trigger_update = False,
        cols = [
            ORM_Column(
                name = 'user_id',
                type_ = 'bigint',
                title = 'User ID',
                desc = 'User that placed the order.',
                fk = 'Users.user_id',
                pk = True
            ),
            ORM_Column(
                name = 'order_id',
                type_ = 'bigint',
                title = 'Order ID',
                desc = 'Order placed by the user.',
                fk = 'Orders.order_id',
                pk = True
            ),
        ],
        constants = [],
        methods = [
            ObjComp_Method(
                name = 'DB_UserOrder',
                type_ = 'None',
                desc = 'Creates a new database `UsersOrders` row object.',
                title = 'Constructor',
                methodtype = MethodType.INSTANCE,
                params = [
                    ObjComp_MethodParam(
                        name = 'user_id',
                        type_ = 'int',
                        desc = 'ID of the User.'
                    ),
                    ObjComp_MethodParam(
                        name = 'order_id',
                        type_ = 'int',
                        desc = 'ID of the Order.'
                    )
                ],
                flag_constructor = True
            )
        ],
        props = []
    )
]
TARGET_MODEL._views = [
    ORM_View(
        name = 'VW_Table_User',
        viewname = 'vwTable_Users',
        title = 'View - Users Table',
        desc = 'Contains information calculated for the users table.',
        cols = [
            ORM_Column(
                name = 'user_id',
                type_ = 'bigint',
                title = 'User ID',
                desc = 'User the data is calculated for.',
                nullable = False
            ),
            ORM_Column(
                name = 'num_orders',
                type_ = 'int',
                title = 'Number of Orders',
                desc = 'Number of orders placed by the user.',
                nullable = False
            ),
        ],
        constants = [],
        methods = [],
        props = []
    ),
    ORM_View(
        name = 'VW_Table_Order',
        viewname = 'vwTable_Orders',
        title = 'View - Orders Table',
        desc = 'Contains information calculated for the orders table.',
        cols = [
            ORM_Column(
                name = 'order_id',
                type_ = 'bigint',
                title = 'Order ID',
                desc = 'Order the data is calculated for.',
                nullable = False
            ),
            ORM_Column(
                name = 'num_users',
                type_ = 'int',
                title = 'Number of Users',
                desc = 'Number of users that placed the order.',
                nullable = False
            ),
        ],
        constants = [],
        methods = [],
        props = []
    )
]


# =============================================================================
# Main Read Test
# =============================================================================
@pytest.mark.parametrize("file_name", [
    "tests/model_files/test_file.json",
    # "tests/model_files/test_file.xml",
    "tests/model_files/test_file.yaml",
])
def test_read(file_name: str) -> None:
    '''
    Test Read
    -
    Reads a file, attempts to create a database model out of it, and then
    asserts that the database model created contains all of the correct data.

    This method is used to test that the package is able to successfully read a
    database model from a file and convert it into a group of database model
    objects.

    Parameters
    -
    - file_name : `str`
        - The directory + file name of the file to read.

    Returns
    -
    None
    '''

    # create base database object
    db = Database(file_name = file_name)

    # create database model from file
    db.Read()

    # validate against target model
    assert db._lang_db == TARGET_MODEL._lang_db
    assert db._lang_orm == TARGET_MODEL._lang_orm
    assert len(db._tables) == len(TARGET_MODEL._tables)
    assert len(db._views) == len(TARGET_MODEL._views)
    for table in db._tables:
        for target_table in TARGET_MODEL._tables:
            if table._tablename != target_table._tablename:
                continue
            assert table._tablename == target_table._tablename
            assert table._title == target_table._title
            assert table._desc == target_table._desc
            assert table._trigger_update == target_table._trigger_update
            assert len(table._cols) == len(target_table._cols)
            for col in table._cols:
                for target_col in target_table._cols:
                    if col._name != target_col._name:
                        continue
                    assert col._title == target_col._title
                    assert col._desc == target_col._desc
                    assert col._fk == target_col._fk
                    assert col._identity == target_col._identity
                    assert col._nullable == target_col._nullable
                    assert col._pk == target_col._pk
                    assert col._type == target_col._type
                    assert col._unique == target_col._unique
                    break
                else:
                    raise AssertionError(
                        f'Column {col} in table {table} had no matches in ' \
                        + f'{target_table._cols} in table {target_table}'
                    )
            assert len(table._constants) == len(target_table._constants)
            for const in table._constants:
                for target_const in target_table._constants:
                    if const._name != target_const._name:
                        continue
                    assert const._type == target_const._type
                    assert const._title == target_const._title
                    assert const._desc == target_const._desc
                    assert const._default == target_const._default
                    break
                else:
                    raise AssertionError(
                        f'Constant {const} in table {table} had no matches ' \
                        + f'in {target_table._constants} in table ' \
                        + f'{target_table}'
                    )
            assert len(table._methods) == len(target_table._methods)
            for method in table._methods:
                for target_method in target_table._methods:
                    if method._name != target_method._name:
                        continue
                    assert method._type == target_method._type
                    assert method._title == target_method._title
                    assert method._desc == target_method._desc
                    assert method._default == target_method._default
                    assert method._flag_constructor \
                        == target_method._flag_constructor
                    assert method._method_type == target_method._method_type
                    assert len(method._params) == len(target_method._params)
                    for param in method._params:
                        for target_param in target_method._params:
                            if param._name != target_param._name:
                                continue
                            assert param._type == target_param._type
                            assert param._title == target_param._title
                            assert param._desc == target_param._desc
                            assert param._default == target_param._default
                            break
                        else:
                            raise AssertionError(
                                f'Parameter {param} in method {method} in ' \
                                + f'table {table} had no matches in ' \
                                + f'{target_method._params} in method ' \
                                + f'{target_method} in table {target_table}'
                            )
                    break
                else:
                    raise AssertionError(
                        f'Method {method} in table {table} had no matches in' \
                        + f' {target_table._methods} in table {target_table}'
                    )
            assert len(table._props) == len(target_table._props)
            for prop in table._props:
                for target_prop in target_table._props:
                    if prop._name != target_prop._name:
                        continue
                    assert prop._type == target_prop._type
                    assert prop._title == target_prop._title
                    assert prop._desc == target_prop._desc
                    assert prop._default == target_prop._default
                    assert prop._readonly == target_prop._readonly
                    break
                else:
                    raise AssertionError(
                        f'Property {prop} in table {table} had no matches in' \
                        + f' {target_table._props} in table {target_table}'
                    )
            break
        else:
            raise AssertionError(
                f'Table {table} had no matches in {TARGET_MODEL._tables}'
            )
    for view in db._views:
        for target_view in TARGET_MODEL._views:
            if view._viewname != target_view._viewname:
                continue
            assert view._viewname == target_view._viewname
            assert view._title == target_view._title
            assert view._desc == target_view._desc
            assert len(view._cols) == len(target_view._cols)
            for col in view._cols:
                for target_col in target_view._cols:
                    if col._name != target_col._name:
                        continue
                    assert col._title == target_col._title
                    assert col._desc == target_col._desc
                    assert col._fk == target_col._fk
                    assert col._identity == target_col._identity
                    assert col._nullable == target_col._nullable
                    assert col._pk == target_col._pk
                    assert col._type == target_col._type
                    assert col._unique == target_col._unique
                    break
                else:
                    raise AssertionError(
                        f'Column {col} in view {view} had no matches in ' \
                        + f'{target_view._cols} in view {target_view}'
                    )
            assert len(view._constants) == len(target_view._constants)
            for const in view._constants:
                for target_const in target_view._constants:
                    if const._name != target_const._name:
                        continue
                    assert const._type == target_const._type
                    assert const._title == target_const._title
                    assert const._desc == target_const._desc
                    assert const._default == target_const._default
                    break
                else:
                    raise AssertionError(
                        f'Constant {const} in view {view} had no matches ' \
                        + f'in {target_view._constants} in view ' \
                        + f'{target_view}'
                    )
            assert len(view._methods) == len(target_view._methods)
            for method in view._methods:
                for target_method in target_view._methods:
                    if method._name != target_method._name:
                        continue
                    assert method._type == target_method._type
                    assert method._title == target_method._title
                    assert method._desc == target_method._desc
                    assert method._default == target_method._default
                    assert method._flag_constructor \
                        == target_method._flag_constructor
                    assert method._method_type == target_method._method_type
                    assert len(method._params) == len(target_method._params)
                    for param in method._params:
                        for target_param in target_method._params:
                            if param._name != target_param._name:
                                continue
                            assert param._type == target_param._type
                            assert param._title == target_param._title
                            assert param._desc == target_param._desc
                            assert param._default == target_param._default
                            break
                        else:
                            raise AssertionError(
                                f'Parameter {param} in method {method} in ' \
                                + f'view {view} had no matches in ' \
                                + f'{target_method._params} in method ' \
                                + f'{target_method} in view {target_view}'
                            )
                    break
                else:
                    raise AssertionError(
                        f'Method {method} in view {view} had no matches in' \
                        + f' {target_view._methods} in view {target_view}'
                    )
            assert len(view._props) == len(target_view._props)
            for prop in view._props:
                for target_prop in target_view._props:
                    if prop._name != target_prop._name:
                        continue
                    assert prop._type == target_prop._type
                    assert prop._title == target_prop._title
                    assert prop._desc == target_prop._desc
                    assert prop._default == target_prop._default
                    assert prop._readonly == target_prop._readonly
                    break
                else:
                    raise AssertionError(
                        f'Property {prop} in view {view} had no matches in' \
                        + f' {target_view._props} in view {target_view}'
                    )
            break
        else:
            raise AssertionError(
                f'View {view} had no matches in {TARGET_MODEL._views}'
            )


# =============================================================================
# End of File
# =============================================================================
