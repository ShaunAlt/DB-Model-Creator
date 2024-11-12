# =============================================================================
# Database Model Creator - Models
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Models
-
Contains all of the objects that are used for reading, defining, and writing
the database model.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for project configuration
from .config import (
    OBJ,
)

# used for pre-defined data types
from .types import (
    TYPES_METHOD, # method types (e.g. instance, static)
    TYPES_PYTHON3, # DatabaseLang.PYTHON3 data types
)

# used for creating enumeration objects
from enum import Enum

# used for regular expressions
import regex as re

# used for type hinting
from typing import (
    List,
    Optional,
    Type,
)


# =============================================================================
# Models
# =============================================================================

# ======================
# Overall Database Model
class Database(OBJ):
    '''
    Overall Database Model
    -
    Contains all of the objects that are used for reading, defining, and
    writing the database model.

    Attributes
    -
    None

    Static Attributes
    -
    - PREFIX_TABLENAME : `str`
        - String to prepend to the ORM objects for each database table.
    - PREFIX_VIEWNAME : `str`
        - String to prepend to the ORM objects for each database view.

    Methods
    -
    None

    Properties
    -
    None
    '''

    # ==========================
    # Static - Table Name Prefix
    PREFIX_TABLENAME = 'DB_'
    ''' String to prepend to the ORM objects for each database table. '''

    # ==========================
    # Static - View Name Prefix
    PREFIX_VIEWNAME = 'VW_'
    ''' String to prepend to the ORM objects for each database view. '''

# =================
# Database ORM Enum
class Database_Orm(Enum):
    '''
    Database ORM Enum
    -
    Contains a collection of all valid database ORMs (e.g. `python-sqlalchemy`)
    that are supported.
    '''

    PYTHON_SQLALCHEMY = 'python-sqlalchemy'
    ''' Python with SQLAlchemy. '''

# ======================
# Database Language Enum
class Database_Lang(Enum):
    '''
    Database Language Enum
    -
    Contains a collection of all valid database languages (e.g. `python`) that
    are supported.
    '''

    PYTHON3 = 'python3'
    ''' Python 3.X. '''

    # ==================
    # Get Language Types
    @classmethod
    def get_language_types(cls, lang: 'Database_Lang') -> Type[Enum]:
        '''
        Get Language Types
        -
        Gets the language type enumerator for the specified language.

        Parameters
        -
        - lang : `Database_Lang`
            - The language to get the language types for.

        Returns
        -
        - `Enum`
            - Enumerator of the backend pre-defined data types for the
                specified language.
        '''

        if lang == cls.PYTHON3: return TYPES_PYTHON3
        else: raise ValueError(f'Unsupported language: {lang}')

# ==================
# Database Type Enum
class Database_Type(Enum):
    '''
    Database Type Enum
    -
    Contains a collection of all valid database types (e.g. `mssql`) that are
    supported.
    '''

    MSSQL = 'mssql'
    ''' Microsoft SQL Server. '''

