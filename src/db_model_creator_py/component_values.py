# =============================================================================
# Database Model Creator - Component Values
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Component Values
-
Contains the objects that contain an individual point of data within an object
component (e.g. the name of a parameter, the description of a constant).
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

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

# used for type-hinting
from typing import (
    List, # list type-hint
    Optional, # optional datatype
)


# =============================================================================
# Abstract Component Value
# =============================================================================
class CompValue(OBJ):
    '''
    Abstract Component Value
    -
    Contains the data for a particular value within an object component.

    Fields
    -
    - _data : `str`
    - data : `str` << readonly >>
    - lang_db : `LangDb | None` << static >>
    - lang_orm : `LangOrm | None` << static >>
    - tables : `List<ORM_Table>` << static >>
    - views : `List<ORM_View>` << static >>

    Methods
    -
    - CompValue(data : `str`) << constructor >>
    - Duplicate() : `CompValue` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - LoadData(...) << static >>
    - Validate() : `bool` << abstract >>
    '''

    # =============
    # Static Fields
    lang_db: Optional[LangDb] = None
    ''' Database Language (e.g. MSSQL). '''
    lang_orm: Optional[LangOrm] = None
    ''' ORM Language (e.g. Python-SQLAlchemy). '''
    tables: List[ORM_Table] = []
    ''' All tables in the database model. '''
    views: List[ORM_View] = []
    ''' ALl views in the database model. '''

    # ====================
    # Method - Constructor
    def __init__(self, data: str) -> None:
        '''
        Abstract Component Value Constructor
        -
        Creates a new `CompValue` object.

        Parameters
        -
        - data : `str`
            - Original component value data.

        Returns
        -
        None
        '''

        # set data
        self._data: str = data
        ''' Original component value data. '''

    # ===============
    # Property - Data
    @property
    def data(self) -> str:
        ''' Original component value data. '''
        return self._data
    
    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'CompValue':
        return CompValue(data = self.data)
    
    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        if lvl == VerbosityLevel.SHORT:
            return ['data']
        elif lvl == VerbosityLevel.LONG:
            return ['data']
        else:
            return ['_data', 'data']
        
    # =========================
    # Method - Load Static Data
    @staticmethod
    def LoadData(
            lang_db: LangDb,
            lang_orm: LangOrm,
            tables: List[ORM_Table],
            views: List[ORM_View]
    ) -> None:
        '''
        Load Static Data
        -
        Loads the static data for the `CompValue` objects.

        Parameters
        -
        - lang_db : `LangDb`
            - Database Language (e.g. MSSQL).
        - lang_orm : `LangOrm`
            - ORM Language (e.g. Python-SQLAlchemy).
        - tables : `List<ORM_Table>`
            - All tables in the database model.
        - views : `List<ORM_View>`
            - All views in the database model.

        Returns
        -
        None
        '''

        # set static values
        CompValue.lang_db = lang_db
        CompValue.lang_orm = lang_orm
        CompValue.tables = tables
        CompValue.views = views

    # ======================
    # Method - Validate Data
    def Validate(self) -> bool:
        '''
        Validate Data
        -
        Validates the data for the particular component value.

        Parameters
        -
        None

        Returns
        -
        - `bool`
            - Whether or not the component value is valid.
        '''

        raise NotImplementedError(
            f'CompValue().Validate() not implemented in {self.__class__}'
        )


# =============================================================================
# Component Value - Default Value
# =============================================================================
class CompValue_Default(CompValue):
    '''
    Component Value - Default Value
    -
    Contains the default value for an object component (e.g. default parameter
    value, default constant value).

    Fields
    -
    None

    Methods
    -
    - CompValue_Default(data : `str`) << constructor >>
    - Duplicate() : `CompValue_Default` << override >>
    - Validate() : `bool` << override >>
    '''


# =============================================================================
# Component Value - Description
# =============================================================================
class CompValue_Desc(CompValue):
    '''
    Component Value - Description
    -
    Contains the description for an object component (e.g. method description,
    property description).

    Fields
    -
    None

    Methods
    -
    - CompValue_Desc(data : `str`) << constructor >>
    - Duplicate() : `CompValue_Desc` << override >>
    - Validate() : `bool` << override >>
    '''


# =============================================================================
# Component Value - Foreign Key
# =============================================================================
class CompValue_Fk(CompValue):
    '''
    Component Value - Foreign Key
    -
    Contains the foreign key of a column.

    Fields
    -
    None

    Methods
    -
    - CompValue_Fk(data : `str`) << constructor >>
    - Duplicate() : `CompValue_Fk` << override >>
    - Validate() : `bool` << override >>
    '''


# =============================================================================
# Component Value - Name
# =============================================================================
class CompValue_Name(CompValue):
    '''
    Component Value - Name
    -
    Contains the name for an object component (e.g. method name, constant name,
    property name).

    Fields
    -
    None

    Methods
    -
    - CompValue_Name(data : `str`) << constructor >>
    - Duplicate() : `CompValue_Name` << override >>
    - Validate() : `bool` << override >>
    '''


# =============================================================================
# Component Value - Title
# =============================================================================
class CompValue_Title(CompValue):
    '''
    Component Value - Title
    -
    Contains the comment title for an object component (e.g. method title,
    property comment title).

    Fields
    -
    None

    Methods
    -
    - CompValue_Title(data : `str`) << constructor >>
    - Duplicate() : `CompValue_Title` << override >>
    - Validate() : `bool` << override >>
    '''


# =============================================================================
# Component Value - Return Type
# =============================================================================
class CompValue_Type(CompValue):
    '''
    Component Value - Return Type
    -
    Contains the return type for an object component (e.g. method return type,
    property return type).

    Fields
    -
    None

    Methods
    -
    - CompValue_Type(data : `str`) << constructor >>
    - Duplicate() : `CompValue_Type` << override >>
    - Validate() : `bool` << override >>
    '''


# =============================================================================
# Back-Reference Import
# =============================================================================

# orm objects
from .orm_objects import (
    ORM_Table, # ORM table object
    ORM_View, # ORM view object
)


# =============================================================================
# End of File
# =============================================================================
