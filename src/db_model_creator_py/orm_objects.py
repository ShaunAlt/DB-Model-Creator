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

        raise NotImplementedError(
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

        raise NotImplementedError(
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

        raise NotImplementedError(
            f'ORM().WriteOrm(comment = {comment}) not defined in ' \
            + f'{self.__class__}'
        )


# =============================================================================
# ORM Column
# =============================================================================
class ORM_Column(OBJ):
    '''
    ORM Column
    -
    Contains the information relating to an individual column in the database
    and ORM.

    Fields
    -
    - _desc : `CompValue_Desc`
    - _fk : `CompValue_Fk | None`
    - _identity : `bool`
    - _name : `CompValue_Name`
    - _nullable : `bool`
    - _pk : `bool`
    - _title : `CompValue_Title`
    - _type : `ColumnType`
    - _unique : `bool`
    - lang_db : `LangDb | None` << static >>
    - lang_orm : `LangOrm | None` << static >>

    Methods
    -
    - Duplicate() : `ORM_Column` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - LoadData(lang_db : `LangDb`, lang_orm : `LangOrm`) : `None` << static >>
    - ORM_Column(...) << constructor >>
    - WriteDb(comment : `bool`) : `str`
    - WriteOrm(comment : `bool`) : `str`
    '''


# =============================================================================
# ORM Table / View Abstract Parent
# =============================================================================
class ORM_TV(OBJ):
    '''
    ORM Table / View Abstract Parent
    -
    Contains the information relating to an individual table or view in the
    database and ORM.

    Fields
    -
    - _cols : `List<ORM_Column>`
    - _constants : `List<ObjComp_Constant>`
    - _desc : `CompValue_Desc`
    - _methods : `List<ObjComp_Method>`
    - _name : `CompValue_Name`
    - _props : `List<ObjComp_Property>`
    - _title : `CompValue_Title`
    - lang_db : `LangDb | None` << static >>
    - lang_orm : `LangOrm | None` << static >>
    - tables : `List<ORM_Table>` << static >>
    - views : `List<ORM_View>` << static >>

    Methods
    -
    - Duplicate() : `ORM_TV` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - LoadData(...) : `None` << static >>
    - ORM_TV(...) << constructor >>
    - WriteDb(comment : `bool`) : `str` << virtual >>
    - WriteOrm(comment : `bool`) : `str` << virtual >>
    '''


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


# =============================================================================
# End of File
# =============================================================================
