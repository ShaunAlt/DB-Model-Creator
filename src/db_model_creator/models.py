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
    TYPES_PYTHON3, # DatabaseLang.PYTHON3 data types
)

# used for creating enumeration objects
from enum import Enum

# used for regular expressions
import regex as re

# used for type hinting
from typing import (
    List,
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
class Value_DefVal(Value):
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
        - Creates a new `Value_DefVal` object.
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
    - update_names(tables, views) : `None`
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
            data += ['_tablenames', '_viewnames']
        return data


# =============================================================================
# End of File
# =============================================================================
