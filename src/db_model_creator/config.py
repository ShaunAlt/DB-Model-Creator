# =============================================================================
# Database Model Creator - Configuration
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Configuration
-
Contains all of the key definitions that are used across the rest of this
package.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for creating enumerators
from enum import IntEnum

# used for type-hinting
from typing import (
    Any, # any type
    List, # used for type-hinting lists
)


# =============================================================================
# Object to String Converter
# =============================================================================
def to_str(obj: Any, lvl: 'OBJ.Verbosity_Level') -> str:
    '''
    Object to String Converter
    -
    Converts a single object to a single or multiple line string. Used by the
    `OBJ().__repr__`, `OBJ.__str__` and `OBJ.debug` methods.

    Parameters
    -
    - obj : `Any`
        - Object being converted to a string.
    - lvl : `OBJ.Verbosity_Level`
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
        if lvl == OBJ.Verbosity_Level.SHORT: output = f'"{obj}"'
        elif lvl in [OBJ.Verbosity_Level.LONG, OBJ.Verbosity_Level.ALL]:
            output = f'"\n\t\t' + obj.replace('\n', '\n\t\t') + '\n\t"'
    elif isinstance(obj, bool): # boolean
        output = str(obj)
    elif isinstance(obj, dict): # dictionary
        if lvl == OBJ.Verbosity_Level.SHORT: output = str(obj)
        elif lvl in [OBJ.Verbosity_Level.LONG, OBJ.Verbosity_Level.ALL]:
            output = (
                'dict(\n\t\t' \
                + ',\n\t\t'.join(
                    (
                        f'#{i} {key}: ' \
                        + to_str(val, lvl - 1).replace('\n', '\n\t')
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
        if lvl == OBJ.Verbosity_Level.SHORT:
            output = ','.join([str(x) for x in obj])
        elif lvl == OBJ.Verbosity_Level.LONG:
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
                            OBJ.Verbosity_Level.LONG
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
        if lvl in [OBJ.Verbosity_Level.SHORT, OBJ.Verbosity_Level.LONG]:
            output = str(obj)
        else: output = repr(obj)
    else: # unknown object type
        if lvl in [OBJ.Verbosity_Level.SHORT, OBJ.Verbosity_Level.LONG]:
            output = f'Unknown Object Type: {obj}'
        else: output = f'Unknown Object Type: {obj!r}'

    # single-line output additional editing
    if lvl == OBJ.Verbosity_Level.SHORT:
        # prevent multiple lines
        output = output.replace('\n', '\\n')

        # cap length at 100 characters
        if (len(output) > 100):
            output = f'{output[:97]}... + {len(output) - 97}'

    return output


# =============================================================================
# Base Object Definition
# =============================================================================
class OBJ(object):
    '''
    Base Object Definition
    -
    Base object definition for all other objects in the package. Contains
    basic methods used for debugging purposes.

    Attributes
    -
    None

    Constants
    -
    - Verbosity_Level : `IntEnum`
        - Contains the different verbosity levels that can be used to get data
            from the current object for debugging and/or logging purposes.

    Methods
    -
    - __repr__() : `str`
        - Official String Representation Method.
        - Called by the `repr` built-in function, this computes the "official"
            string representation of the current object.
    - __str__() : `str`
        - Informal String Representation Method.
        - Called by the `str`, `__format__`, and `print` built-in functions,
            this computes the "informal" or nicely printable string
            representation of the current object.
    - _get_data(lvl) : `List[str]`
        - Instance Method.
        - Returns a list of attribute / property values that the object should
            contain, which can be used by debugging functions to produce a
            pretty output of the current object instance.
    - debug(indent=0) : `str`
        - Instance Method.
        - Creates a multi-line string representation of the current object
            instance, including all attribute / property values (using the
            `OBJ.Verbosity_Level.ALL` level).
    - duplicate() : `OBJ`
        - Instance Method.
        - Creates a duplicate of the current object, however with entirely new
            references to all attribute and property values, meaning that the
            duplicate created is entirely independent from the original.

    Properties
    -
    None
    '''

    # ===========================
    # Constant - Verbosity Levels
    class Verbosity_Level(IntEnum):
        ''' Contains the different verbosity levels that can be used to get
            data from the current object for debugging and/or logging
            purposes. '''

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
        data_labels = self._get_data(OBJ.Verbosity_Level.LONG)

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
                            OBJ.Verbosity_Level.LONG
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
        data_labels = self._get_data(OBJ.Verbosity_Level.SHORT)

        # construct data strings for each data point
        data_strings = []
        for label in data_labels:
            value = ''
            try:
                value = (
                    f'{label} = ' \
                    + to_str(getattr(self, label), OBJ.Verbosity_Level.SHORT)
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

    # =================
    # Method - Get Data
    def _get_data(self, lvl: 'OBJ.Verbosity_Level') -> List[str]:
        '''
        Get Data
        -
        Returns a list of attribute / property values that the object should
        contain, which can be used by debugging functions to produce a pretty
        output of the current object instance.

        Parameters
        -
        - lvl : `OBJ.Verbosity_Level`
            - The level of verbosity.

        Returns
        -
        - `list[str]`
            - A collection of the names of all attributes and properties that
                should be retrieved from the current object instance.
        '''

        # This method should be overridden in subclasses
        raise NotImplementedError(
            f'OBJ()._get_data(lvl = {lvl}) has not been defined in ' \
            + f'{self.__class__}'
        )

    # =====================
    # Method - Debug Object
    def debug(self, indent: int = 0) -> str:
        '''
        Debug Object
        -
        Creates a multi-line string representation of the current object
        instance, including all attribute / property values (using the
        `OBJ.Verbosity_Level.ALL` level).

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
        data_labels = self._get_data(OBJ.Verbosity_Level.ALL)

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
                            OBJ.Verbosity_Level.ALL
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
    def duplicate(self) -> 'OBJ':
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
        raise NotImplementedError(
            f'OBJ().duplicate() has not been defined in {self.__class__}'
        )


# =============================================================================
# End of File
# =============================================================================
