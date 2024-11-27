# =============================================================================
# Database Model Creator - Generic Objects
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Generic Objects
-
Contains the generic objects that are implemented by the objects in the rest of
this package.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for custom errors
from .errors import (
    AbstractError, # abstract method error
)

# used for creating enumerators
from enum import (
    Enum, # regular enumerator
    EnumMeta,
    IntEnum, # enumerator for integers
)

# used for type-hinting
from typing import (
    Any, # any type
    List, # used for type-hinting lists
)


# =============================================================================
# Object to String Converter
# =============================================================================
def to_str(obj: Any, lvl: 'VerbosityLevel') -> str:
    '''
    Object to String Converter
    -
    Converts a single object to a single or multiple line string. Used by the
    `OBJ().__repr__`, `OBJ.__str__` and `OBJ.debug` methods.

    Parameters
    -
    - obj : `Any`
        - Object being converted to a string.
    - lvl : `VerbosityLevel`
        - Verbosity level with which to output the data.

    Returns
    -
    - `str`
        - String representation of the given object.
    '''

    # initialize variables
    output: str = '' # string being produced

    # identify datatype
    if obj is None: # none type
        output = str(obj)
    elif isinstance(obj, type): # object type
        output = obj.__name__
    elif isinstance(obj, int): # integer
        output = str(obj)
    elif isinstance(obj, float): # float
        output = str(obj)
    elif isinstance(obj, complex): # complex number
        output = str(obj)
    elif isinstance(obj, str): # string
        if lvl == VerbosityLevel.SHORT: output = f'"{obj}"'
        elif lvl in [VerbosityLevel.LONG, VerbosityLevel.ALL]:
            output = f'"\n\t\t' + obj.replace('\n', '\n\t\t') + '\n\t"'
    elif isinstance(obj, bool): # boolean
        output = str(obj)
    elif isinstance(obj, dict): # dictionary
        if lvl == VerbosityLevel.SHORT: output = str(obj)
        elif lvl in [VerbosityLevel.LONG, VerbosityLevel.ALL]:
            output = (
                'dict(\n\t\t' \
                + ',\n\t\t'.join(
                    (
                        f'#{i} {key}: ' \
                        + (
                            to_str(
                                val,
                                VerbosityLevel(lvl - 1)
                            ).replace('\n', '\n\t')
                        )
                    )
                    for i, (key, val) in enumerate(obj.items())
                )
                + '\n\t}'
            )
    elif isinstance(obj, ( # sequence data types
            bytes,
            bytearray,
            memoryview,
            list,
            tuple,
            set,
            frozenset,
    )):
        if lvl == VerbosityLevel.SHORT:
            output = ','.join([str(x) for x in obj])
        elif lvl == VerbosityLevel.LONG:
            output = (
                f'{obj.__class__.__name__}(\n\t\t' \
                + ',\n\t\t'.join([
                    f'{i}: {str(x)}'
                    for i, x in enumerate(list(obj)[:20])
                ])
            )
            if len(obj) > 20: output += f',\n\t\t... + {len(obj) - 20} items'
            output += '\n\t)'
        else:
            output = (
                f'{obj.__class__.__name__}(\n\t\t' \
                + ',\n\t\t'.join([
                    (
                        f'#{i}: ' \
                        + to_str(
                            x,
                            VerbosityLevel.LONG
                        ).replace('\n', '\n\t')
                    )
                    for i, x in enumerate(obj)
                ]) \
                + '\n\t)'
            )
    elif isinstance(obj, range): # range object
        output = str(obj)
    elif callable(obj): # function
        output = obj.__name__
    elif isinstance(obj, OBJ): # custom object
        if lvl in [VerbosityLevel.SHORT, VerbosityLevel.LONG]:
            output = str(obj)
        else: output = repr(obj)
    elif isinstance(obj, Enum): # enumeration object
        if lvl == VerbosityLevel.SHORT:
            output = str(obj)
        else: output = repr(obj)
    else: # unknown object type
        if lvl in [VerbosityLevel.SHORT, VerbosityLevel.LONG]:
            output = f'Unknown Object Type: {obj}'
        else: output = f'Unknown Object Type: {obj!r}'

    # single-line output additional editing
    if lvl == VerbosityLevel.SHORT:
        # prevent multiple lines
        output = output.replace('\n', '\\n')

        # cap length at 100 characters
        if (len(output) > 100):
            output = f'{output[:97]}... + {len(output) - 97}'

    return output