# ======================
# Object Data Definition
class ObjData(OBJ):
    '''
    Object Data Definition
    -
    Contains the data of a particular component within an ORM object. Used by
    specific object data definition child objects for added functionality.

    Attributes
    -
    - _desc : `Value_Desc`
        - Description of the component.
    - _name : `Value_Name`
        - Name of the component.
    - _type : `Value_Type`
        - Return type of the component.
    
    Static Attributes
    -
    None

    Methods
    -
    - __init__(name, type_, lang, desc) : `None`
        - Constructor Method.
        - Creates a new `ObjData` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `ObjData`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not all attributes are valid.
    - valid_desc : `bool`
        - Readonly.
        - Whether or not the component description is valid.
    - valid_name : `bool`
        - Readonly.
        - Whether or not the component name is valid.
    - valid_type : `bool`
        - Readonly.
        - Whether or not the component return type is valid.
    - value_desc : `str`
        - Readonly.
        - Re-formatted string representation of the component description.
    - value_name : `str`
        - Readonly.
        - Re-formatted string representation of the component name.
    - value_type : `str`
        - Readonly.
        - Re-formatted string representation of the component return datatype.
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            lang: Database_Lang,
            desc: str
    ) -> None:
        '''
        `ObjData` Constructor
        -
        Creates a new `ObjData` object.

        Parameters
        -
        - name : `str`
            - Name of the component.
        - type_ : `str`
            - Return type of the component.
        - lang : `Database_Lang`
            - ORM language.
        - desc : `str`
            - Description of the component.

        Returns
        -
        None
        '''

        # set attributes
        self._desc = Value_Desc(desc)
        ''' Description of the component. '''
        self._name = Value_Name(name)
        ''' Name of the component. '''
        self._type = Value_Type(type_, lang)
        ''' Return type of the component. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        ''' Whether or not all attributes are valid. '''
        return self.valid_desc and self.valid_name and self.valid_type

    # ==============================
    # Property - Valid - Description
    @property
    def valid_desc(self) -> bool:
        ''' Whether or not the component description is valid. '''
        return self._desc.valid

    # =======================
    # Property - Valid - Name
    @property
    def valid_name(self) -> bool:
        ''' Whether or not the component name is valid. '''
        return self._name.valid

    # =======================
    # Property - Valid - Type
    @property
    def valid_type(self) -> bool:
        ''' Whether or not the component return type is valid. '''
        return self._type.valid

    # ==============================
    # Property - Value - Description
    @property
    def value_desc(self) -> str:
        ''' Re-formatted string representation of the component
            description. '''
        return self._desc.value
    
    # =======================
    # Property - Value - Name
    @property
    def value_name(self) -> str:
        ''' Re-formatted string representation of the component name. '''
        return self._name.value

    # =======================
    # Property - Value - Type
    @property
    def value_type(self) -> str:
        ''' Re-formatted string representation of the component return
            datatype. '''
        return self._type.value

    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        if lvl == OBJ.Verbosity_Level.SHORT:
            return ['value_name', 'value_type', 'valid']
        elif lvl == OBJ.Verbosity_Level.LONG:
            return [
                'valid',
                'valid_desc',
                'valid_name',
                'valid_type',
                'value_name',
                'value_type',
                'value_desc',
            ]
        else:
            return [
                '_desc',
                '_name',
                '_type',
                'valid',
                'valid_desc',
                'valid_name',
                'valid_type',
                'value_name',
                'value_type',
                'value_desc',
            ]

    # =========================
    # Method - Duplicate Object
    def duplicate(self) -> 'ObjData':
        return ObjData(
            name = self._name._data,
            type_ = self._type._data,
            lang = self._type._lang,
            desc = self._desc._data
        )

# =================================
# Object Data Definition - Constant
class ObjData_Constant(ObjData):
    '''
    Object Data Definition - Constant
    -
    Contains the information about an individual constant within an ORM object.

    Attributes
    -
    - _default : `Value_Default | None`
        - Default value of the constant. Defaults to `None`, meaning an error
            will be used instead of the default value.
    - _desc : `Value_Desc`
        - Description of the constant.
    - _name : `Value_Name`
        - Name of the constant.
    - _title : `Value_Title`
        - Commented title of the constant.
    - _type : `Value_Type`
        - Datatype of the constant.

    Methods
    -
    - __init__(name, type_, lang, desc, title, default=None) : `None`
        - Constructor Method.
        - Creates a new `ObjData_Constant` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `ObjData_Constant`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not all attributes are valid.
    - valid_default : `bool`
        - Readonly.
        - Whether or not the component default value is valid.
    - valid_desc : `bool`
        - Readonly.
        - Whether or not the component description is valid.
    - valid_name : `bool`
        - Readonly.
        - Whether or not the component name is valid.
    - valid_title : `bool`
        - Readonly.
        - Whether or not the component title is valid.
    - valid_type : `bool`
        - Readonly.
        - Whether or not the component return type is valid.
    - value_default : `str`
        - Readonly.
        - Re-formatted string representation of the component default value.
    - value_desc : `str | None`
        - Readonly.
        - Re-formatted string representation of the component description.
    - value_name : `str`
        - Readonly.
        - Re-formatted string representation of the component name.
    - value_title : `str`
        - Readonly.
        - Re-formatted string representation of the component title.
    - value_type : `str`
        - Readonly.
        - Re-formatted string representation of the component return datatype.
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            lang: Database_Lang,
            desc: str,
            title: str,
            default: Optional[str] = None
    ) -> None:
        '''
        `ObjData_Constant` Constructor
        -
        Creates a new `ObjData_Constant` object.

        Parameters
        -
        - name : `str`
            - Name of the constant.
        - type_ : `str`
            - Datatype of the constant.
        - lang : `Database_Lang`
            - ORM language.
        - desc : `str`
            - Description of the constant.
        - title : `str`
            - Commented title of the constant.
        - default : `str | None`
            - Default value of the constant. Defaults to `None`, meaning an
                error will be used instead of the default value.

        Returns
        -
        None
        '''

        # initialize parent object data
        super().__init__(name, type_, lang, desc)

        # initialize attributes
        self._default = Value_Default(default) if default else None
        ''' Default value of the constant. Defaults to `None`, meaning an
            error will be used instead of the default value. '''
        self._title = Value_Title(title)
        ''' Commented title of the constant. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        ''' Whether or not all attributes are valid. '''
        return super().valid and self.valid_default and self.valid_title

    # ================================
    # Property - Valid - Default Value
    @property
    def valid_default(self) -> bool:
        ''' Whether or not the component default value is valid. '''
        return (
            (self._default is None)
            or (self._default.valid)
        )
    
    # ========================
    # Property - Valid - Title
    @property
    def valid_title(self) -> bool:
        ''' Whether or not the component title is valid. '''
        return self._title.valid

    # ================================
    # Property - Value - Default Value
    @property
    def value_default(self) -> Optional[str]:
        ''' Re-formatted string representation of the component default
            value. '''
        return self._default.value if self._default else None
    
    # ========================
    # Property - Value - Title
    @property
    def value_title(self) -> Optional[str]:
        ''' Re-formatted string representation of the component title. '''
        return self._title.value

    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        # get parent data
        data = super()._get_data(lvl)

        # add additional attributes
        if lvl == OBJ.Verbosity_Level.SHORT:
            data.append('value_default')
        elif lvl == OBJ.Verbosity_Level.LONG:
            data.extend([
                'valid_default',
                'valid_title',
                'value_default',
                'value_title',
            ])
        else:
            data.extend([
                '_default',
                '_title',
                'valid_default',
                'valid_title',
                'value_default',
                'value_title',
            ])

        return data

    # =========================
    # Method - Duplicate Object
    def duplicate(self) -> 'ObjData_Constant':
        return ObjData_Constant(
            name = self._name._data,
            type_ = self._type._data,
            lang = self._type._lang,
            desc = self._desc._data,
            title = self._title._data,
            default = self._default._data if self._default else None
        )

