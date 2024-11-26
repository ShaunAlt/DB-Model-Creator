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
            and (self._params == other._params)
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