# =============================================================================
# Generic Enum
# =============================================================================
class EnumParentMeta(EnumMeta):
    '''
    Generic Enum Meta
    -
    Contains additional functionality that other `Enum` classes require.
    '''

    # ===============
    # Contains (`in`)
    def __contains__(cls, item: object) -> bool:
        try: cls(item)
        except ValueError: return False
        return True
class EnumParent(Enum, metaclass=EnumParentMeta):
    pass


# =============================================================================
# File Types Enum
# =============================================================================
class FileType(EnumParent):
    '''
    File Types Enum
    -
    Collection of all valid file types that the database model can be read
    from.
    '''

    JSON = 'json'
    ''' JSON Format (.json). '''

    XML = 'xml'
    ''' XML Format (.xml). '''

    YAML = 'yaml'
    ''' YAML Format (.yaml). '''


# =============================================================================
# Method Types Enum
# =============================================================================
class MethodType(EnumParent):
    '''
    Method Types Enum
    -
    Collection of all valid method types (e.g. "instance", "static") that can
    be used when creating ORM object methods.
    '''

    CLASS = 'class'
    ''' Class Method. This type allows the method to access the class it is
        defined in. '''

    INSTANCE = 'instance'
    ''' Instance Method. This type allows the method to access a particular
        instance of the class it is defined in. '''

    STATIC = 'static'
    ''' Static Method. This method has no special accessors, and does not
        depend on the class it is defined in, nor any particular instance of
        that class. '''


