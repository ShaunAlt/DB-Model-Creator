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
# File Type Error
# =============================================================================
class FileTypeError(Exception):
    ''' File Type Error. Used when an invalid file type was encountered. '''


# =============================================================================
# Invalid Database Language Error
# =============================================================================
class LangDbError(Exception):
    ''' Invalid Database Language Error. Used when an invalid database language
        is encountered. '''


# =============================================================================
# Invalid ORM Language Error
# =============================================================================
class LangOrmError(Exception):
    ''' Invalid ORM Language Error. Used when an invalid ORM language is
        encountered. '''


# =============================================================================
# Read Error
# =============================================================================
class ReadError(Exception):
    ''' File Read Error. Used when the database model file being read is
        invalid. '''


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
