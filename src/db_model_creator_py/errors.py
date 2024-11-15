# =============================================================================
# Database Model Creator - Custom Errors
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Custom Errors
-
Contains definitions for all custom errors implemented in the project.
'''
# =============================================================================


# =============================================================================
# Abstract Method Error
# =============================================================================
class AbstractError(Exception):
    ''' Abstract Error. Used when an object defines an abstract function. '''


# =============================================================================
# Undefined Functionality Error
# =============================================================================
class UndefFuncError(Exception):
    ''' Undefined Functionality Error. Used when a section of code (e.g. an
        object method) has been defined but no functionality has been assigned
        to it. (Similar to a TODO notification). '''


# =============================================================================
# End of File
# =============================================================================
