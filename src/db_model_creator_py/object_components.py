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

# custom error definitions
from .errors import (
    AbstractError, # abstract method error
    UndefFuncError, # undefined functionality error
)

# generic objects
from .generic_objects import (
    MethodType, # method types
    OBJ, # base object model
    VerbosityLevel, # verbosity levels
)

# supported languagges
from .supported_languages import (
    LangOrm, # supported ORM languages
)

# used for type-hinting
from typing import (
    List, # list type-hint
    Optional, # nullable datatype
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
    - __eq__(other) << equality check >>
    - Duplicate() : `ObjComp` << override >>
    - FromDict(data) : `ORM` << class, abstract >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - LoadData(lang_orm : `LangOrm`) : `None` << static >>
    - ObjComp(...) << constructor >>
    - Write(comment : `bool`) : `str` << abstract >>
    '''

    # =============
    # Static Fields
    lang_orm: Optional[LangOrm] = None
    ''' ORM Language the object component will be created in. '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            (isinstance(other, self.__class__))
            and (self._name == other._name)
            and (self._type == other._type)
            and (self._desc == other._desc)
            and (self._default == other._default)
            and (self._title == other._title)
        )

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            desc: str,
            default: Optional[str] = None,
            title: Optional[str] = None
    ) -> None:
        '''
        Object Component Constructor
        -
        Creates a new `ObjComp` object.

        Parameters
        -
        - name : `str`
            - Name of the object component.
        - type_ : `str`
            - Return type of the object component.
        - desc : `str`
            - Description of the object component.
        - default : `str | None`
            - Default value of the object component, if required.
        - title : `str | None`
            - Comment title of the object component, if required.

        Returns
        -
        None
        '''

        # set fields
        self._default = CompValue_Default(default) if default else None
        ''' Default value of the object component, if required. '''
        self._desc = CompValue_Desc(desc)
        ''' Description of the object component. '''
        self._name = CompValue_Name(name)
        ''' Name of the object component. '''
        self._title = CompValue_Title(title) if title else None
        ''' Comment title of the object component, if required. '''
        self._type = CompValue_Type(type_)
        ''' Return type of the object component. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        ''' Whether or not all data in the component is valid. '''
        return all([
            self.valid_default,
            self.valid_desc,
            self.valid_name,
            self.valid_title,
            self.valid_type,
        ])

    # ================================
    # Property - Valid - Default Value
    @property
    def valid_default(self) -> bool:
        ''' Whether or not the default value of the component is valid. '''
        return (
            (self._default is None)
            or (self._default.Validate())
        )
    
    # ==============================
    # Property - Valid - Description
    @property
    def valid_desc(self) -> bool:
        ''' Whether or not the description of the component is valid. '''
        return self._desc.Validate()
    
    # =======================
    # Property - Valid - Name
    @property
    def valid_name(self) -> bool:
        ''' Whether or not the name of the component is valid. '''
        return self._name.Validate()
    
    # ================================
    # Property - Valid - Comment Title
    @property
    def valid_title(self) -> bool:
        ''' Whether or not the comment title of the component is valid. '''
        return (
            (self._title is None)
            or (self._title.Validate())
        )
    
    # ==============================
    # Property - Valid - Return Type
    @property
    def valid_type(self) -> bool:
        ''' Whether or not the return type of the component is valid. '''
        return self._type.Validate()
    
    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ObjComp':
        return ObjComp(
            name = self._name.data,
            type_ = self._type.data,
            desc = self._desc.data,
            default = self._default.data if self._default else None,
            title = self._title.data if self._title else None
        )
    
    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ObjComp':
        '''
        Create from Dictionary
        -
        Creates a new `ObjComp` object from a given dictionary.

        Parametes
        -
        - data : `dict`
            - Dictionary containing the data required to create the new
                `ObjComp` object.

        Returns
        -
        - `ObjComp`
            - New `ObjComp` object from the dictionary data.
        '''

        raise AbstractError(
            f'ObjComp.FromDict(data = {data}) not defined in {cls}'
        )

    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        if lvl == VerbosityLevel.SHORT:
            return ['lang_orm', 'valid']
        elif lvl == VerbosityLevel.LONG:
            return [
                '_default',
                '_desc',
                '_name',
                '_title',
                '_type',
                'lang_orm',
                'valid',
                'valid_default',
                'valid_desc',
                'valid_name',
                'valid_title',
                'valid_type',
            ]
        else:
            return [
                '_default',
                '_desc',
                '_name',
                '_title',
                '_type',
                'lang_orm',
                'valid',
                'valid_default',
                'valid_desc',
                'valid_name',
                'valid_title',
                'valid_type',
            ]

    # =========================
    # Method - Load Static Data
    @staticmethod
    def LoadData(lang_orm: LangOrm) -> None:
        '''
        Load Static Data
        -
        Loads the static data for all object components.

        Parameters
        -
        - lang_orm : `LangOrm`
            - ORM language the object component will be created in.

        Returns
        -
        None
        '''

        # set orm language
        ObjComp.lang_orm = lang_orm

    # ===================
    # Method - Write Data
    def Write(self, comment: bool) -> str:
        '''
        Write Data
        -
        Writes the source code for the current object component in the
        required ORM language.

        Parameters
        -
        - comment : `bool`
            - Whether to write the comment for the object component, or the
                actual code.

        Returns
        -
        - `str`
            - String containing the object component formatted for the ORM
                language.
        '''

        raise AbstractError(
            f'ObjComp().Write(comment = {comment}) not defined in ' \
            + f'{self.__class__}'
        )


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

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            desc: str,
            title: str,
            default: Optional[str] = None
    ) -> None:
        '''
        Object Constant Constructor
        -
        Creates a new `ObjComp_Constant` object.

        Parameters
        -
        - name : `str`
            - Name of the object constant.
        - type_ : `str`
            - Return type of the object constant.
        - desc : `str`
            - Description of the object constant.
        - title : `str`
            - Comment title of the object constant.
        - default : `str | None`
            - Default value of the object constant, if required.

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            type_ = type_,
            desc = desc,
            default = default,
            title = title
        )

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ObjComp_Constant':
        return ObjComp_Constant(
            name = self._name.data,
            type_ = self._type.data,
            desc = self._desc.data,
            title = self._title.data if self._title else '',
            default = self._default.data if self._default else None
        )
    
    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ObjComp_Constant':
        # get the name of the constant
        _name: object = data.get('name', None)
        if _name is None: # validate name existence
            raise ValueError('Failed to read Constant Name (`name`)')
        if not isinstance(_name, str): # validate name type
            raise TypeError(
                'Constant Name (`name`) expected a `str` type, got ' \
                + f'{type(_name)}'
            )
        if _name == '': # validate name data
            raise ValueError('Constant Name (`name`) must not be empty')
        
        # get the type of the constant
        _type: object = data.get('type_', None)
        if _type is None: # validate type existence
            raise ValueError('Failed to read Constant Data Type (`type_`)')
        if not isinstance(_type, str): # validate type type
            raise TypeError(
                'Constant Data Type (`type_`) expected a `str` type, got ' \
                + f'{type(_type)}'
            )
        if _type == '': # validate type data
            raise ValueError('Constant Data Type (`type_`) must not be empty')
        
        # get the desc of the constant
        _desc: object = data.get('desc', None)
        if _desc is None: # validate description existence
            raise ValueError('Failed to read Constant Description (`desc`)')
        if not isinstance(_desc, str): # validate description type
            raise TypeError(
                'Constant Description (`desc`) expected a `str` type, got ' \
                + f'{type(_desc)}'
            )
        if _desc == '': # validate description data
            raise ValueError('Constant Description (`desc`) must not be empty')
        
        # get the title of the constant
        _title: object = data.get('title', None)
        if _title is None: # validate title existence
            raise ValueError('Failed to read Constant Title (`title`)')
        if not isinstance(_title, str): # validate title type
            raise TypeError(
                'Constant Title (`title`) expected a `str` type, got ' \
                + f'{type(_title)}'
            )
        if _title == '': # validate title data
            raise ValueError('Constant Title (`title`) must not be empty')
        
        # get the default value of the constant
        _default: object = data.get('default', '')
        if not isinstance(_default, str): # validate default value type
            raise TypeError(
                'Constant Default Value (`default`) expected a `str` type, ' \
                + f'got {type(_default)}'
            )
        
        return cls(
            name = _name,
            type_ = _type,
            desc = _desc,
            title = _title,
            default = _default
        )

    # ===================
    # Method - Write Data
    def Write(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ObjComp_Constant.Write(comment = {comment}) not defined'
        )


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
    - _flag_constructor : `bool`
    - _method_type : `MethodType`
    - _params : `List<ObjComp_MethodParam>`
    - valid : `bool` << override, readonly >>
    - valid_params : `bool` << readonly >>

    Methods
    -
    - __eq__(other) << equality check >>
    - Duplicate() : `ObjComp_Method` << override >>
    - ObjComp_Method(...) << constructor >>
    - Write(comment : `bool`) : `str` << override >>
    '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            super().__eq__(other)
            and (isinstance(other, self.__class__))
            and (self._flag_constructor == other._flag_constructor)
            and (self._method_type == other._method_type)
            and (len(self._params) == len(other._params))
            and (all([param in other._params for param in self._params]))
        )

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            desc: str,
            title: str,
            methodtype: MethodType,
            params: List['ObjComp_MethodParam'],
            default: Optional[str] = None,
            flag_constructor: bool = False
    ) -> None:
        '''
        Object Property Constructor
        -
        Creates a new `ObjComp_Property` object.

        Parameters
        -
        - name : `str`
            - Name of the object property.
        - type_ : `str`
            - Return type of the object property.
        - desc : `str`
            - Description of the object property.
        - title : `str`
            - Comment title of the object property.
        - default : `str | None`
            - Default value of the object property, if required.
        - flag_constructor : `bool`
            - Whether or not the method is an object constructor method (e.g.
                `__init__`).

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            type_ = type_,
            desc = desc,
            default = default,
            title = title
        )

        # set fields
        self._flag_constructor = flag_constructor
        ''' Whether or not the method is an object constructor method (e.g.
            `__init__`). '''
        self._method_type = methodtype
        ''' Type of method this object represents. '''
        self._params = params
        ''' Collection of parameters for the current method. '''

    # ================
    # Property - Valid
    @property
    def valid(self) -> bool:
        return (
            super().valid
            and all([
                self.valid_params,
            ])
        )

    # ====================================
    # Property - Valid - Method Parameters
    @property
    def valid_params(self) -> bool:
        ''' Whether or not the method parameters are valid. '''
        return all([param.valid for param in self._params])

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ObjComp_Method':
        return ObjComp_Method(
            name = self._name.data,
            type_ = self._type.data,
            desc = self._desc.data,
            title = self._title.data if self._title else '',
            methodtype = self._method_type,
            params = [param.Duplicate() for param in self._params],
            default = self._default.data if self._default else None,
            flag_constructor = self._flag_constructor
        )

    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ObjComp_Method':
        # get the name of the method
        _name: object = data.get('name', None)
        if _name is None: # validate name existence
            raise ValueError('Failed to read Method Name (`name`)')
        if not isinstance(_name, str): # validate name type
            raise TypeError(
                'Method Name (`name`) expected a `str` type, got ' \
                + f'{type(_name)}'
            )
        if _name == '': # validate name data
            raise ValueError('Method Name (`name`) must not be empty')
        
        # get the type of the method
        _type: object = data.get('type_', None)
        if _type is None: # validate type existence
            raise ValueError('Failed to read Method Data Type (`type_`)')
        if not isinstance(_type, str): # validate type type
            raise TypeError(
                'Method Data Type (`type_`) expected a `str` type, got ' \
                + f'{type(_type)}'
            )
        if _type == '': # validate type data
            raise ValueError('Method Data Type (`type_`) must not be empty')
        
        # get the desc of the method
        _desc: object = data.get('desc', None)
        if _desc is None: # validate description existence
            raise ValueError('Failed to read Method Description (`desc`)')
        if not isinstance(_desc, str): # validate description type
            raise TypeError(
                'Method Description (`desc`) expected a `str` type, got ' \
                + f'{type(_desc)}'
            )
        if _desc == '': # validate description data
            raise ValueError('Method Description (`desc`) must not be empty')
        
        # get the title of the method
        _title: object = data.get('title', None)
        if _title is None: # validate title existence
            raise ValueError('Failed to read Method Title (`title`)')
        if not isinstance(_title, str): # validate title type
            raise TypeError(
                'Method Title (`title`) expected a `str` type, got ' \
                + f'{type(_title)}'
            )
        if _title == '': # validate title data
            raise ValueError('Method Title (`title`) must not be empty')
        
        # get the method type of the method
        _methodtype: object = data.get('methodtype', 'instance')
        if not isinstance(_methodtype, str): # validate method type type
            raise TypeError(
                'Method Type (`methodtype`) expected a `str` type, got ' \
                + f'{type(_methodtype)}'
            )
        if _methodtype not in MethodType: # validate method type data
            raise ValueError(
                'Invalid Method Type (`methodtype`) - expected on of ' \
                + f'{[mt.value for mt in MethodType]!r}, got `{_methodtype!r}`'
            )
        _methodtype = MethodType(_methodtype)
        
        # get the parameters of the method
        _params: object = data.get('params', None)
        if _params is None: # validate parameters existence
            raise ValueError('Failed to read Method Parameters (`params`)')
        if not isinstance(_params, list): # validate parameters type
            raise TypeError(
                'Method Parameters (`params`) expected a `list` type, got ' \
                + f'{type(_params)}'
            )
        params: list[ObjComp_MethodParam] = []
        for i, param in enumerate(params):
            # validate parameter data is a dict
            if not isinstance(param, dict):
                raise TypeError(
                    f'Method Parameter at index {i} expected a `dict` type, ' \
                    + f'got {type(param)}'
                )
            
            # create parameter
            try:
                params.append(ObjComp_MethodParam.FromDict(param))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create parameter at index {i}: {e!r}'
                )
        
        # get the default value of the method
        _default: object = data.get('default', '')
        if not isinstance(_default, str): # validate default value type
            raise TypeError(
                'Method Default Value (`default`) expected a `str` type, ' \
                + f'got {type(_default)}'
            )
        
        # get the constructor flag value of the method
        _flag_constructor: object = data.get('flag_constructor', 'False')
        if _flag_constructor not in ['True', 'False']: # validate flag value
            raise ValueError(
                'Method Flag-Constructor Value (`flag_constructor`) expected' \
                + 'a `str` value of either "True" or "False", got ' \
                + f'{_flag_constructor!r}'
            )
        _flag_constructor = _flag_constructor == 'True'
        
        return cls(
            name = _name,
            type_ = _type,
            desc = _desc,
            title = _title,
            methodtype = _methodtype,
            params = params,
            default = _default,
            flag_constructor = _flag_constructor
        )

    # ===================
    # Method - Write Data
    def Write(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ObjComp_Method.Write(comment = {comment}) not defined'
        )


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

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            desc: str,
            default: Optional[str] = None
    ) -> None:
        '''
        Object Method Parameter Constructor
        -
        Creates a new `ObjComp_MethodParam` object.

        Parameters
        -
        - name : `str`
            - Name of the method parameter.
        - type_ : `str`
            - Return type of the method parameter.
        - desc : `str`
            - Description of the method parameter.
        - default : `str | None`
            - Default value of the method parameter, if required.

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            type_ = type_,
            desc = desc,
            default = default,
            title = None
        )

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ObjComp_MethodParam':
        return ObjComp_MethodParam(
            name = self._name.data,
            type_ = self._type.data,
            desc = self._desc.data,
            default = self._default.data if self._default else None
        )

    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ObjComp_MethodParam':
        # get the name of the method parameter
        _name: object = data.get('name', None)
        if _name is None: # validate name existence
            raise ValueError('Failed to read Method Parameter Name (`name`)')
        if not isinstance(_name, str): # validate name type
            raise TypeError(
                'Method Parameter Name (`name`) expected a `str` type, got ' \
                + f'{type(_name)}'
            )
        if _name == '': # validate name data
            raise ValueError(
                'Method Parameter Name (`name`) must not be empty'
            )
        
        # get the type of the method parameter
        _type: object = data.get('type_', None)
        if _type is None: # validate type existence
            raise ValueError(
                'Failed to read Method Parameter Data Type (`type_`)'
            )
        if not isinstance(_type, str): # validate type type
            raise TypeError(
                'Method Parameter Data Type (`type_`) expected a `str` type,' \
                + f' got {type(_type)}'
            )
        if _type == '': # validate type data
            raise ValueError(
                'Method Parameter Data Type (`type_`) must not be empty'
            )
        
        # get the desc of the method parameter
        _desc: object = data.get('desc', None)
        if _desc is None: # validate description existence
            raise ValueError(
                'Failed to read Method Parameter Description (`desc`)'
            )
        if not isinstance(_desc, str): # validate description type
            raise TypeError(
                'Method Parameter Description (`desc`) expected a `str` ' \
                + f'type, got {type(_desc)}'
            )
        if _desc == '': # validate description data
            raise ValueError(
                'Method Parameter Description (`desc`) must not be empty'
            )
        
        # get the default value of the method parameter
        _default: object = data.get('default', '')
        if not isinstance(_default, str): # validate default value type
            raise TypeError(
                'Method Parameter Default Value (`default`) expected a `str`' \
                + f' type, got {type(_default)}'
            )
        
        return cls(
            name = _name,
            type_ = _type,
            desc = _desc,
            default = _default
        )

    # ===================
    # Method - Write Data
    def Write(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ObjComp_MethodParam.Write(comment = {comment}) not defined'
        )


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
    - _readonly : `bool`

    Methods
    -
    - Duplicate() : `ObjComp_Property` << override >>
    - ObjComp_Property(...) << constructor >>
    - Write(comment : `bool`) : `str` << override >>
    '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        return (
            super().__eq__(other)
            and (isinstance(other, self.__class__))
            and (self._readonly == other._readonly)
        )

    # ====================
    # Method - Constructor
    def __init__(
            self,
            name: str,
            type_: str,
            desc: str,
            title: str,
            default: Optional[str] = None,
            readonly: bool = False
    ) -> None:
        '''
        Object Property Constructor
        -
        Creates a new `ObjComp_Property` object.

        Parameters
        -
        - name : `str`
            - Name of the object property.
        - type_ : `str`
            - Return type of the object property.
        - desc : `str`
            - Description of the object property.
        - title : `str`
            - Comment title of the object property.
        - default : `str | None`
            - Default value of the object property, if required.
        - readonly : `bool`
            - Whether or not the object property is read-only.

        Returns
        -
        None
        '''

        super().__init__(
            name = name,
            type_ = type_,
            desc = desc,
            default = default,
            title = title
        )

        # set fields
        self._readonly = readonly
        ''' Whether or not the object property is read-only. '''

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'ObjComp_Property':
        return ObjComp_Property(
            name = self._name.data,
            type_ = self._type.data,
            desc = self._desc.data,
            title = self._title.data if self._title else '',
            default = self._default.data if self._default else None,
            readonly = self._readonly
        )

    # ===============================
    # Method - Create from Dictionary
    @classmethod
    def FromDict(cls, data: dict) -> 'ObjComp_Property':
        # get the name of the property
        _name: object = data.get('name', None)
        if _name is None: # validate name existence
            raise ValueError('Failed to read Property Name (`name`)')
        if not isinstance(_name, str): # validate name type
            raise TypeError(
                'Property Name (`name`) expected a `str` type, got ' \
                + f'{type(_name)}'
            )
        if _name == '': # validate name data
            raise ValueError('Property Name (`name`) must not be empty')
        
        # get the type of the property
        _type: object = data.get('type_', None)
        if _type is None: # validate type existence
            raise ValueError('Failed to read Property Data Type (`type_`)')
        if not isinstance(_type, str): # validate type type
            raise TypeError(
                'Property Data Type (`type_`) expected a `str` type, got ' \
                + f'{type(_type)}'
            )
        if _type == '': # validate type data
            raise ValueError('Property Data Type (`type_`) must not be empty')
        
        # get the desc of the property
        _desc: object = data.get('desc', None)
        if _desc is None: # validate description existence
            raise ValueError('Failed to read Property Description (`desc`)')
        if not isinstance(_desc, str): # validate description type
            raise TypeError(
                'Property Description (`desc`) expected a `str` type, got ' \
                + f'{type(_desc)}'
            )
        if _desc == '': # validate description data
            raise ValueError('Property Description (`desc`) must not be empty')
        
        # get the title of the property
        _title: object = data.get('title', None)
        if _title is None: # validate title existence
            raise ValueError('Failed to read Property Title (`title`)')
        if not isinstance(_title, str): # validate title type
            raise TypeError(
                'Property Title (`title`) expected a `str` type, got ' \
                + f'{type(_title)}'
            )
        if _title == '': # validate title data
            raise ValueError('Property Title (`title`) must not be empty')
        
        # get the default value of the property
        _default: object = data.get('default', '')
        if not isinstance(_default, str): # validate default value type
            raise TypeError(
                'Property Default Value (`default`) expected a `str` type, ' \
                + f'got {type(_default)}'
            )
        
        # get the readonly status of the property
        _readonly: object = data.get('readonly', 'False')
        if _readonly not in ['True', 'False']: # validate readonly value
            raise ValueError(
                'Property Read-Only Status (`readonly`) expected a `str` ' \
                + f'value of either "True" or "False", got {_readonly!r}'
            )
        _readonly = _readonly == 'True'
        
        return cls(
            name = _name,
            type_ = _type,
            desc = _desc,
            title = _title,
            default = _default,
            readonly = _readonly
        )

    # ===================
    # Method - Write Data
    def Write(self, comment: bool) -> str:
        raise UndefFuncError(
            f'ObjComp_Property.Write(comment = {comment}) not defined'
        )


# =============================================================================
# Back-Reference Import
# =============================================================================

# component values
from .component_values import (
    CompValue_Default, # default component value
    CompValue_Desc, # component description
    CompValue_Name, # component name
    CompValue_Title, # component comment title
    CompValue_Type, # component return type
)


# =============================================================================
# End of File
# =============================================================================
