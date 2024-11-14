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
