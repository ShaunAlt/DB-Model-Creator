# =============================================================================
# Database Model Creator - Testing File Reading - YAML
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Testing File Reading - YAML
-
Contains all of the objects that are used for testing the ability of this
package to read and process database models being read from a YAML file.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for reading file data
from io import BytesIO


# =============================================================================
# Main YAML Test
# =============================================================================
def test_yaml(file: BytesIO) -> None:
    '''
    Test YAML Read
    -
    Reads a YAML file, attempts to create a database model out of it, and then
    asserts that the database model created contains all of the correct data.

    This method is used to test that the package is able to successfully read a
    database model from a YAML file and convert it into a group of database
    model objects.

    Parameters
    -
    - file : `BytesIO`
        - The file to read.

    Returns
    -
    None
    '''

    raise NotImplementedError(f'test_yaml(file = {file}) has not been defined')


# =============================================================================
# End of File
# =============================================================================
