# =============================================================================
# Database Model Creator - Types
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Types
-
Contains the objects used for defining the data types allowed in each language.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for creating enumeration objects
from enum import Enum


# =============================================================================
# Types Models
# =============================================================================

# =================
# Method Types Enum
class TYPES_METHOD(Enum):
    '''
    Collection of all valid method types (e.g. "instance", "static") that can
    be used when creating ORM object methods.
    '''

    # =================
    # Class Method Type
    CLASS = 'class'
    ''' Class Method. This type allows the method to access the class it is
        defined in. '''

    # ====================
    # Instance Method Type
    INSTANCE = 'instance'
    ''' Instance Method. This type allows the method to access a particular
        instance of the class it is defined in. '''

    # ==================
    # Static Method Type
    STATIC = 'static'
    ''' Static Method. This method has no special accessors, and does not
        depend on the class it is defined in, nor any particular instance of
        that class. '''
    
# ================
# MSSQL Types Enum
class TYPES_MSSQL(Enum):
    '''
    Collection of all valid types for the MSSQL database.
    
    Information: https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver16
    '''

    BIGINT = 'bigint'
    ''' 8-byte signed integer. '''

    BIT = 'bit'
    ''' Integer data type that can store `1`, `0`, or `NULL`. '''

    INT = 'int'
    ''' 4-byte signed integer. '''

    SMALLINT = 'smallint'
    ''' 2-byte signed integer. '''

    TINYINT = 'tinyint'
    ''' 1-byte unsigned integer. '''

# ==================
# Python3 Types Enum
class TYPES_PYTHON3(Enum):
    '''
    Collection of all valid built-in or importable Python types.

    Values that are a single string (e.g. `"None"`) are expected to be a
    built-in data type that does not require to be imported.

    Values that contain period delimiters are expected to be importable
    from the corresponding Python module (`"typing.List"` will import the
    `typing` module, and then use `typing.List` as the data type).
    '''

    # ============
    # Boolean Type
    BOOL = 'bool'
    ''' Python datatype used for boolean types. '''

    # ==========
    # Bytes Type
    BYTES = 'bytes'
    ''' Python datatype used for a collection of bytes. Immutable. '''

    # ===============
    # Byte Array Type
    BYTEARRAY = 'bytearray'
    ''' Python datatype used for a collection of bytes. Mutable. '''

    # =============
    # Callable Type
    CALLABLE = 'typing.Callable'
    ''' Python datatype used to represent a callable type (method). '''

    # ============
    # Complex Type
    COMPLEX = 'complex'
    ''' Python datatype used to represent a complex number type. '''

    # ===============
    # Dictionary Type
    DICT = 'typing.Dict'
    ''' Python datatype used to represent a dictionary. Mutable. '''

    # ==========
    # Float Type
    FLOAT = 'float'
    ''' Python datatype used to represent a floating point number type. '''

    # ===============
    # Frozen Set Type
    FROZENSET = 'typing.FrozenSet'
    ''' Python datatype used to represent a set of objects. Immutable. '''

    # ============
    # Integer Type
    INT = 'int'
    ''' Python datatype used for integer types. '''

    # =========
    # List Type
    LIST = 'typing.List'
    ''' Python datatype used for creating lists. '''

    MEMORYVIEW = 'memoryview'
    # =========
    # None Type
    NONE = 'None'
    ''' Python datatype used for nullable values. '''

    # =============
    # Optional Type
    OPTIONAL = 'typing.Optional'
    ''' Python datatype used for type-hinting a nullable type. '''

    # ==========
    # Range Type
    RANGE = 'range'
    ''' Python datatype used for type-hinting a range. '''

    # ========
    # Set Type
    SET = 'typing.Set'
    ''' Python datatype used to represent a set of objects. Mutable. '''

    # ===========
    # String Type
    STR = 'str'
    ''' Python datatype used to represent a string of characters. Mutable. '''

    # ==========
    # Tuple Type
    TUPLE = 'typing.Tuple'
    ''' Python datatype used to represent a tuple of objects. Immutable. '''

    # =========
    # Type Type
    TYPE = 'type'
    ''' Python datatype used to represent an object type (reference to the
        class instead of an instance). '''

    # ==========
    # Union Type
    UNION = 'typing.Union'
    ''' Python datatype used for type-hinting multiple types. '''


# =============================================================================
# End of File
# =============================================================================
