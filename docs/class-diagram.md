# DB Model Creator Class Diagram
Created by: Shaun Altmann

``` mermaid
classDiagram
    namespace Component-Values {
        %% Abstract Component Value Object
        class CompValue {
            << abstract class >>
            - _data : str
            + data : str << readonly >>
            # lang_db : LangDb | None << static >>
            # lang_orm : LangOrm | None << static >>
            # tables : List~ORM_Table~ << static >>
            # views : List~ORM_View~ << static >>

            + CompValue(data : str) << constructor >>
            + Duplicate() CompValue << override >>
            # GetData(lvl : VerbosityLevel) List~str~ << override >>
            + LoadData(lang_db : LangDb, lang_orm : LangOrm, tables : List~ORM_Table~, views : List~ORM_View~) << static >>
            + Validate() bool << abstract >>
        }

        %% Contains the default value of a component (e.g. default parameter
        %%  value)
        class CompValue_Default {
            + CompValue_Default(data : str) << constructor >>
            + Duplicate() CompValue_Default << override >>
            + Validate() bool << override >>
        }

        %% Contains the description of a component (e.g. property description)
        class CompValue_Desc {
            + CompValue_Desc(data : str) << constructor >>
            + Duplicate() CompValue_Desc << override >>
            + Validate() bool << override >>
        }

        %% Contains the foreign key of a column
        class CompValue_Fk {
            + CompValue_Fk(data : str) << constructor >>
            + Duplicate() CompValue_Fk << override >>
            + Validate() bool << override >>
        }

        %% Contains the name of a component (e.g. method name)
        class CompValue_Name {
            + CompValue_Name(data : str) << constructor >>
            + Duplicate() CompValue_Name << override >>
            + Validate() bool << override >>
        }

        %% Contains the comment title of a component (e.g. method comment
        %%  title)
        class CompValue_Title {
            + CompValue_Title(data : str) << constructor >>
            + Duplicate() CompValue_Title << override >>
            + Validate() bool << override >>
        }

        %% Contains the return type of a component (e.g. property return type)
        class CompValue_Type {
            + CompValue_Type(data : str) << constructor >>
            + Duplicate() CompValue_Type << override >>
            + Validate() bool << override >>
        }
    }
    OBJ --|> CompValue
    CompValue --> LangDb : lang_db
    CompValue --> LangOrm : lang_orm
    CompValue --> ORM_Table : tables
    CompValue --> ORM_View : views
    CompValue --|> CompValue_Default
    CompValue --|> CompValue_Desc
    CompValue --|> CompValue_Fk
    CompValue --|> CompValue_Name
    CompValue --|> CompValue_Title
    CompValue --|> CompValue_Type

    namespace Generic-Objects {
        %% Collection of supported File Types to read from
        class FileType {
            << enumeration >>
            JSON
            XML
            YAML
        }

        %% Collection of valid Method Types
        class MethodType {
            << enumeration >>
            CLASS
            INSTANCE
            STATIC
        }

        %% Generic Object implemented by all other Classes
        class OBJ {
            << abstract class >>
            + __repr__() str
            + __str__() str
            + Debug(indent : int = 0) str
            + Duplicate() OBJ << abstract >>
            # GetData(lvl : VerbosityLevel) List~str~ << abstract >>
        }

        %% Verbosity Level used for debugging OBJ
        class VerbosityLevel {
            << enumeration >>
            SHORT
            LONG
            ALL
        }
    }
    note for OBJ "Python uses __repr__ and __str__. Custom definition in other
    languages is required."
    note for ColumnType "This needs to be extended to include a list of all
    possible column types for the supported orm and database languages."
    note for FileType "Add more lines here to extend support to reading the
    database model from other file types."

    namespace Object-Components {
        %% Abstract Object Component Object
        class ObjComp {
            << abstract >>
            # _default : CompValue_Default | None
            # _desc : CompValue_Desc
            # _name : CompValue_Name
            # _title : CompValue_Title | None
            # _type : CompValue_Type
            # lang_orm : LangOrm | None << static >>
            + valid : bool << virtual, readonly >>
            + valid_default : bool << readonly >>
            + valid_desc : bool << readonly >>
            + valid_name : bool << readonly >>
            + valid_title : bool << readonly >>
            + valid_type : bool << readonly >>

            + Duplicate() ObjComp << override >>
            # GetData(lvl : VerbosityLevel) List~str~ << override >>
            + LoadData(lang_orm : LangOrm) << static >>
            + ObjComp(name : str, type_ : str, desc : str, default : str | None = None, title : str | None = None) << constructor >>
            + Write(comment : bool) str << abstract >>
        }

        %% Contains the information for a particular ORM object constant
        class ObjComp_Constant {
            + Duplicate() ObjComp_Constant << override >>
            + ObjComp_Constant(name : str, type_ : str, desc : str, title : str, default : str | None = None) << constructor >>
            + Write(comment : bool) str << override >>
        }

        %% Contains the information for a particular ORM object method
        class ObjComp_Method {
            - _method_type : MethodType
            - _params : List~ObjComp_MethodParam~
            + valid : bool << override, readonly >>
            + valid_params : bool << readonly >>
            
            + Duplicate() ObjComp_Method << override >>
            + ObjComp_Method(name : str, type_ : str, desc : str, title : str, methodtype : MethodType, params : List~ObjComp_MethodParam~) << constructor >>
            + Write(comment : bool) str << override >>
        }

        %% Contains the information for a particular ORM object method
        %%  parameter
        class ObjComp_MethodParam {
            + Duplicate() ObjComp_MethodParam << override >>
            + ObjComp_MethodParam(name : str, type_ : str, desc : str, default : str | None = None) << constructor >>
            + Write(comment : bool) str << override >>
        }

        %% Contains the information for a particular ORM object property
        class ObjComp_Property {
            + Duplicate() ObjComp_Property << override >>
            + ObjComp_Property(name : str, type_ : str, desc : str, title : str, default : str | None = None) << constructor >>
            + Write(comment : bool) str << override >>
        }
    }
    OBJ --|> ObjComp
    ObjComp --> CompValue_Default : _default
    ObjComp --> CompValue_Desc : _desc
    ObjComp --> CompValue_Name : _name
    ObjComp --> CompValue_Title : _title
    ObjComp --> CompValue_Type : _type
    ObjComp --> LangOrm : lang_orm
    ObjComp --|> ObjComp_Constant
    ObjComp --|> ObjComp_Method
    ObjComp --|> ObjComp_MethodParam
    ObjComp --|> ObjComp_Property
    ObjComp_Method --> MethodType : _method_type
    ObjComp_Method --> ObjComp_MethodParam : _params

    namespace ORM-Objects {
        %% Abstract ORM Object
        class ORM {
            << abstract >>
            # _desc : CompValue_Desc
            # _name : CompValue_Name
            # _title : CompValue_Title
            # lang_db : LangDb | None << static >>
            # lang_orm : LangOrm | None << static >>
            + name : str << readonly >>
            # tables : List~ORM_Table~ << static >>
            # views : List~ORM_View~ << static >>

            + Duplicate() ORM << override >>
            # GetData(lvl : VerbosityLevel) List~str~ << override >>
            + LoadData(lang_db : LangDb, lang_orm : LangOrm, tables : List~ORM_Table~, views : List~ORM_View~) << static >>
            + ORM(name : str, title : str, desc : str) << constructor >>
            + Validate() bool << abstract >>
            + WriteDb(comment : bool) str << abstract >>
            + WriteOrm(comment : bool) str << abstract >>
        }

        %% ORM Table / View Column
        class ORM_Column {
            - _fk : CompValue_Fk | None
            - _identity : bool
            - _nullable : bool
            - _pk : bool
            - _type : str
            - _unique : bool

            + Duplicate() ORM_Column << override >>
            # GetData(lvl : VerbosityLevel) List~str~ << override >>
            + ORM_Column(name : str, type_ : str, title : str, desc : str, nullable : bool = False, pk : bool = False, identity : bool = False, fk : str | None = None, unique : bool = False) << constructor >>
            + Validate() bool << override >>
            + WriteDb(comment : bool) str << override >>
            + WriteOrm(comment : bool) str << override >>
        }

        %% ORM Table / View Abstract Parent
        class ORM_TV {
            << abstract >>
            # _cols : List~ORM_Column~
            # _constants : List~ObjComp_Constant~
            # _methods : List~ObjComp_Method~
            # _props : List~ObjComp_Property~

            + Duplicate() ORM_TV << override >>
            # GetData(lvl : VerbosityLevel) List~str~ << override >>
            + ORM_TV(name : str, title : str, desc : str, cols : List~ORM_Column~, constants : List~ObjComp_Constant~, methods : List~ObjComp_Method~, props : List~ObjComp_Property~) << constructor >>
            + Validate() bool << override >>
            + WriteDb(comment : bool) str << override >>
            + WriteOrm(comment : bool) str << override >>
        }

        %% ORM Table
        class ORM_Table {
            - _trigger_update : bool

            + Duplicate() ORM_Table << override >>
            # GetData(lvl : VerbosityLevel) List~str~ << override >>
            + ORM_Table(name : str, title : str, desc : str, trigger_update : bool, cols : List~ORM_Column~, constants : List~ObjComp_Constant~, methods : List~ObjComp_Method~, props : List~ObjComp_Property~) << constructor >>
            + Validate() bool << override >>
            + WriteDb(comment : bool) str << override >>
            + WriteOrm(comment : bool) str << override >>
        }

        %% ORM View
        class ORM_View {
            + Duplicate() ORM_View << override >>
            + ORM_View(name : str, title : str, desc : str, cols : List~ORM_Column~, constants : List~ObjComp_Constant~, methods : List~ObjComp_Method~, props : List~ObjComp_Property~) << constructor >>
            + Validate() bool << override >>
            + WriteDb(comment : bool) str << override >>
            + WriteOrm(comment : bool) str << override >>
        }
    }
    OBJ --|> ORM
    ORM --|> ORM_Column
    ORM --> CompValue_Desc : _desc
    ORM --> CompValue_Name : _name
    ORM --> CompValue_Title : _title
    ORM --> LangDb : lang_db
    ORM --> LangOrm : lang_orm
    ORM --> ORM_Table : tables
    ORM --> ORM_View : views
    ORM_Column --> CompValue_Fk : _fk
    ORM_Column --> ColumnType : _type
    ORM --|> ORM_TV
    ORM_TV --> ORM_Column : _cols
    ORM_TV --> ObjComp_Constant : _constants
    ORM_TV --> ObjComp_Method : _methods
    ORM_TV --> ObjComp_Property : _props
    ORM_TV --|> ORM_Table
    ORM_TV --|> ORM_View

    namespace Supported-Languages {
        %% Supported Database Languages
        class LangDb {
            << enumeration >>
            MSSQL
        }

        %% Supported ORM Languages
        class LangOrm {
            << enumeration >>
            PYTHON3
        }
    }
    note for LangDb "Add Database and ORM languages as required
    to these enumerators to extend functionality and support."

    class Database {
        - _file_name : str
        - _file_type : FileType
        - _prefix_orm_table : str
        - _prefix_orm_view : str
        - _save_dir_db : str
        - _save_dir_orm : str
        - _tables : List~ORM_Table~
        - _views : List~ORM_View~

        + Database(file_name : str, prefix_orm_table : str = 'DB_', prefix_orm_view : str = 'VW_', save_dir_db : str = 'output/database/', save_dir_orm : str = 'output/orm') << constructor >>
        + Read()
        + Read_JSON()
        + Read_XML()
        + Read_YAML()
        + Validate()
        + Write()
        + Write_DB_MSSQL()
        + Write_ORM_PYTHON()
    }
    note for Database "Add more Read_* and Write_* methods to extend the
    support to more languages."
    OBJ --|> Database
    Database --> FileType : _file_type
    Database --> ORM_Table : _tables
    Database --> ORM_View : _views
```