# ===============================
# Object Data Definition - Method
class ObjData_Method(ObjData):
    '''
    Object Data Definition - Method
    -
    Contains the information about an individual method within an ORM object.

    Attributes
    -
    - _desc : `Value_Desc`
        - Description of the method.
    - _method_type : `TYPES_METHOD`
        - Type of method being created.
    - _name : `Value_Name`
        - Name of the method.
    - _params : `list[ObjData_MethodParam]`
        - Collection of parameters for the method.
    - _title : `Value_Title`
        - Commented title of the method.
    - _type : `Value_Type`
        - Datatype of the method.

    Methods
    -
    - __init__(name, type_, lang, desc, method_type, params, title) : `None`
        - Constructor Method.
        - Creates a new `ObjData_Method` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `ObjData_Method`
        - `OBJ` Instance Method.

    Properties
    -
    - method_type : `TYPES_METHOD`
        - Readonly.
        - Type of method being created.
    - params : `list[ObjData_MethodParam]`
        - Readonly.
        - Collection of parameters for the method.
    - valid : `bool`
        - Readonly.
        - Whether or not all attributes are valid.
    - valid_desc : `bool`
        - Readonly.
        - Whether or not the component description is valid.
    - valid_name : `bool`
        - Readonly.
        - Whether or not the component name is valid.
    - valid_params : `bool`
        - Readonly.
        - Whether or not the component parameters are valid.
    - valid_title : `bool`
        - Readonly.
        - Whether or not the component title is valid.
    - valid_type : `bool`
        - Readonly.
        - Whether or not the component return type is valid.
    - value_desc : `str | None`
        - Readonly.
        - Re-formatted string representation of the component description.
    - value_name : `str`
        - Readonly.
        - Re-formatted string representation of the component name.
    - value_title : `str`
        - Readonly.
        - Re-formatted string representation of the component title.
    - value_type : `str`
        - Readonly.
        - Re-formatted string representation of the component return datatype.
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            lang: Database_Lang,
            desc: str,
            method_type: TYPES_METHOD,
            params: list['ObjData_MethodParam'],
            title: str
    ) -> None:
        '''
        `ObjData_Method` Constructor
        -
        Creates a new `ObjData_Method` object.

        Parameters
        -
        - name : `str`
            - Name of the method parameter.
        - type_ : `str`
            - Datatype of the method parameter.
        - lang : `Database_Lang`
            - ORM language.
        - desc : `str`
            - Description of the method parameter.
        - method_type : `TYPES_METHOD`
            - Type of method being created.
        - params : `list[ObjData_MethodParam]`
            - Collection of parameters for the method.
        - title : `str`
            - Commented title of the method.

        Returns
        -
        None
        '''

        # initialize parent object data
        super().__init__(name, type_, lang, desc)

        # initialize attributes
        self._method_type = method_type
        ''' Type of method being created. '''
        self._params = params
        ''' Collection of parameters for the method. '''
        self._title = Value_Title(title)
        ''' Commented title of the method. '''

    # ======================
    # Property - Method Type
    @property
    def method_type(self) -> TYPES_METHOD:
        ''' Type of method being created. '''
        return self._method_type
    
    # ============================
    # Property - Method Parameters
    @property
    def params(self) -> List['ObjData_MethodParam']:
        ''' Collection of parameters for the method. '''
        return self._params

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        ''' Whether or not all attributes are valid. '''
        return super().valid and self.valid_params
    
    # ====================================
    # Property - Valid - Method Parameters
    @property
    def valid_params(self) -> bool:
        ''' Whether or not the component parameters are valid. '''
        return all(param.valid for param in self._params)
    
    # ========================
    # Property - Valid - Title
    @property
    def valid_title(self) -> bool:
        ''' Whether or not the component title is valid. '''
        return self._title.valid
    
    # ========================
    # Property - Value - Title
    @property
    def value_title(self) -> str:
        ''' Re-formatted string representation of the component title. '''
        return self._title.value

    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        # get parent data
        data = super()._get_data(lvl)

        # add additional attributes
        if lvl == OBJ.Verbosity_Level.SHORT:
            data.append('method_type')
        elif lvl == OBJ.Verbosity_Level.LONG:
            data.extend([
                'method_type',
                'params',
                'valid_title',
                'value_title',
            ])
        else:
            data.extend([
                '_method_type',
                '_params',
                '_title',
                'method_type',
                'params',
                'valid_params',
                'valid_title',
                'value_title',
            ])

        return data

    # =========================
    # Method - Duplicate Object
    def duplicate(self) -> 'ObjData_Method':
        return ObjData_Method(
            name = self._name._data,
            type_ = self._type._data,
            lang = self._type._lang,
            desc = self._desc._data,
            method_type = self.method_type,
            params = [param.duplicate() for param in self.params],
            title = self._title._data
        )

# =========================================
# Object Data Definition - Method Parameter
class ObjData_MethodParam(ObjData):
    '''
    Object Data Definition - Method Parameter
    -
    Contains the information about an individual method parameter within an ORM
    object.

    Attributes
    -
    - _default : `Value_Default | None`
        - Default value of the method parameter. Defaults to `None`, meaning
            the method parameter is a positional argument instead of a keyword
            argument.
    - _desc : `Value_Desc`
        - Description of the method parameter.
    - _name : `Value_Name`
        - Name of the method parameter.
    - _type : `Value_Type`
        - Datatype of the method parameter.

    Methods
    -
    - __init__(name, type_, lang, desc, default=None) : `None`
        - Constructor Method.
        - Creates a new `ObjData_MethodParam` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `ObjData_MethodParam`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not all attributes are valid.
    - valid_default : `bool`
        - Readonly.
        - Whether or not the component default value is valid.
    - valid_desc : `bool`
        - Readonly.
        - Whether or not the component description is valid.
    - valid_name : `bool`
        - Readonly.
        - Whether or not the component name is valid.
    - valid_type : `bool`
        - Readonly.
        - Whether or not the component return type is valid.
    - value_default : `str`
        - Readonly.
        - Re-formatted string representation of the component default value.
    - value_desc : `str | None`
        - Readonly.
        - Re-formatted string representation of the component description.
    - value_name : `str`
        - Readonly.
        - Re-formatted string representation of the component name.
    - value_type : `str`
        - Readonly.
        - Re-formatted string representation of the component return datatype.
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            lang: Database_Lang,
            desc: str,
            default: Optional[str] = None
    ) -> None:
        '''
        `ObjData_MethodParam` Constructor
        -
        Creates a new `ObjData_MethodParam` object.

        Parameters
        -
        - name : `str`
            - Name of the method parameter.
        - type_ : `str`
            - Datatype of the method parameter.
        - lang : `Database_Lang`
            - ORM language.
        - desc : `str`
            - Description of the method parameter.
        - default : `str | None`
            - Default value of the method parameter. Defaults to `None`,
                meaning the method parameter is a positional argument instead
                of a keyword argument.

        Returns
        -
        None
        '''

        # initialize parent object data
        super().__init__(name, type_, lang, desc)

        # initialize attributes
        self._default = Value_Default(default) if default else None
        '''  Default value of the method parameter. Defaults to `None`, meaning
            the method parameter is a positional argument instead of a keyword
            argument. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        ''' Whether or not all attributes are valid. '''
        return super().valid and self.valid_default

    # ================================
    # Property - Valid - Default Value
    @property
    def valid_default(self) -> bool:
        ''' Whether or not the component default value is valid. '''
        return (
            (self._default is None)
            or (self._default.valid)
        )

    # ================================
    # Property - Value - Default Value
    @property
    def value_default(self) -> Optional[str]:
        ''' Re-formatted string representation of the component default
            value. '''
        return self._default.value if self._default else None

    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        # get parent data
        data = super()._get_data(lvl)

        # add additional attributes
        if lvl == OBJ.Verbosity_Level.SHORT:
            data.append('value_default')
        elif lvl == OBJ.Verbosity_Level.LONG:
            data.extend([
                'valid_default',
                'value_default',
            ])
        else:
            data.extend([
                '_default',
                'valid_default',
                'value_default',
            ])

        return data

    # =========================
    # Method - Duplicate Object
    def duplicate(self) -> 'ObjData_MethodParam':
        return ObjData_MethodParam(
            name = self._name._data,
            type_ = self._type._data,
            lang = self._type._lang,
            desc = self._desc._data,
            default = self._default._data if self._default else None
        )

# =================================
# Object Data Definition - Property
class ObjData_Property(ObjData):
    '''
    Object Data Definition - Property
    -
    Contains the information about an individual property within an ORM object.

    Attributes
    -
    - _default : `Value_Default | None`
        - Default value of the property. Defaults to `None`, meaning an error
            will be used instead of the default return value.
    - _desc : `Value_Desc`
        - Description of the property.
    - _name : `Value_Name`
        - Name of the property.
    - _title : `Value_Title`
        - Commented title of the property.
    - _type : `Value_Type`
        - Datatype of the property.

    Methods
    -
    - __init__(name, type_, lang, desc, title, default=None) : `None`
        - Constructor Method.
        - Creates a new `ObjData_Property` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `ObjData_Property`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not all attributes are valid.
    - valid_default : `bool`
        - Readonly.
        - Whether or not the component default value is valid.
    - valid_desc : `bool`
        - Readonly.
        - Whether or not the component description is valid.
    - valid_name : `bool`
        - Readonly.
        - Whether or not the component name is valid.
    - valid_title : `bool`
        - Readonly.
        - Whether or not the component title is valid.
    - valid_type : `bool`
        - Readonly.
        - Whether or not the component return type is valid.
    - value_default : `str`
        - Readonly.
        - Re-formatted string representation of the component default value.
    - value_desc : `str | None`
        - Readonly.
        - Re-formatted string representation of the component description.
    - value_name : `str`
        - Readonly.
        - Re-formatted string representation of the component name.
    - value_title : `str`
        - Readonly.
        - Re-formatted string representation of the component title.
    - value_type : `str`
        - Readonly.
        - Re-formatted string representation of the component return datatype.
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            lang: Database_Lang,
            desc: str,
            title: str,
            default: Optional[str] = None
    ) -> None:
        '''
        `ObjData_Property` Constructor
        -
        Creates a new `ObjData_Property` object.

        Parameters
        -
        - name : `str`
            - Name of the property.
        - type_ : `str`
            - Datatype of the property.
        - lang : `Database_Lang`
            - ORM language.
        - desc : `str`
            - Description of the property.
        - title : `str`
            - Commented title of the property.
        - default : `str | None`
            - Default value of the property. Defaults to `None`, meaning an
                error will be used instead of the default return value.

        Returns
        -
        None
        '''

        # initialize parent object data
        super().__init__(name, type_, lang, desc)

        # initialize attributes
        self._default = Value_Default(default) if default else None
        ''' Default value of the property. Defaults to `None`, meaning an
            error will be used instead of the default return value. '''
        self._title = Value_Title(title)
        ''' Commented title of the property. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        ''' Whether or not all attributes are valid. '''
        return super().valid and self.valid_default and self.valid_title

    # ================================
    # Property - Valid - Default Value
    @property
    def valid_default(self) -> bool:
        ''' Whether or not the component default value is valid. '''
        return (
            (self._default is None)
            or (self._default.valid)
        )
    
    # ========================
    # Property - Valid - Title
    @property
    def valid_title(self) -> bool:
        ''' Whether or not the component title is valid. '''
        return self._title.valid
    
    # ================================
    # Property - Value - Default Value
    @property
    def value_default(self) -> Optional[str]:
        ''' Re-formatted string representation of the component default
            value. '''
        return self._default.value if self._default else None

    # ========================
    # Property - Value - Title
    @property
    def value_title(self) -> Optional[str]:
        ''' Re-formatted string representation of the component title. '''
        return self._title.value

    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        # get parent data
        data = super()._get_data(lvl)

        # add additional attributes
        if lvl == OBJ.Verbosity_Level.SHORT:
            data.append('value_default')
        elif lvl == OBJ.Verbosity_Level.LONG:
            data.extend([
                'valid_default',
                'valid_title',
                'value_default',
                'value_title',
            ])
        else:
            data.extend([
                '_default',
                '_title',
                'valid_default',
                'valid_title',
                'value_default',
                'value_title',
            ])

        return data

    # =========================
    # Method - Duplicate Object
    def duplicate(self) -> 'ObjData_Property':
        return ObjData_Property(
            name = self._name._data,
            type_ = self._type._data,
            lang = self._type._lang,
            desc = self._desc._data,
            title = self._title._data,
            default = self._default._data if self._default else None
        )

# ==============================
# ORM Object Definition - Column

# =============================
# ORM Object Definition - Table

# ============================
# ORM Object Definition - View

# ================
# Value Definition
class Value(OBJ):
    '''
    Value Definition
    -
    Contains the value of a particular component within the overall database.
    Used by specific value definition child objects for added functionality.

    Attributes
    -
    - _data : `str`
        - Original value.

    Static Attributes
    -
    None

    Methods
    -
    - __init__(data) : `None`
        - Constructor Method.
        - Creates a new `Value` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `Value`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not the data is valid.
    - value : `str`
        - Readonly.
        - A re-formatted version of the original data.
    '''

    # ====================
    # Method - Constructor
    def __init__(self, data: str) -> None:
        '''
        `Value` Constructor
        -
        Creates a new `Value` object.

        Parameters
        -
        - data : `str`
            - Original value.

        Returns
        -
        None
        '''

        # set data
        self._data: str = data
        ''' Original value. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        ''' Whether or not the data is valid. '''
        raise NotImplementedError(
            f'Value().valid not defined in {self.__class__}'
        )
    
    # ================
    # Property - Value
    @property
    def value(self) -> str:
        ''' A re-formatted version of the original value. '''
        raise NotImplementedError(
            f'Value().value not defined in {self.__class__}'
        )
    
    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        if lvl == Value.Verbosity_Level.SHORT:
            return ['value']
        else:
            return ['_data', 'valid', 'value']
        
    # ==================
    # Method - Duplicate
    def duplicate(self) -> 'Value':
        ''' Creates a duplicate of the current `Value` object. '''
        return self.__class__(self._data)

