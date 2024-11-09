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
from enum import Enum

# used for type-hinting
from typing import (
    List, # used for type-hinting lists
)


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
    - Verbosity_Level : `Enum`
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
    class Verbosity_Level(Enum):
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

        # TODO
        raise NotImplementedError('OBJ().__repr__() has not been defined')

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

        # TODO
        raise NotImplementedError('OBJ().__str__() has not been defined')

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

        # TODO
        raise NotImplementedError(
            f'OBJ().debug(indent = {indent}) has not been defined'
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
