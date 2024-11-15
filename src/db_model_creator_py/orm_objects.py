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

# component values
from .component_values import (
    CompValue_Desc, # object description
    CompValue_Fk, # column foreign key
    CompValue_Name, # object name
    CompValue_Title, # object comment title
)

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

# object components
from .object_components import (
    ObjComp_Constant, # object constant
    ObjComp_Method, # object method
    ObjComp_Property, # object property
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
    - Duplicate() : `ORM` << override >>
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
    - Duplicate() : `ORM_Column` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_Column(...) << constructor >>
    - WriteDb(comment : `bool`) : `str`
    - WriteOrm(comment : `bool`) : `str`
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            title: str,
            desc: str,
            nullable: bool = False,
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
                to `False`, meaning the column is `NOT NULL`.
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
    - Duplicate() : `ORM_TV` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_TV(...) << constructor >>
    - WriteDb(comment : `bool`) : `str` << virtual >>
    - WriteOrm(comment : `bool`) : `str` << virtual >>
    '''

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
    - _trigger_update : `bool`

    Methods
    -
    - Duplicate() : `ORM_Table` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_Table(...) << constructor >>
    - WriteDb(comment : `bool`) : `str` << override >>
    - WriteOrm(comment : `bool`) : `str` << override >>
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
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
            - Name of the table.
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
        self._trigger_update = trigger_update
        ''' Whether or not an update trigger and table should be created to
            track the data changes in this table. '''

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ORM_Table':
        return ORM_Table(
            name = self.name,
            title = self._title.data,
            desc = self._desc.data,
            trigger_update = self._trigger_update,
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
                '_trigger_update',
            ])
        else:
            data.extend([
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
    None

    Methods
    -
    - Duplicate() : `ORM_View` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - ORM_View(...) << constructor >>
    - WriteDb(comment : `bool`) : `str` << override >>
    - WriteOrm(comment : `bool`) : `str` << override >>
    '''

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
        ORM View Constructor
        -
        Creates a new `ORM_View` object.

        Parameters
        -
        - name : `str`
            - Name of the view.
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

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ORM_View':
        return ORM_View(
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
            pass
        else:
            pass
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
# End of File
# =============================================================================