# =============================================================================
# Base Object Definition
# =============================================================================
class OBJ(object):
    '''
    Base Object Definition
    -
    Base object definition for all other objects in the package. Contains
    basic methods used for debugging purposes.

    Fields
    -
    None

    Methods
    -
    - __repr__() : `str`
    - __str__() : `str`
    - Debug(indent : `int` = 0) : `str`
    - Duplicate() : `OBJ` << abstract >>
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << abstract >>
    '''

    # ==============================================
    # Method - Official String Representation Method
    def __repr__(self) -> str:
        '''
        Official String Representation
        -
        Called by the `repr` built-in function, this computes the "official"
        string representation of the current object.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Official string representation of the current object.
        '''

        # initialize data
        data_labels: List[str] # collection of object data labels
        data_strings: List[str] # collection of object data labels + values
        label: str # item from `data_labels`
        value: str # item to add to `data_strings`

        # get object data
        data_labels = self.GetData(VerbosityLevel.LONG)

        # construct data strings for each data point
        data_strings = []
        for label in data_labels:
            value = ''
            try:
                value = (
                    f'{label} = ' \
                    + (
                        to_str(
                            getattr(self, label),
                            VerbosityLevel.LONG
                        ).replace('\n', '\n\t')
                    )
                )
            except Exception as e:
                value = (f'{label} = {e}')
            data_strings.append(value)

        # create overall data string
        return (
            f'<{self.__class__.__name__}\n\t' \
            + ',\n\t'.join(data_strings) \
            + f'\n/{self.__class__.__name__}>'
        )

    # ==============================================
    # Method - Informal String Representation Method
    def __str__(self) -> str:
        '''
        Informal String Representation
        -
        Called by the `str`, `__format__`, and `print` built-in functions,
        this computes the "informal" or nicely printable string
        representation of the current object.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Informal string representation of the current object.
        '''

        # initialize data
        data_labels: List[str] # collection of object data labels
        data_strings: List[str] # collection of object data labels + values
        label: str # item from `data_labels`
        value: str # item to add to `data_strings`

        # get object data
        data_labels = self.GetData(VerbosityLevel.SHORT)

        # construct data strings for each data point
        data_strings = []
        for label in data_labels:
            value = ''
            try:
                value = (
                    f'{label} = ' \
                    + to_str(getattr(self, label), VerbosityLevel.SHORT)
                )
            except Exception as e:
                value = (f'{label} = {e}')
            data_strings.append(value)

        # create overall data string
        return (
            f'<{self.__class__.__name__} :: ' \
            + ', '.join(data_strings) \
            + f' />'
        )

    # =====================
    # Method - Debug Object
    def Debug(self, indent: int = 0) -> str:
        '''
        Debug Object
        -
        Creates a multi-line string representation of the current object
        instance, including all attribute / property values (using the
        `VerbosityLevel.ALL` level).

        Parameters
        -
        - indent : `int`
            - Specifies the amount of additional indentation to use in the
                string. Defaults to `0`.

        Returns
        -
        - `str`
            - Multi-line debug string representation of the current object.
        '''

        # initialize data
        data_labels: List[str] # collection of object data labels
        data_strings: List[str] # collection of object data labels + values
        label: str # item from `data_labels`
        t: str = '\t' * indent # additional indentation
        value: str # item to add to `data_strings`

        # get object data
        data_labels = self.GetData(VerbosityLevel.ALL)

        # construct data strings for each data point
        data_strings = []
        for label in data_labels:
            value = ''
            try:
                value = (
                    f'{label} = ' \
                    + (
                        to_str(
                            getattr(self, label),
                            VerbosityLevel.ALL
                        ).replace('\n', f'\n\t{t}')
                    )
                )
            except Exception as e:
                value = (f'{label} = {e}')
            data_strings.append(value)

        # create overall data string
        return (
            f'{t}<{self.__class__.__name__}\n\t' \
            + f',\n\t{t}'.join(data_strings) \
            + f'\n{t}/{self.__class__.__name__}>'
        )

    # =========================
    # Method - Duplicate Object
    def Duplicate(self) -> 'OBJ':
        '''
        Duplicate Object
        -
        Creates a duplicate of the current object, however with entirely new
        references to all attribute and property values, meaning that the
        duplicate created is entirely independent from the original.

        Parameters
        -
        None

        Returns
        -
        - `OBJ`
            - Duplicate of the current object.
        '''

        # this method should be overridden in subclasses
        raise AbstractError(
            f'OBJ().Duplicate() has not been defined in {self.__class__}'
        )

    # =================
    # Method - Get Data
    def GetData(self, lvl: 'VerbosityLevel') -> List[str]:
        '''
        Get Data
        -
        Returns a list of attribute / property values that the object should
        contain, which can be used by debugging functions to produce a pretty
        output of the current object instance.

        Parameters
        -
        - lvl : `VerbosityLevel`
            - The level of verbosity.

        Returns
        -
        - `List<str>`
            - A collection of the names of all attributes and properties that
                should be retrieved from the current object instance.
        '''

        # This method should be overridden in subclasses
        raise AbstractError(
            f'OBJ().GetData(lvl = {lvl}) has not been defined in ' \
            + f'{self.__class__}'
        )


# =============================================================================
# Verbosity Levels Enum
# =============================================================================
class VerbosityLevel(IntEnum):
    '''
    Verbosity Levels Enum
    -
    Contains the different verbosity levels that can be used to get
    data from the current object for debugging and/or logging
    purposes.
    '''

    SHORT = 0
    ''' Shortest verbosity level, get only a couple of data points. Used
        for single-line string representations of the current object. '''
    LONG = 1
    ''' Long verbosity level, get most data points. Used for multi-line
        string representations of the current object. '''
    ALL = 2
    ''' Very detailed verbosity level, get all data points. Used for
        debug strings that include the all instance data in the object in a
        very lone multi-line string. '''


# =============================================================================
# End of File
# =============================================================================