# ================================
# Value Definition - Default Value
class Value_Default(Value):
    '''
    Value Definition - Default Value
    -
    Contains the default value of a particular component within the overall
    database (e.g. default parameter value).

    Attributes
    -
    - _data : `str`
        - Original value.
    
    Static Attributes
    -
    None

    Methods
    -
    - __init__(data) : `None`
        - Constructor Method.
        - Creates a new `Value_Default` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `Value`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not the data is valid.
    - value : `str`
        - Readonly.
        - A re-formatted version of the original data.
    '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        '''
        Whether or not the data is valid.
        
        Requirements
        - None
        '''

        return True
    
    # ================
    # Property - Value
    @property
    def value(self) -> str:
        ''' A re-formatted version of the original value. '''
        return str(self._data).strip()

# ==============================
# Value Definition - Description
class Value_Desc(Value):
    '''
    Value Definition - Description
    -
    Contains the description of a particular component within the overall
    database (e.g. table description, property description).

    Attributes
    -
    - _data : `str`
        - Original value.
    
    Static Attributes
    -
    None

    Methods
    -
    - __init__(data) : `None`
        - Constructor Method.
        - Creates a new `Value_Desc` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `Value`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not the data is valid.
    - value : `str`
        - Readonly.
        - A re-formatted version of the original data.
    '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        '''
        Whether or not the data is valid.
        
        Requirements
        - None
        '''

        return True
    
    # ================
    # Property - Value
    @property
    def value(self) -> str:
        ''' A re-formatted version of the original value. '''
        return str(self._data).strip()

# ==============================
# Value Definition - Foreign Key
class Value_Fk(Value):
    '''
    Value Definition - Foreign Key
    -
    Contains the string representation of a particular foreign key constraint
    in the database.

    Attributes
    -
    - _data : `str`
        - Original value.
    
    Static Attributes
    -
    - TABLES : `list[str]`
        - Collection of all table in the database (so that types can
            reference that ORM object).

    Methods
    -
    - __init__(data) : `None`
        - Constructor Method.
        - Creates a new `Value_Fk` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `Value`
        - `OBJ` Instance Method.
    - update_static(tables) : `None`
        - Static Method.
        - Updates the `TABLES` static attribute with the provided tables.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not the data is valid.
    - value : `str`
        - Readonly.
        - A re-formatted version of the original data.
    '''

    # ====================
    # Static - Table Names
    TABLES: List[None] = []
    ''' Collection of all tables in the database (so that types can
        reference that ORM object). '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        '''
        Whether or not the data is valid.
        
        Requirements
        - Should contain the table and column names of the primary key that the
            foreign key should be associated with.
        '''

        # get original data
        data: str = str(self._data).strip()

        # validate it contains 2 period-delimited strings
        if len(data.split('.')) != 2: return False

        # get the table and column names
        table_name, column_name = data.split('.')

        # check if table and column names exist in the tables
        # if (
        #     (table_name not in Value_Fk.TABLES)
        #     or (column_name not in Value_Type.TABLE_COLUMNS[table_name])
        # ): return False
        raise NotImplementedError(
            f'Value_Fk(data = {self._data}).valid not fully defined'
        )
        
    # ================
    # Property - Value
    @property
    def value(self) -> str:
        ''' A re-formatted version of the original value. '''
        return str(self._data).strip()

    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        data: List[str] = super()._get_data(lvl)
        if lvl == OBJ.Verbosity_Level.ALL:
            data += ['TABLES']
        return data
    
    # ====================================
    # Method - Update Table and View Names
    @staticmethod
    def update_static(tables: None, views: None) -> None:
        '''
        Update Table and View Names
        -
        Updates the `TABLES` static attribute with the provided tables.

        Parameters
        -
        - tables : `TODO`
            - Collection of all tables in the database.

        Returns
        -
        None
        '''

        raise NotImplementedError(
            f'Value_Fk.update_static(tables = {tables}) not had the ' \
            + 'functionality defined.'
        )

# =======================
# Value Definition - Name
class Value_Name(Value):
    '''
    Value Definition - Name
    -
    Contains the name of a particular component within the overall database
    (e.g. table name, property name).

    Attributes
    -
    - _data : `str`
        - Original value.
    
    Static Attributes
    -
    None

    Methods
    -
    - __init__(data) : `None`
        - Constructor Method.
        - Creates a new `Value_Name` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `Value`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not the data is valid.
    - value : `str`
        - Readonly.
        - A re-formatted version of the original data.
    '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        '''
        Whether or not the data is valid.
        
        Requirements
        - Starts with a lowercase or uppercase letter, or underscore.
        - Contains only lowercase or uppercase letters, numbers, or
            underscores.
        '''
        # use regex to validate expression
        return re.search(
            "^[a-zA-Z_][a-zA-Z0-9_]*$",
            str(self._data).strip()
        ) is not None
    
    # ================
    # Property - Value
    @property
    def value(self) -> str:
        ''' A re-formatted version of the original value. '''
        return str(self._data).strip()

# ========================
# Value Definition - Title
class Value_Title(Value):
    '''
    Value Definition - Title
    -
    Contains the commented title of a particular component within the overall
    database (e.g. constant title comment, property title comment).

    Attributes
    -
    - _data : `str`
        - Original value.
    
    Static Attributes
    -
    None

    Methods
    -
    - __init__(data) : `None`
        - Constructor Method.
        - Creates a new `Value_Title` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `Value`
        - `OBJ` Instance Method.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not the data is valid.
    - value : `str`
        - Readonly.
        - A re-formatted version of the original data.
    '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        '''
        Whether or not the data is valid.
        
        Requirements
        - Single Line String
        '''

        # get data
        data = str(self._data).strip()

        return (
            ('\n' not in data)
            and ('\r' not in data)
        )
    
    # ================
    # Property - Value
    @property
    def value(self) -> str:
        ''' A re-formatted version of the original value. '''
        return str(self._data).strip()

# =======================
# Value Definition - Type
class Value_Type(Value):
    '''
    Value Definition - Type
    -
    Contains the string representation of a particular data type in the backend
    language (e.g. property return type).

    Attributes
    -
    - _data : `str`
        - Original value.
    - _lang : `Database_Lang`
        - Backend language (e.g. 'Database_Lang.PYTHON3').
    
    Static Attributes
    -
    - TABLE_NAMES : `list[str]`
        - Collection of all table names in the database (so that types can
            reference that ORM object).
    - VIEW_NAMES : `list[str]`
        - Collection of all view names in the database (so that types can
            reference that ORM object).

    Methods
    -
    - __init__(data, lang) : `None`
        - Constructor Method.
        - Creates a new `Value_Type` object.
    - _get_data(lvl) : `List[str]`
        - `OBJ` Instance Method.
    - duplicate() : `Value`
        - `OBJ` Instance Method.
    - update_static(tables, views) : `None`
        - Static Method.
        - Updates the `TABLE_NAMES` and `VIEW_NAMES` static attributes with
            the provided tables and views.

    Properties
    -
    - valid : `bool`
        - Readonly.
        - Whether or not the data is valid.
    - value : `str`
        - Readonly.
        - A re-formatted version of the original data.
    '''

    # ====================
    # Static - Table Names
    TABLE_NAMES: List[str] = []
    ''' Collection of all table names in the database (so that types can
        reference that ORM object). '''
    VIEW_NAMES: List[str] = []
    ''' Collection of all view names in the database (so that types can
        reference that ORM object). '''

    # ===========
    # Constructor
    def __init__(self, data: str, lang: Database_Lang) -> None:
        '''
        `Value_Type` Constructor
        -
        Creates a new `Value_Type` object.

        Parameters
        -
        - data : `str`
            - Original value.
        - lang : `Database_Lang`
            - Backend language.

        Returns
        -
        None
        '''

        super().__init__(data)

        # set language
        self._lang: Database_Lang = lang
        ''' Backend language. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        '''
        Whether or not the data is valid.
        
        Requirements
        - Comma-delimited (could reference multiple types).
        - Each individual type must be valid in either the pre-defined language
            types, or a table or view name.
        '''

        # get original data
        data: str = str(self._data).strip()
        if len(data) == 0: return True # default to `None / null`

        # get language types
        lang_types: Type[Enum] = Database_Lang.get_language_types(self._lang)

        # split data by commas, and validate
        for type_str in data.split(','):
            type_str = type_str.strip() # remove whitespace

            # if not pre-defined, table name, or view name - invalid
            if (
                (type_str in lang_types)
                or (type_str in Value_Type.TABLE_NAMES)
                or (type_str in Value_Type.VIEW_NAMES)
            ): return False

        return True
    
    # ================
    # Property - Value
    @property
    def value(self) -> str:
        ''' A re-formatted version of the original value. '''

        # get original data
        data: str = str(self._data).strip()

        # get language types
        lang_types: Type[Enum] = Database_Lang.get_language_types(self._lang)

        # handle python data
        if self._lang == Database_Lang.PYTHON3:
            # default value
            if len(data) == 0: return TYPES_PYTHON3.NONE.value

            # method to convert individual value to valid string
            def value_to_string_python3(val: str):
                # pre-defined type
                if val in lang_types:
                    return val

                # table name
                if val in Value_Type.TABLE_NAMES:
                    return f'\'{Database.PREFIX_TABLENAME}{val}\''

                # view name
                if val in Value_Type.VIEW_NAMES:
                    return f'\'{Database.PREFIX_VIEWNAME}{val}\''

                # default to string
                return f'"{val}"'

            # get string of all values
            values_str = ', '.join([
                value_to_string_python3(val.strip())
                for val in data.split(',')
            ])

            # add brackets if required
            if len(data.split(',')) > 1:
                values_str = f'{TYPES_PYTHON3.UNION}[{values_str}]'

            return values_str

        raise ValueError(f'Database language {self._lang} is not supported')

    # =================
    # Method - Get Data
    def _get_data(self, lvl: OBJ.Verbosity_Level) -> List[str]:
        data: List[str] = super()._get_data(lvl)
        if lvl != OBJ.Verbosity_Level.SHORT:
            data += ['_lang']
        if lvl == OBJ.Verbosity_Level.ALL:
            data += ['TABLE_NAMES', 'VIEW_NAMES']
        return data
    
    # ====================================
    # Method - Update Table and View Names
    @staticmethod
    def update_static(tables: None, views: None) -> None:
        '''
        Update Table and View Names
        -
        Updates the `TABLE_NAMES` and `VIEW_NAMES` static attributes with
        the provided tables and views.

        Parameters
        -
        - tables : `TODO`
            - Collection of all tables in the database.
        - views : `TODO`
            - Collection of all views in the database.

        Returns
        -
        None
        '''

        raise NotImplementedError(
            f'Value_Type.update_static(tables = {tables}, views = {views}) ' \
            + 'not had the functionality defined.'
        )


# =============================================================================
# End of File
# =============================================================================
