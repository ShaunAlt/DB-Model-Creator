# =============================================================================
# Database Model Creator - Object Components
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Object Components
-
Contains the objects that contain all of the component data within the ORM
objects (e.g. constants, properties).
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# generic objects
from .generic_objects import (
    ColumnType, # column datatypes
    OBJ, # base object model
    VerbosityLevel, # verbosity levels
)

# supported languagges
from .supported_languages import (
    LangDb, # supported database languages
    LangOrm, # supported ORM languages
)


# =============================================================================
# Abstract Object Component
# =============================================================================
class ObjComp(OBJ):
    '''
    Abstract Object Component
    -
    Contains the common attributes and methods for all object components.

    Fields
    -
    - _default : `CompValue_Default | None`
    - _desc : `CompValue_Desc`
    - _name : `CompValue_Name`
    - _title : `CompValue_Title | None`
    - _type : `CompValue_Type`
    - lang_orm : `LangOrm | None` << static >>
    - valid : `bool` << virtal, readonly >>
    - valid_default : `bool` << readonly >>
    - valid_desc : `bool` << readonly >>
    - valid_name : `bool` << readonly >>
    - valid_title : `bool` << readonly >>
    - valid_type : `bool` << readonly >>

    Methods
    -
    - Duplicate() : `ObjComp` << override >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - LoadData(lang_orm : `LangOrm`) : `None` << static >>
    - ObjComp(...) << constructor >>
    - Write(comment : `bool`) : `str` << abstract >>
    '''


# =============================================================================
# Object Component - Constant
# =============================================================================
class ObjComp_Constant(ObjComp):
    '''
    Object Component - Constant
    -
    Contains the information about an individual constant within an ORM object.

    Fields
    -
    None

    Methods
    -
    - Duplicate() : `ObjComp_Constant` << override >>
    - ObjComp_Constant(...) << constructor >>
    - Write(comment : `bool`) : `str` << override >>
    '''


# =============================================================================
# Object Component - Method
# =============================================================================
class ObjComp_Method(ObjComp):
    '''
    Object Component - Method
    -
    Contains the information about an individual method within an ORM object.

    Fields
    -
    - _method_type : `MethodType`
    - _params : `List<ObjComp_MethodParam>`
    - valid : `bool` << override, readonly >>
    - valid_params : `bool` << readonly >>

    Methods
    -
    - Duplicate() : `ObjComp_Method` << override >>
    - ObjComp_Method(...) << constructor >>
    - Write(comment : `bool`) : `str` << override >>
    '''


# =============================================================================
# Object Component - Method Parameter
# =============================================================================
class ObjComp_MethodParam(ObjComp):
    '''
    Object Component - Constant
    -
    Contains the information about an individual parameter within a method
    within an ORM object.

    Fields
    -
    None

    Methods
    -
    - Duplicate() : `ObjComp_MethodParam` << override >>
    - ObjComp_MethodParam(...) << constructor >>
    - Write(comment : `bool`) : `str` << override >>
    '''


# =============================================================================
# Object Component - Property
# =============================================================================
class ObjComp_Property(ObjComp):
    '''
    Object Component - Property
    -
    Contains the information about an individual property within an ORM object.

    Fields
    -
    None

    Methods
    -
    - Duplicate() : `ObjComp_Property` << override >>
    - ObjComp_Property(...) << constructor >>
    - Write(comment : `bool`) : `str` << override >>
    '''


# =============================================================================
# End of File
# =============================================================================
