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
    ReadError, # file read error
    UndefFuncError, # undefined functionality error
)

# generic objects
from .generic_objects import (
    FileType, # supported file types
    MethodType, # object method type
    OBJ, # base object model
    VerbosityLevel, # verbosity levels
)

# object components
from .object_components import (
    ObjComp_Constant,
    ObjComp_Method,
    ObjComp_MethodParam,
    ObjComp_Property,
)

# orm objects
from .orm_objects import (
    ORM_Column,
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
    - GetData(lvl : `VerbosityLevel`) : `List<str>` << override >>
    - Read()
    - Read_JSON()
    - Read_XML()
    - Read_YAML()
    - Validate()
    - Write()
    - Write_DB_MSSQL()
    - Write_ORM_PYTHON()
    '''

    # =======================
    # Method - Equality Check
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Database): return False
        return (
            (self._lang_db == other._lang_db)
            and (self._lang_orm == other._lang_orm)
            and (len(self._tables) == len(other._tables))
            and (len(self._views) == len(other._views))
            and all([table in other._tables for table in self._tables])
            and all([view in other._views for view in self._views])
        )

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

    # =================
    # Method - Get Data
    def GetData(self, lvl: VerbosityLevel) -> List[str]:
        if lvl == VerbosityLevel.SHORT:
            return [
                '_file_name',
                '_lang_db',
                '_lang_orm',
            ]
        elif lvl == VerbosityLevel.LONG:
            return [
                '_file_name',
                '_file_type',
                '_lang_db',
                '_lang_orm',
                '_prefix_orm_table',
                '_prefix_orm_view',
                '_save_dir_db',
                '_save_dir_orm',
                '_tables',
                '_views',
            ]
        else:
            return [
                '_file_name',
                '_file_type',
                '_lang_db',
                '_lang_orm',
                '_prefix_orm_table',
                '_prefix_orm_view',
                '_save_dir_db',
                '_save_dir_orm',
                '_tables',
                '_views',
            ]
    
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

        # import json module
        import json

        # read file
        try:
            with open(self._file_name, 'r') as file:
                data = json.load(file)
        except:
            raise ReadError(
                f'Database().Read_JSON() could not parse file ' \
                + f'`{self._file_name}`'
            )
        
        # set the database language
        self.SetLangDb(data.get('lang_db', None))

        # set the orm language
        self.SetLangOrm(data.get('lang_orm', None))

        # set the tables
        self.SetTables(data.get('tables', None))

        # set the views
        self.SetViews(data.get('views', None))

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

        # import yaml module
        import xmltodict # type: ignore

        # read file
        try:
            with open(self._file_name, 'r') as file:
                data = xmltodict.parse(
                    ''.join(file.readlines()[1:]) # skip xml declaration
                )['database'] # get database data
        except:
            raise ReadError(
                f'Database().Read_XML() could not parse file ' \
                + f'`{self._file_name}`'
            )
        
        print(f'Original: {data}')

        # convert data into required formats
        for key, subkey in [('tables', 'table'), ('views', 'view')]:
            # validate it is a dict with the required sub-key
            if not (
                    (isinstance(data.get(key, None), dict))
                    and (subkey in data[key])
            ): continue

            # convert tables and views into lists
            data[key] = data[key][subkey]

            # only continue if this is now a list
            if not isinstance(data[key], list): continue

            # convert data in each into lists
            for table_view in data[key]:
                # skip if not a dict
                if not isinstance(table_view, dict): continue

                # go through columns, constants, properties
                for key2, subkey2 in [
                        ('columns', 'column'),
                        ('constants', 'constant'),
                        ('props', 'prop'),
                ]:
                    if (
                            (key2 in table_view)
                            and (isinstance(table_view[key2], dict))
                            and (subkey2 in table_view[key2])
                    ):
                        if isinstance(table_view[key2][subkey2], list):
                            table_view[key2] = table_view[key2][subkey2]
                        else:
                            table_view[key2] = [table_view[key2][subkey2]]

                # convert methods into lists
                if (
                        ('methods' in table_view)
                        and (isinstance(table_view['methods'], dict))
                        and ('method' in table_view['methods'])
                ):
                    if isinstance(table_view['methods']['method'], list):
                        table_view['methods'] \
                            = table_view['methods']['method']
                    else:
                        table_view['methods'] \
                            = [table_view['methods']['method']]

                    # convert parameters into lists
                    if isinstance(table_view['methods'], list):
                        for method in table_view['methods']:
                            if (
                                    ('params' in method)
                                    and (isinstance(method['params'], dict))
                                    and ('param' in method['params'])
                            ):
                                if isinstance(method['params']['param'], list):
                                    method['params'] \
                                        = method['params']['param']
                                else:
                                    method['params'] \
                                        = [method['params']['param']]

        print(f'Parsed: {data}')
        
        # set the database language
        self.SetLangDb(data.get('lang_db', None))

        # set the orm language
        self.SetLangOrm(data.get('lang_orm', None))

        # set the tables
        self.SetTables(data.get('tables', None))

        # set the views
        self.SetViews(data.get('views', None))
    
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
        
        # import yaml module
        import yaml # type: ignore

        # read file
        try:
            with open(self._file_name, 'r') as file:
                data = yaml.safe_load(file)
        except:
            raise ReadError(
                f'Database().Read_YAML() could not parse file ' \
                + f'`{self._file_name}`'
            )
        
        # set the database language
        self.SetLangDb(data.get('lang_db', None))

        # set the orm language
        self.SetLangOrm(data.get('lang_orm', None))

        # set the tables
        self.SetTables(data.get('tables', None))

        # set the views
        self.SetViews(data.get('views', None))
    
    # =====================
    # Set Database Language
    def SetLangDb(self, val: object) -> None:
        '''
        Set Database Language
        -
        Gets a value from the read file, and attempts to set the database
        language from this value.

        Parameters
        -
        - val : `object`
            - The value to set the database language to.

        Returns
        -
        None
        '''

        # validate the data exists
        if val is None:
            raise ValueError('Failed to read Database Language (`lang_db`)')

        # validate the data is a string
        if not isinstance(val, str):
            raise TypeError(
                'Database Language (`lang_db`) expected a `str` type, got ' \
                + f'`{type(val)}`'
            )
        
        # validate the data value
        if val not in LangDb:
            raise ValueError(
                'Invalid Database Language (`lang_db`) - expected one of ' \
                + f'`{[lang.value for lang in LangDb]!r}`, got `{val!r}`'
            )

        # set the database language
        self._lang_db = LangDb(val)
    
    # ================
    # Set ORM Language
    def SetLangOrm(self, val: object) -> None:
        '''
        Set ORM Language
        -
        Gets a value from the read file, and attempts to set the ORM language
        from this value.

        Parameters
        -
        - val : `object`
            - The value to set the ORM language to.

        Returns
        -
        None
        '''

        # validate the data exists
        if val is None:
            raise ValueError('Failed to read ORM Language (`lang_orm`)')

        # validate the data is a string
        if not isinstance(val, str):
            raise TypeError(
                'ORM Language (`lang_orm`) expected a `str` type, got ' \
                + f'`{type(val)}`'
            )
        
        # validate the data value
        if val not in LangOrm:
            raise ValueError(
                'Invalid ORM Language (`lang_orm`) - expected one of ' \
                + f'`{[lang.value for lang in LangOrm]!r}`, got `{val!r}`'
            )

        # set the orm language
        self._lang_orm = LangOrm(val)

    # ==========
    # Set Tables
    def SetTables(self, val: object) -> None:
        '''
        Set Tables
        -
        Gets a value from the read file, and attempts to set the tables from
        this value.

        Parameters
        -
        - val : `object`
            - The value to create the tables from.

        Returns
        -
        None
        '''

        # validate the data exists
        if val is None:
            raise ValueError('Failed to read Tables (`tables`)')
        
        # validate the data is a list
        if not isinstance(val, list):
            raise TypeError(
                'Tables (`tables`) expected a `list` type, got ' \
                + f'`{type(val)}`'
            )

        # validate there are 1+ tables
        if len(val) < 1:
            raise ValueError(
                'Tables (`tables`) must contain at least one table'
            )

        # set the tables
        for i, table in enumerate(val):
            # validate the table data is a dict
            if not isinstance(table, dict):
                raise TypeError(
                    f'Table at index `{i}` expected a `dict` type, got ' \
                    + f'`{type(table)}`'
                )
            
            # create table
            try:
                self._tables.append(ORM_Table.FromDict(table))
            except Exception as e:
                raise RuntimeError(
                    f'Failed to create table at index `{i}`: {e!r}'
                )

    # =========
    # Set Views
    def SetViews(self, val: object) -> None:
        '''
        Set Views
        -
        Gets a value from the read file, and attempts to set the views from
        this value.

        Parameters
        -
        - val : `object`
            - The value to create the views from.

        Returns
        -
        None
        '''

        # validate the data exists
        if val is None:
            raise ValueError('Failed to read Views (`views`)')
        
        # validate the data is a list
        if not isinstance(val, list):
            raise TypeError(
                'Views (`views`) expected a `list` type, got ' \
                + f'`{type(val)}`'
            )

        # validate there are 1+ views
        if len(val) < 1:
            raise ValueError(
                'Views (`views`) must contain at least one view'
            )

        # set the views
        for i, view in enumerate(val):
            # validate the view data is a dict
            if not isinstance(view, dict):
                raise TypeError(
                    f'View at index `{i}` expected a `dict` type, got ' \
                    + f'`{type(view)}`'
                )
            
            # create view
            try:
                self._views.append(ORM_View.FromDict(view))
            except Exception as e:
                raise RuntimeError(
                    f'View at index `{i}` failed to create: {e!r}'
                )

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
