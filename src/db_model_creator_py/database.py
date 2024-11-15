# =============================================================================
# Database Model Creator - Database Model
# Created by: Shaun Altmann
# =============================================================================
'''
Databsase Model Creator - Database Model
-
Contains the key database model that includes all of the information for a
given database.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# custom errors
from .errors import (
    FileTypeError, # file type error
    LangDbError, # invalid database language error
    LangOrmError, # invalid orm language error
    UndefFuncError, # undefined functionality error
)

# generic objects
from .generic_objects import (
    FileType, # supported file types
    OBJ, # base object model
    VerbosityLevel, # verbosity levels
)

# orm objects
from .orm_objects import (
    ORM_Table, # orm table
    ORM_View, # orm view
)

# supported languagges
from .supported_languages import (
    LangDb, # supported database languages
    LangOrm, # supported ORM languages
)

# used for type hinting
from typing import (
    List, # list data type
    Optional, # nullable data type
)


# =============================================================================
# Database Model
# =============================================================================
class Database(OBJ):
    '''
    Database Model
    -
    Contains all of the information for an individual database.

    Fields
    -
    - _file_name : `str`
    - _file_type : `str`
    - _lang_db : `LangDb | None`
    - _lang_orm : `LangOrm | None`
    - _prefix_orm_table : `str`
    - _prefix_orm_view : `str`
    - _save_dir_db : `str`
    - _save_dir_orm : `str`
    - _tables : `List<ORM_Table>`
    - _views : `List<ORM_View>`

    Methods
    -
    - Database(...) << constructor >>
    - Read()
    - Read_JSON()
    - Read_XML()
    - Read_YAML()
    - Validate()
    - Write()
    - Write_DB_MSSQL()
    - Write_ORM_PYTHON()
    '''

    # ====================
    # Method - Constructor
    def __init__(
            self,
            file_name: str,
            prefix_orm_table: str = 'DB_',
            prefix_orm_view: str = 'VW_',
            save_dir_db: str = 'output/database/',
            save_dir_orm: str = 'output/orm/'
    ) -> None:
        '''
        Database Model Constructor
        -
        Creates a new `Database` object.

        Parameters
        -
        - file_name : `str`
            - Name + Directory of the file containing the database model.
        - prefix_orm_table : `str`
            - String to prepend to the start of each object definition in the
                ORM. (e.g. if a table is called "Users", the ORM definition
                will be called "DB_Users" if the prefix is "DB_").
        - prefix_orm_view : `str`
            - String to prepent to the start of each object definition in the
                ORM. (e.g. if a view is called "Users", the ORM definition
                will be called "VW_Users" if the prefix is "VW_").
        - save_dir_db : `str`
            - Directory to save all of the files for the database.
        - save_dir_orm : `str`
            - Directory to save all of the files for the ORM.

        Returns
        -
        None
        '''

        # set fields
        self._file_name = file_name
        ''' Name + Directory of the file containing the database model. '''
        self._file_type: FileType
        ''' Filetype of the file containing the database model. '''
        self._lang_db: Optional[LangDb] = None
        ''' Language to write the database in (e.g. MSSQL). '''
        self._lang_orm: Optional[LangOrm] = None
        ''' Language to write the ORM in (e.g. Python-SQLAlchemy). '''
        self._prefix_orm_table = prefix_orm_table
        ''' String to prepend to the start of each object definition in the
            ORM. (e.g. if a table is called "Users", then the ORM definition
            will be called "DB_Users" if the prefix is "DB_"). '''
        self._prefix_orm_view = prefix_orm_view
        ''' String to prepend to the start of each object definition in the
            ORM. (e.g. if a view is called "Users", then the ORM definition
            will be called "VW_Users" if the prefix is "VW_"). '''
        self._save_dir_db = save_dir_db
        ''' Directory to save all of the files for the database. '''
        self._save_dir_orm = save_dir_orm
        ''' Directory to save all of the files for the ORM. '''
        self._tables: List[ORM_Table] = []
        ''' Collection of all tables in the database. '''
        self._views: List[ORM_View] = []
        ''' Collection of all views in the database. '''

        # identify the file type of the database model file
        for _filetype in FileType:
            if file_name.split('.')[-1] == _filetype.value:
                self._file_type = _filetype
                break
        else:
            raise FileTypeError(
                f'Database(file_name = {file_name}, ...) does not have a ' \
                + f'valid extension supported by {FileType}'
            )

    # ========================
    # Read Database Model File
    def Read(self) -> None:
        '''
        Read Database Model File
        -
        Reads the database model from the provided file, and creates the
        database model objects.

        Parameters
        -
        None

        Returns
        -
        None
        '''

        # run required file read
        if self._file_type == FileType.JSON:
            self.Read_JSON()
        elif self._file_type == FileType.XML:
            self.Read_XML()
        elif self._file_type == FileType.YAML:
            self.Read_YAML()
        else:
            raise FileTypeError(
                'Database().Read() failed to find read function for ' \
                + f'{self._file_type}'
            )

    # ===============================
    # Read Database Model File - JSON
    def Read_JSON(self) -> None:
        '''
        Read Database Model File - JSON
        -
        Reads the database model from the provided JSON file, and creates the
        database model objects.

        Parameters
        -
        None

        Returns
        -
        None
        '''

        # validate the file type
        if self._file_type != FileType.JSON:
            raise FileTypeError(
                'Database().Read_JSON() was called but `self._file_type = ' \
                + f'{self._file_type!r}`'
            )

        raise UndefFuncError('Database().Read_JSON() not defined')

    # ==============================
    # Read Database Model File - XML
    def Read_XML(self) -> None:
        '''
        Read Database Model File - XML
        -
        Reads the database model from the provided XML file, and creates the
        database model objects.

        Parameters
        -
        None

        Returns
        -
        None
        '''

        # validate the file type
        if self._file_type != FileType.XML:
            raise FileTypeError(
                'Database().Read_XML() was called but `self._file_type = ' \
                + f'{self._file_type!r}`'
            )

        raise UndefFuncError('Database().Read_XML() not defined')

    # ===============================
    # Read Database Model File - YAML
    def Read_YAML(self) -> None:
        '''
        Read Database Model File - YAML
        -
        Reads the database model from the provided YAML file, and creates the
        database model objects.

        Parameters
        -
        None

        Returns
        -
        None
        '''

        # validate the file type
        if self._file_type != FileType.YAML:
            raise FileTypeError(
                'Database().Read_YAML() was called but `self._file_type = ' \
                + f'{self._file_type!r}`'
            )

        raise UndefFuncError('Database().Read_YAML() not defined')

    # ========
    # Validate
    def Validate(self) -> bool:
        '''
        Validate
        -
        Checks if the database model is valid.

        Parameters
        -
        None

        Returns
        -
        - `bool`
            - Whether or not the database model is valid.
        '''

        raise UndefFuncError('Database().Validate() not defined')

    # ==========================
    # Write Database Model Files
    def Write(self) -> None:
        '''
        Write Database Model Files
        -
        Writes all of the database model files using the stored database model.

        Parameters
        -
        None

        Returns
        -
        None
        '''

        # write database files
        if self._lang_db == LangDb.MSSQL:
            self.Write_DB_MSSQL()
        else:
            raise LangDbError(
                'Database().Write() tried to find write function for ' \
                + f'{self._lang_db}'
            )
        
        # write orm files
        if self._lang_orm == LangOrm.PYTHON_SQLALCHEMY:
            self.Write_ORM_PYTHON()
        else:
            raise LangOrmError(
                'Database().Write() tried to find write function for ' \
                + f'{self._lang_orm}'
            )
        
    # =================================
    # Write Database Code Files - MSSQL
    def Write_DB_MSSQL(self) -> None:
        '''
        Write Database Code Files - MSSQL
        -
        Write all of the database code files.

        Parameters
        -
        None

        Returns
        -
        None
        '''

        raise UndefFuncError('Database().Write_DB_MSSQL() not defined')

    # =================================
    # Write Database ORM Files - PYTHON
    def Write_ORM_PYTHON(self) -> None:
        '''
        Write Database ORM Files - PYTHON
        -
        Write all of the database code files.

        Parameters
        -
        None

        Returns
        -
        None
        '''

        raise UndefFuncError('Database().Write_ORM_PYTHON() not defined')


# =============================================================================
# End of File
# =============================================================================
