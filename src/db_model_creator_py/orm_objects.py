# =============================================================================
# Database Model Creator - ORM Objects
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - ORM Objects
-
Contains the objects that contain all of the table, view, and other data for
the database.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# custom errors
from .errors import (
    AbstractError, # abstract method error
    UndefFuncError, # undefined functionality error
)

# generic objects
from .generic_objects import (
    OBJ, # base object model
    VerbosityLevel, # verbosity levels
)

# supported languagges
from .supported_languages import (
    LangDb, # supported database languages
    LangOrm, # supported ORM languages
)

# used for type hinting
from typing import (
    List, # list data type
    Optional, # nullable data type
)


# =============================================================================
# ORM Abstract Model
# =============================================================================
class ORM(OBJ):
    '''
    Abstract ORM Model
    -
    Contains the generic functionality shared by all of the orm objects.

    Fields
    -
    - _desc : `CompValue_Desc`
    - _name : `CompValue_Name`
    - _title : `CompValue_Title`
    - lang_db : `LangDb | None` << static >>
    - lang_orm : `LangOrm | None` << static >>
    - name : `str` << readonly >>
    - tables : `List<ORM_Table>` << static >>
    - views : `List<ORM_View>` << static >>

    Methods
    -
    - __eq__(other) << equality check >>
    - Duplicate() : `ORM` << override >>
    - FromDict(data) : `ORM` << class, abstract >>
    - GetData(lvl : VerbosityLevel) : `List<str>` << override >>
    - LoadData(...) << static >>
    - ORM(name : str, title : str, desc : str) << constructor >>
    - Validate() : `bool` << abstract >>
    - WriteDb(comment : bool) : `str` << abstract >>
    - WriteOrm(comment : bool) : `str` << abstract >>
    '''

    # =============
    # Static Fields
    lang_db: Optional[LangDb] = None
    ''' Database language to write the object in. '''
    lang_orm: Optional[LangOrm] = None
    ''' ORM language to write the object in. '''
    tables: List['ORM_Table'] = []
    ''' Collection of all tables in the database. '''
    views: List['ORM_View'] = []
    ''' Collection of all views in the database. '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            (isinstance(other, self.__class__))
            and (self._desc == other._desc)
            and (self._title == other._title)
            and (self.name == other.name)
        )

    # ====================
    # Method - Constructor
    def __init__(self, name: str, title: str, desc: str) -> None:
        '''
        ORM Object Constructor
        -
        Creates a new `ORM` object.

        Parameters
        -
        - name : `str`
            - Name of the ORM object.
        - title : `str`
            - Comment title of the ORM object.
        - desc : `str`
            - Description of the ORM object.

        Returns
        -
        None
        '''

        # set fields
        self._desc = CompValue_Desc(desc)
        ''' Description of the ORM object. '''
        self._name = CompValue_Name(name)
        ''' Name of the ORM object. '''
        self._title = CompValue_Title(title)
        ''' Comment title of the ORM object. '''

    # ===============
    # Property - Name
    @property
    def name(self) -> str:
        ''' Name of the ORM object. '''
        return self._name.data
    
    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ORM':
        return ORM(
            name = self.name,
            title = self._title.data,
            desc = self._desc.data
        )
    
    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ORM':
        '''
        Create from Dictionary
        -
        Creates a new `ORM` object from a given dictionary.

        Parametes
        -
        - data : `dict`
            - Dictionary containing the data required to create the new `ORM`
                object.

        Returns
        -
        - `ORM`
            - New `ORM` object from the dictionary data.
        '''

        raise AbstractError(
            f'ORM.FromDict(data = {data}) not defined in {cls}'
        )

    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        if lvl == VerbosityLevel.SHORT:
            return ['name']
        elif lvl == VerbosityLevel.LONG:
            return [
                '_desc',
                '_name',
                '_title',
                'lang_db',
                'lang_orm',
                'tables',
                'views',
            ]
        else:
            return [
                '_desc',
                '_name',
                '_title',
                'lang_db',
                'lang_orm',
                'name',
                'tables',
                'views',
            ]
        
    # ================
    # Load Static Data
    @staticmethod
    def LoadData(
            lang_db: LangDb,
            lang_orm: LangOrm,
            tables: List['ORM_Table'],
            views: List['ORM_View']
    ) -> None:
        '''
        Load Static Data
        -
        Loads the static data for all ORM objects.

        Parameters
        -
        - lang_db : `LangDb`
            - Database language to write the objects in.
        - lang_orm : `LangOrm`
            - ORM language to write the objects in.
        - tables : `List<ORM_Table>`
            - Collection of all tables in the database.
        - views : `List<ORM_View>`
            - Collection of all views in the database.

        Returns
        -
        None
        '''

        # set static data
        ORM.lang_db = lang_db
        ORM.lang_orm = lang_orm
        ORM.tables = tables
        ORM.views = views

    # =================
    # Method - Validate
    def Validate(self) -> bool:
        '''
        Validate
        -
        Validates the current ORM object.

        Parameters
        -
        None

        Returns
        -
        - `bool`
            - Whether or not the object data is valid.
        '''

        raise AbstractError(
            f'ORM().Validate() not defined in {self.__class__}'
        )
    
    # ============================
    # Method - Write Database Code
    def WriteDb(self, comment: bool) -> str:
        '''
        Write Database Code
        -
        Creates a string of the code required to create the current ORM object
        in the database using the required language.

        Parameters
        -
        - comment : `bool`
            - Whether to create the comment for the object or the actual code.

        Returns
        -
        - `str`
            - String of the ORM object code in the database language.
        '''

        raise AbstractError(
            f'ORM().WriteDb(comment = {comment}) not defined in ' \
            + f'{self.__class__}'
        )
    
    # =======================
    # Method - Write ORM Code
    def WriteOrm(self, comment: bool) -> str:
        '''
        Write ORM Code
        -
        Creates a string of the code required to create the current ORM object
        in the ORM using the required language.

        Parameters
        -
        - comment : `bool`
            - Whether to create the comment for the object or the actual code.

        Returns
        -
        - `str`
            - String of the ORM object code in the ORM language.
        '''

        raise AbstractError(
            f'ORM().WriteOrm(comment = {comment}) not defined in ' \
            + f'{self.__class__}'
        )


# =============================================================================
# ORM Column
# =============================================================================
class ORM_Column(ORM):
    '''
    ORM Column
    -
    Contains the information relating to an individual column in the database
    and ORM.

    Fields
    -
    - _fk : `CompValue_Fk | None`
    - _identity : `bool`
    - _nullable : `bool`
    - _pk : `bool`
    - _type : `str`
    - _unique : `bool`

    Methods
    -
    - __eq__(other) << equality check >>
    - Duplicate() : `ORM_Column` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_Column(...) << constructor >>
    - WriteDb(comment : `bool`) : `str`
    - WriteOrm(comment : `bool`) : `str`
    '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            super().__eq__(other)
            and (isinstance(other, self.__class__))
            and (self._fk == other._fk)
            and (self._identity == other._identity)
            and (self._nullable == other._nullable)
            and (self._pk == other._pk)
            and (self._type == other._type)
            and (self._unique == other._unique)
        )

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            title: str,
            desc: str,
            nullable: bool = True,
            pk: bool = False,
            identity: bool = False,
            fk: Optional[str] = None,
            unique: bool = False
    ) -> None:
        '''
        ORM Column Constructor
        -
        Creates a new `ORM_Column` object.

        Parameters
        -
        - name : `str`
            - Column name.
        - type_ : `str`
            - Database datatype of the column.
        - title : `str`
            - Comment title of the column.
        - desc : `str`
            - Description of the column.
        - nullable : `bool`
            - Whether or not `NULL` values are allowed in the column. Defaults
                to `True`, meaning the column is `NULL`.
        - pk : `bool`
            - Whether or not the column is a primary key.
        - identity : `bool`
            - Whether or not the column is an auto-incrementing identity
                column.
        - fk : `str | None`
            - Defaults to `None`, meaning the column does not have a foreign
                key constraint. If not `None`, should contain the table and
                column name of the primary key that this column references.
        - unique : `bool`
            - Whether or not the column has a unique key constraint. Defaults
                to `False`, meaning the column is not unique.

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            title = title,
            desc = desc
        )

        # set fields
        self._fk = CompValue_Fk(fk) if fk else None
        ''' Defaults to `None`, meaning the column does not have a foreign
            key constraint. If not `None`, should contain the table and
            column name of the primary key that this column references. '''
        self._identity = identity
        ''' Whether or not the column is an auto-incrementing identity
            column. '''
        self._nullable = nullable
        ''' Whether or not `NULL` values are allowed in the column. Defaults
            to `False`, meaning the column is `NOT NULL`. '''
        self._pk = pk
        ''' Whether or not the column is a primary key. '''
        self._type = type_
        ''' Database datatype of the column. '''
        self._unique = unique
        ''' Whether or not the column has a unique key constraint. Defaults
            to `False`, meaning the column is not unique. '''

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ORM_Column':
        return ORM_Column(
            name = self.name,
            type_ = self._type,
            title = self._title.data,
            desc = self._desc.data,
            nullable = self._nullable,
            pk = self._pk,
            identity = self._identity,
            fk = self._fk.data if self._fk else None,
            unique = self._unique
        )
    
    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ORM_Column':
        # get the name of the column
        _name: object = data.get('name', None)
        if _name is None: # validate name existence
            raise ValueError('Failed to read Column Name (`name`)')
        if not isinstance(_name, str): # validate name type
            raise TypeError(
                'Column Name (`name`) expected a `str` type, got ' \
                + f'{type(_name)}'
            )
        if _name == '': # validate name data
            raise ValueError('Column Name (`name`) must not be empty')
        
        # get the type of the column
        _type: object = data.get('type_', None)
        if _type is None: # validate type existence
            raise ValueError('Failed to read Column Type (`type_`)')
        if not isinstance(_type, str): # validate type type
            raise TypeError(
                'Column Type (`type_`) expected a `str` type, got ' \
                + f'{type(_type)}'
            )
        if _type == '': # validate type data
            raise ValueError('Column Type (`type_`) must not be empty')
        
        # get the comment title of the column
        _title: object = data.get('title', None)
        if _title is None: # validate title existence
            raise ValueError('Failed to read Column Title (`title`)')
        if not isinstance(_title, str): # validate title type
            raise TypeError(
                'Column Title (`title`) expected a `str` type, got ' \
                + f'{type(_title)}'
            )
        if _title == '': # validate title data
            raise ValueError('Column Title (`title`) must not be empty')
        
        # get the description of the column
        _desc: object = data.get('desc', None)
        if _desc is None: # validate description existence
            raise ValueError('Failed to read Column Description (`desc`)')
        if not isinstance(_desc, str): # validate description type
            raise TypeError(
                'Column Description (`desc`) expected a `str` type, got ' \
                + f'{type(_desc)}'
            )
        if _desc == '': # validate description data
            raise ValueError('Column Description (`desc`) must not be empty')
        
        # get the nullable status of the column
        _nullable: object = data.get('nullable', 'True')
        if _nullable not in ['True', 'False']: # validate nullable value
            raise ValueError(
                'Column Nullable Status (`nullable`) expected a `str` value ' \
                + f'of either "True" or "False", got {_nullable!r}'
            )
        _nullable = True if _nullable == 'True' else False

        # get the primary key status of the column
        _pk: object = data.get('pk', 'False')
        if _pk not in ['True', 'False']: # validate pk value
            raise ValueError(
                'Column Primary Key Status (`pk`) expected a `str` value ' \
                + f'of either "True" or "False", got {_pk!r}'
            )
        _pk = True if _pk == 'True' else False

        # get the identity / auto-increment status of the column
        _identity: object = data.get('identity', 'False')
        if _identity not in ['True', 'False']: # validate identity value
            raise ValueError(
                'Column Identity / Auto-Increment Status (`identity`) ' \
                + 'expected a `str` value of either "True" or "False", got ' \
                + f'{_identity!r}'
            )
        _identity = True if _identity == 'True' else False

        # get the unique status of the column
        _unique: object = data.get('unique', 'False')
        if _unique not in ['True', 'False']: # validate unique value
            raise ValueError(
                'Column Unique Key Status (`unique`) expected a `str` value ' \
                + f'of either "True" or "False", got {_unique!r}'
            )
        _unique = True if _unique == 'True' else False

        # get the foreign key status of the column
        _fk: object = data.get('title', '')
        if not isinstance(_fk, str): # validate title type
            raise TypeError(
                'Column Foreign Key Status (`fk`) expected a `str | None` ' \
                + f'type, got {type(_fk)}'
            )
        
        # create the ORM_Column object
        return cls(
            name = _name,
            type_ = _type,
            title = _title,
            desc = _desc,
            nullable = _nullable,
            pk = _pk,
            identity = _identity,
            fk = _fk,
            unique = _unique,
        )

    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        data = super().GetData(lvl)
        if lvl == VerbosityLevel.SHORT:
            data.extend(['_type'])
        elif lvl == VerbosityLevel.LONG:
            data.extend([
                '_fk',
                '_identity',
                '_nullable',
                '_pk',
                '_type',
                '_unique',
            ])
        else:
            data.extend([
                '_fk',
                '_identity',
                '_nullable',
                '_pk',
                '_type',
                '_unique',
            ])
        return data
    
    # =================
    # Method - Validate
    def Validate(self) -> bool:
        raise UndefFuncError('ORM_Column().Validate() not defined')

    # ============================
    # Method - Write Database Code
    def WriteDb(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ORM_Column().WriteDb(comment = {comment}) not defined'
        )

    # =======================
    # Method - Write ORM Code
    def WriteOrm(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ORM_Column().WriteOrm(comment = {comment}) not defined'
        )


# =============================================================================
# ORM Table / View Abstract Parent
# =============================================================================
class ORM_TV(ORM):
    '''
    ORM Table / View Abstract Parent
    -
    Contains the information relating to an individual table or view in the
    database and ORM.

    Fields
    -
    - _cols : `List<ORM_Column>`
    - _constants : `List<ObjComp_Constant>`
    - _methods : `List<ObjComp_Method>`
    - _props : `List<ObjComp_Property>`

    Methods
    -
    - __eq__(other) << equality check >>
    - Duplicate() : `ORM_TV` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_TV(...) << constructor >>
    - WriteDb(comment : `bool`) : `str` << virtual >>
    - WriteOrm(comment : `bool`) : `str` << virtual >>
    '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            super().__eq__(other)
            and (isinstance(other, self.__class__))
            and (self._cols == other._cols)
            and (self._constants == other._constants)
            and (self._methods == other._methods)
            and (self._props == other._props)
        )

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            title: str,
            desc: str,
            cols: List['ORM_Column'],
            constants: List['ObjComp_Constant'],
            methods: List['ObjComp_Method'],
            props: List['ObjComp_Property']
    ) -> None:
        '''
        ORM Table / View Constructor
        -
        Creates a new `ORM_TV` object.

        Parameters
        -
        - name : `str`
            - Name of the table / view.
        - title : `str`
            - Comment title of the table / view.
        - desc : `str`
            - Description of the table / view.
        - cols : `List<ORM_Column>`
            - Collection of columns in the table / view.
        - constants : `List<ObjComp_Constant>`
            - Collection of constants in the table / view ORM object.
        - methods : `List<ObjComp_Method>`
            - Collection of methods in the table / view ORM object.
        - props : `List<ObjComp_Property>`
            - Collection of properties in the table / view ORM object.

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            title = title,
            desc = desc
        )

        # set fields
        self._cols = cols
        ''' Collection of columns in the table / view. '''
        self._constants = constants
        ''' Collection of constants in the table / view ORM object. '''
        self._methods = methods
        ''' Collection of methods in the table / view ORM object. '''
        self._props = props
        ''' Collection of properties in the table / view ORM object. '''

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ORM_TV':
        return ORM_TV(
            name = self.name,
            title = self._title.data,
            desc = self._desc.data,
            cols = [col.Duplicate() for col in self._cols],
            constants = [constant.Duplicate() for constant in self._constants],
            methods = [method.Duplicate() for method in self._methods],
            props = [prop.Duplicate() for prop in self._props]
        )
    
    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        data = super().GetData(lvl)
        if lvl == VerbosityLevel.SHORT:
            pass
        elif lvl == VerbosityLevel.LONG:
            data.extend([
                '_cols',
                '_constants',
                '_methods',
                '_props',
            ])
        else:
            data.extend([
                '_cols',
                '_constants',
                '_methods',
                '_props',
            ])
        return data
    
    # =================
    # Method - Validate
    def Validate(self) -> bool:
        raise AbstractError(
            f'ORM_TV().Validate() not defined in {self.__class__}'
        )

    # ============================
    # Method - Write Database Code
    def WriteDb(self, comment: bool) -> str:
        raise AbstractError(
            f'ORM_TV().WriteDb(comment = {comment}) not defined in ' \
            + f'{self.__class__}'
        )

    # =======================
    # Method - Write ORM Code
    def WriteOrm(self, comment: bool) -> str:
        raise AbstractError(
            f'ORM_TV().WriteOrm(comment = {comment}) not defined in ' \
            + f'{self.__class__}'
        )


# =============================================================================
# ORM Table
# =============================================================================
class ORM_Table(ORM_TV):
    '''
    ORM Table
    -
    Contains the information relating to an individual table in the database
    and ORM.

    Fields
    -
    - _tablename : `CompValue_Name`
    - _trigger_update : `bool`

    Methods
    -
    - __eq__(other) << equality check >>
    - Duplicate() : `ORM_Table` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_Table(...) << constructor >>
    - WriteDb(comment : `bool`) : `str` << override >>
    - WriteOrm(comment : `bool`) : `str` << override >>
    '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            super().__eq__(other)
            and (isinstance(other, self.__class__))
            and (self._tablename == other._tablename)
            and (self._trigger_update == other._trigger_update)
        )

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            tablename: str,
            title: str,
            desc: str,
            trigger_update: bool,
            cols: List['ORM_Column'],
            constants: List['ObjComp_Constant'],
            methods: List['ObjComp_Method'],
            props: List['ObjComp_Property']
    ) -> None:
        '''
        ORM Table Constructor
        -
        Creates a new `ORM_Table` object.

        Parameters
        -
        - name : `str`
            - Name of the table ORM object.
        - tablename : `str`
            - Name of the table as seen in the database.
        - title : `str`
            - Comment title of the table.
        - desc : `str`
            - Description of the table.
        - trigger_update : `bool`
            - Whether or not an update trigger and table should be created to
                track the data changes in this table.
        - cols : `List<ORM_Column>`
            - Collection of columns in the table.
        - constants : `List<ObjComp_Constant>`
            - Collection of constants in the table ORM object.
        - methods : `List<ObjComp_Method>`
            - Collection of methods in the table ORM object.
        - props : `List<ObjComp_Property>`
            - Collection of properties in the table ORM object.

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            title = title,
            desc = desc,
            cols = cols,
            constants = constants,
            methods = methods,
            props = props
        )

        # set fields
        self._tablename = CompValue_Name(tablename)
        ''' Name of the table as seen in the database. '''
        self._trigger_update = trigger_update
        ''' Whether or not an update trigger and table should be created to
            track the data changes in this table. '''

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ORM_Table':
        return ORM_Table(
            name = self.name,
            tablename = self._tablename.data,
            title = self._title.data,
            desc = self._desc.data,
            trigger_update = self._trigger_update,
            cols = [col.Duplicate() for col in self._cols],
            constants = [constant.Duplicate() for constant in self._constants],
            methods = [method.Duplicate() for method in self._methods],
            props = [prop.Duplicate() for prop in self._props]
        )
    
    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ORM_Column':
        # get the name of the table orm object
        _name: object = data.get('name', None)
        if _name is None: # validate name existence
            raise ValueError('Failed to read Table ORM Name (`name`)')
        if not isinstance(_name, str): # validate name type
            raise TypeError(
                'Table ORM Name (`name`) expected a `str` type, got ' \
                + f'{type(_name)}'
            )
        if _name == '': # validate name data
            raise ValueError('Table ORM Name (`name`) must not be empty')

        # get the name of the table (database name)
        _tablename: object = data.get('tablename', None)
        if _tablename is None: # validate tablename existence
            raise ValueError(
                'Failed to read Table Database Name (`tablename`)'
            )
        if not isinstance(_tablename, str): # validate tablename type
            raise TypeError(
                'Table Database Name (`tablename`) expected a `str` type, ' \
                + f'got {type(_tablename)}'
            )
        if _tablename == '': # validate tablename data
            raise ValueError(
                'Table Database Name (`tablename`) must not be empty'
            )
        
        # get the title of the table orm object
        _title: object = data.get('title', None)
        if _title is None: # validate title existence
            raise ValueError('Failed to read Table Title (`title`)')
        if not isinstance(_title, str): # validate title type
            raise TypeError(
                'Table Title (`title`) expected a `str` type, got ' \
                + f'{type(_title)}'
            )
        if _title == '': # validate title data
            raise ValueError('Table Title (`title`) must not be empty')
        
        # get the description of the table orm object
        _desc: object = data.get('desc', None)
        if _desc is None: # validate description existence
            raise ValueError('Failed to read Table Description (`desc`)')
        if not isinstance(_desc, str): # validate description type
            raise TypeError(
                'Table Description (`desc`) expected a `str` type, got ' \
                + f'{type(_desc)}'
            )
        if _desc == '': # validate description data
            raise ValueError('Table Description (`desc`) must not be empty')

        # get the trigger-update flag for the table
        _tu: object = data.get('trigger_update', None)
        if _tu is None: # validate trigger-update flag existence
            raise ValueError(
                'Failed to read Table Trigger-Update Flag (`trigger_update`)'
            )
        if _tu not in ['True', 'False']: # validate trigger-update value
            raise ValueError(
                'Table Trigger-Update Flag (`trigger_update`) expected a ' \
                + f'`str` value of either "True" or "False", got {_tu!r}'
            )
        _tu = True if _tu == 'True' else False

        # get the columns data for the table
        _cols: object = data.get('cols', None)
        if _cols is None: # validate columns existence
            raise ValueError('Failed to read Table Columns (`cols`)')
        if not isinstance(_cols, list): # validate columns type
            raise TypeError(
                'Table Columns (`cols`) expected a `list` type, got ' \
                + f'{type(_cols)}'
            )
        if len(_cols) < 1: # validate columns data
            raise ValueError(
                'Table Columns (`cols`) must contain at least one column'
            )
        cols: list[ORM_Column] = []
        for i, col in _cols:
            # validate column data is a dict
            if not isinstance(col, dict):
                raise TypeError(
                    f'Column at index `{i}` expected a `dict` type, got ' \
                    + f'{type(col)}'
                )
            
            # create column
            try:
                cols.append(ORM_Column.FromDict(col))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create column at index `{i}`: {e!r}'
                )

        # get the constants data for the table
        _consts: object = data.get('constants', None)
        if _consts is None: # validate constants existence
            raise ValueError('Failed to read Table Constants (`constants`)')
        if not isinstance(_consts, list): # validate constants type
            raise TypeError(
                'Table Constants (`constants`) expected a `list` type, got ' \
                + f'{type(_consts)}'
            )
        consts: list[ObjComp_Constant] = []
        for i, const in _consts:
            # validate constant data is a dict
            if not isinstance(const, dict):
                raise TypeError(
                    f'Constant at index `{i}` expected a `dict` type, got ' \
                    + f'{type(const)}'
                )
            
            # create constant
            try:
                consts.append(ObjComp_Constant.FromDict(const))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create constant at index `{i}`: {e!r}'
                )

        # get the methods data for the table
        _methods: object = data.get('methods', None)
        if _methods is None: # validate methods existence
            raise ValueError('Failed to read Table Methods (`methods`)')
        if not isinstance(_methods, list): # validate methods type
            raise TypeError(
                'Table Methods (`methods`) expected a `list` type, got ' \
                + f'{type(_methods)}'
            )
        methods: list[ObjComp_Method] = []
        for i, method in _methods:
            # validate method data is a dict
            if not isinstance(method, dict):
                raise TypeError(
                    f'Method at index `{i}` expected a `dict` type, got ' \
                    + f'{type(method)}'
                )
            
            # create method
            try:
                methods.append(ObjComp_Method.FromDict(method))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create method at index `{i}`: {e!r}'
                )

        # get the properties data for the table
        _props: object = data.get('props', None)
        if _props is None: # validate properties existence
            raise ValueError('Failed to read Table Properties (`props`)')
        if not isinstance(_props, list): # validate properties type
            raise TypeError(
                'Table Properties (`props`) expected a `list` type, got ' \
                + f'{type(_props)}'
            )
        props: list[ObjComp_Property] = []
        for i, prop in _props:
            # validate property data is a dict
            if not isinstance(prop, dict):
                raise TypeError(
                    f'Property at index `{i}` expected a `dict` type, got ' \
                    + f'{type(prop)}'
                )
            
            # create property
            try:
                props.append(ObjComp_Property.FromDict(prop))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create property at index `{i}`: {e!r}'
                )
            
        # create ORM_Table object
        return cls(
            name = _name,
            tablename = _tablename,
            title = _title,
            desc = _desc,
            trigger_update = _tu,
            cols = cols,
            constants = consts,
            methods = methods,
            props = props
        )

    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        data = super().GetData(lvl)
        if lvl == VerbosityLevel.SHORT:
            pass
        elif lvl == VerbosityLevel.LONG:
            data.extend([
                '_tablename',
                '_trigger_update',
            ])
        else:
            data.extend([
                '_tablename',
                '_trigger_update',
            ])
        return data
    
    # =================
    # Method - Validate
    def Validate(self) -> bool:
        raise UndefFuncError(
            'ORM_Table().Validate() not defined'
        )

    # ============================
    # Method - Write Database Code
    def WriteDb(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ORM_Table().WriteDb(comment = {comment}) not defined'
        )

    # =======================
    # Method - Write ORM Code
    def WriteOrm(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ORM_Table().WriteOrm(comment = {comment}) not defined'
        )


# =============================================================================
# ORM View
# =============================================================================
class ORM_View(ORM_TV):
    '''
    ORM View
    -
    Contains the information relating to an individual view in the database
    and ORM.

    Fields
    -
    - _viewname : `CompValue_Name`

    Methods
    -
    - __eq__(other) << equality check >>
    - Duplicate() : `ORM_View` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_View(...) << constructor >>
    - WriteDb(comment : `bool`) : `str` << override >>
    - WriteOrm(comment : `bool`) : `str` << override >>
    '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            super().__eq__(other)
            and (isinstance(other, self.__class__))
            and (self._viewname == other._viewname)
        )

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            viewname: str,
            title: str,
            desc: str,
            cols: List['ORM_Column'],
            constants: List['ObjComp_Constant'],
            methods: List['ObjComp_Method'],
            props: List['ObjComp_Property']
    ) -> None:
        '''
        ORM View Constructor
        -
        Creates a new `ORM_View` object.

        Parameters
        -
        - name : `str`
            - Name of the view ORM object.
        - viewname : `str`
            - Name of the view as it appears in the database.
        - title : `str`
            - Comment title of the view.
        - desc : `str`
            - Description of the view.
        - cols : `List<ORM_Column>`
            - Collection of columns in the view.
        - constants : `List<ObjComp_Constant>`
            - Collection of constants in the view ORM object.
        - methods : `List<ObjComp_Method>`
            - Collection of methods in the view ORM object.
        - props : `List<ObjComp_Property>`
            - Collection of properties in the view ORM object.

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            title = title,
            desc = desc,
            cols = cols,
            constants = constants,
            methods = methods,
            props = props
        )

        # set fields
        self._viewname = CompValue_Name(viewname)
        ''' Name of the view as it appears in the database. '''

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ORM_View':
        return ORM_View(
            name = self.name,
            viewname = self._viewname.data,
            title = self._title.data,
            desc = self._desc.data,
            cols = [col.Duplicate() for col in self._cols],
            constants = [constant.Duplicate() for constant in self._constants],
            methods = [method.Duplicate() for method in self._methods],
            props = [prop.Duplicate() for prop in self._props]
        )
    
    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ORM_Column':
        # get the name of the table orm object
        _name: object = data.get('name', None)
        if _name is None: # validate name existence
            raise ValueError('Failed to read Table ORM Name (`name`)')
        if not isinstance(_name, str): # validate name type
            raise TypeError(
                'Table ORM Name (`name`) expected a `str` type, got ' \
                + f'{type(_name)}'
            )
        if _name == '': # validate name data
            raise ValueError('Table ORM Name (`name`) must not be empty')

        # get the name of the table (database name)
        _tablename: object = data.get('tablename', None)
        if _tablename is None: # validate tablename existence
            raise ValueError(
                'Failed to read Table Database Name (`tablename`)'
            )
        if not isinstance(_tablename, str): # validate tablename type
            raise TypeError(
                'Table Database Name (`tablename`) expected a `str` type, ' \
                + f'got {type(_tablename)}'
            )
        if _tablename == '': # validate tablename data
            raise ValueError(
                'Table Database Name (`tablename`) must not be empty'
            )
        
        # get the title of the table orm object
        _title: object = data.get('title', None)
        if _title is None: # validate title existence
            raise ValueError('Failed to read Table Title (`title`)')
        if not isinstance(_title, str): # validate title type
            raise TypeError(
                'Table Title (`title`) expected a `str` type, got ' \
                + f'{type(_title)}'
            )
        if _title == '': # validate title data
            raise ValueError('Table Title (`title`) must not be empty')
        
        # get the description of the table orm object
        _desc: object = data.get('desc', None)
        if _desc is None: # validate description existence
            raise ValueError('Failed to read Table Description (`desc`)')
        if not isinstance(_desc, str): # validate description type
            raise TypeError(
                'Table Description (`desc`) expected a `str` type, got ' \
                + f'{type(_desc)}'
            )
        if _desc == '': # validate description data
            raise ValueError('Table Description (`desc`) must not be empty')

        # get the columns data for the table
        _cols: object = data.get('cols', None)
        if _cols is None: # validate columns existence
            raise ValueError('Failed to read Table Columns (`cols`)')
        if not isinstance(_cols, list): # validate columns type
            raise TypeError(
                'Table Columns (`cols`) expected a `list` type, got ' \
                + f'{type(_cols)}'
            )
        if len(_cols) < 1: # validate columns data
            raise ValueError(
                'Table Columns (`cols`) must contain at least one column'
            )
        cols: list[ORM_Column] = []
        for i, col in _cols:
            # validate column data is a dict
            if not isinstance(col, dict):
                raise TypeError(
                    f'Column at index `{i}` expected a `dict` type, got ' \
                    + f'{type(col)}'
                )
            
            # create column
            try:
                cols.append(ORM_Column.FromDict(col))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create column at index `{i}`: {e!r}'
                )

        # get the constants data for the table
        _consts: object = data.get('constants', None)
        if _consts is None: # validate constants existence
            raise ValueError('Failed to read Table Constants (`constants`)')
        if not isinstance(_consts, list): # validate constants type
            raise TypeError(
                'Table Constants (`constants`) expected a `list` type, got ' \
                + f'{type(_consts)}'
            )
        consts: list[ObjComp_Constant] = []
        for i, const in _consts:
            # validate constant data is a dict
            if not isinstance(const, dict):
                raise TypeError(
                    f'Constant at index `{i}` expected a `dict` type, got ' \
                    + f'{type(const)}'
                )
            
            # create constant
            try:
                consts.append(ObjComp_Constant.FromDict(const))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create constant at index `{i}`: {e!r}'
                )

        # get the methods data for the table
        _methods: object = data.get('methods', None)
        if _methods is None: # validate methods existence
            raise ValueError('Failed to read Table Methods (`methods`)')
        if not isinstance(_methods, list): # validate methods type
            raise TypeError(
                'Table Methods (`methods`) expected a `list` type, got ' \
                + f'{type(_methods)}'
            )
        methods: list[ObjComp_Method] = []
        for i, method in _methods:
            # validate method data is a dict
            if not isinstance(method, dict):
                raise TypeError(
                    f'Method at index `{i}` expected a `dict` type, got ' \
                    + f'{type(method)}'
                )
            
            # create method
            try:
                methods.append(ObjComp_Method.FromDict(method))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create method at index `{i}`: {e!r}'
                )

        # get the properties data for the table
        _props: object = data.get('props', None)
        if _props is None: # validate properties existence
            raise ValueError('Failed to read Table Properties (`props`)')
        if not isinstance(_props, list): # validate properties type
            raise TypeError(
                'Table Properties (`props`) expected a `list` type, got ' \
                + f'{type(_props)}'
            )
        props: list[ObjComp_Property] = []
        for i, prop in _props:
            # validate property data is a dict
            if not isinstance(prop, dict):
                raise TypeError(
                    f'Property at index `{i}` expected a `dict` type, got ' \
                    + f'{type(prop)}'
                )
            
            # create property
            try:
                props.append(ObjComp_Property.FromDict(prop))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create property at index `{i}`: {e!r}'
                )
            
        # create ORM_Table object
        return cls(
            name = _name,
            tablename = _tablename,
            title = _title,
            desc = _desc,
            cols = cols,
            constants = consts,
            methods = methods,
            props = props
        )

    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        data = super().GetData(lvl)
        if lvl == VerbosityLevel.SHORT:
            pass
        elif lvl == VerbosityLevel.LONG:
            data.extend([
                '_viewname',
            ])
        else:
            data.extend([
                '_viewname',
            ])
        return data
    
    # =================
    # Method - Validate
    def Validate(self) -> bool:
        raise UndefFuncError(
            'ORM_View().Validate() not defined'
        )

    # ============================
    # Method - Write Database Code
    def WriteDb(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ORM_View().WriteDb(comment = {comment}) not defined'
        )

    # =======================
    # Method - Write ORM Code
    def WriteOrm(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ORM_View().WriteOrm(comment = {comment}) not defined'
        )


# =============================================================================
# Back-Reference Import
# =============================================================================

# component values
from .component_values import (
    CompValue_Desc, # object description
    CompValue_Fk, # column foreign key
    CompValue_Name, # object name
    CompValue_Title, # object comment title
)

# object components
from .object_components import (
    ObjComp_Constant, # object constant
    ObjComp_Method, # object method
    ObjComp_Property, # object property
)


# =============================================================================
# End of File
# =============================================================================
