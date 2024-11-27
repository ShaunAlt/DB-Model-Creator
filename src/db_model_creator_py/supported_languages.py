# =============================================================================
# Database Model Creator - Supported Languages
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Supported Languages
-
Contains the objects that contain the collections of languages supported by the
package.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for creating enumerators
from .generic_objects import (
    EnumParent, # parent enum class
)


# =============================================================================
# Supported Database Languages Enum
# =============================================================================
class LangDb(EnumParent):
    '''
    Supported Database Languages Enum
    -
    Collection of all valid database languages that are supported by the
    package.
    '''

    MSSQL = 'mssql'
    ''' Microsoft SQL Server. '''


# =============================================================================
# Supported ORM Languages Enum
# =============================================================================
class LangOrm(EnumParent):
    '''
    Supported ORM Languages Enum
    -
    Collection of all valid ORM languages that are supported by the package.
    '''

    PYTHON_SQLALCHEMY = 'python-sqlalchemy'
    ''' Python with SQLAlchemy. '''


# =============================================================================
# End of File
# =============================================================================
