# DB Model Creator - Creating a New Model
Created by: Shaun Altmann

## Table of Contents
- [Creating the Overall Model](#creating-the-overall-model)
    - [Creating the Overall Model in JSON](#creating-the-overall-model-in-json)
    - [Creating the Overall Model in XML](#creating-the-overall-model-in-xml)
    - [Creating the Overall Model in YAML](#creating-the-overall-model-in-yaml)
- [Creating a Table](#creating-a-table)
    - [Creating a Table in JSON](#creating-a-table-in-json)
    - [Creating a Table in XML](#creating-a-table-in-xml)
    - [Creating a Table in YAML](#creating-a-table-in-yaml)
- [Creating a View](#creating-a-view)
    - [Creating a View in JSON](#creating-a-view-in-json)
    - [Creating a View in XML](#creating-a-view-in-xml)
    - [Creating a View in YAML](#creating-a-view-in-yaml)
- [Creating a Column](#creating-a-column)
    - [Creating a Column in JSON](#creating-a-column-in-json)
    - [Creating a Column in XML](#creating-a-column-in-xml)
    - [Creating a Column in YAML](#creating-a-column-in-yaml)
- [Creating an Object Constant](#creating-an-object-constant)
    - [Creating an Object Constant in JSON](#creating-an-object-constant-in-json)
    - [Creating an Object Constant in XML](#creating-an-object-constant-in-xml)
    - [Creating an Object Constant in YAML](#creating-an-object-constant-in-yaml)
- [Creating an Object Method](#creating-an-object-method)
    - [Creating an Object Method in JSON](#creating-an-object-method-in-json)
    - [Creating an Object Method in XML](#creating-an-object-method-in-xml)
    - [Creating an Object Method in YAML](#creating-an-object-method-in-yaml)
- [Creating an Object Method Parameter](#creating-an-object-method-parameter)
    - [Creating an Object Method Parameter in JSON](#creating-an-object-method-parameter-in-json)
    - [Creating an Object Method Parameter in XML](#creating-an-object-method-parameter-in-xml)
    - [Creating an Object Method Parameter in YAML](#creating-an-object-method-parameter-in-yaml)
- [Creating an Object Property](#creating-an-object-property)
    - [Creating an Object Property in JSON](#creating-an-object-property-in-json)
    - [Creating an Object Property in XML](#creating-an-object-property-in-xml)
    - [Creating an Object Property in YAML](#creating-an-object-property-in-yaml)

## Creating the Overall Model
To create the overall database model, you will need to create a new file in the
language you prefer (see [README.md](../README.md) for a list of supported
languages). Then, you will need to create a base database object with the
following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| lang_db | Defines the language that the database will be written in (e.g. MSSQL, PostgreSQL). | `lang_db = "mssql"` |
| lang_orm | Defines the language that the ORM will be written in (e.g. Python-SQLAlchemy, C++). | `lang_orm = "python-sqlalchemy"` |
| tables | Contains a list of all of the tables in the database. See [Creating a Table](#creating-a-table) for information on how to create each table. | `tables = [...]` |
| views | Contains a list of all of the views in the database. See [Creating a View](#creating-a-view) for information on how to create each view. | `views = [...]` |

### Creating the Overall Model in JSON
``` json file=example.json
{
    "lang_db": "mssql",
    "lang_orm": "python-sqlalchemy",
    "tables": [
        {
            "table 1": "See `Creating a Table` for information on creating a table."
        }
    ],
    "views": [
        {
            "table 2": "See `Creating a View` for information on creating a view."
        }
    ]
}
```

### Creating the Overall Model in XML
``` xml file=example.xml
<?xml version="1.0" encoding="UTF-8">
<database>
    <lang_db>mssql</lang_db>
    <lang_orm>python-sqlalchemy</lang_orm>
    <tables>
        <table>
            See `Creating a Table` for information on creating a table.
        </table>
    </tables>
    <views>
        <view>
            See `Creating a View` for information on creating a view.
        </view>
    </views>
</database>
```

### Creating the Overall Model in YAML
``` yaml file=example.yaml
lang_db: "mssql"
lang_orm: "python-sqlalchemy"
tables:
    - table1: "See `Creating a Table` for information on creating a table."
views:
    - view1: "See `Creating a View` for information on creating a view."
```

## Creating a Table
To create an individual table in the database model, you will need to create a
table object with the following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| name | Name of the table is it would appear in the database | `name = "Users"` |
| title | Comment title for the table. This should be only a couple of keywords that describe the purpose of the table | `title = "User Accounts"` |
| desc | Long-winded description of the table. This should be a single paragraph explaining the purpose of the table. | `desc = "Contains all of the user accounts for the application."` |
| trigger_update | Boolean flag indicating whether or not the table should have an Update table created for it. An update table is a table with the same name (with `UPDATE_` prefixed) with a trigger which stores any data changes to the original table in the update table. | `trigger_update = True` |
| columns | Contains a list of all columns in the table, in the order that they should be created in the database. See [Creating a Column](#creating-a-column) for information on how to create each column. | `columns = [...]` |
| constants | Contains a list of all constants that the ORM object referencing the database table should contain. See [Creating an Object Constant](#creating-an-object-constant) for information on how to create each constant. | `constants = [...]` |
| methods | Contains a list of all methods that the ORM object referencing the database table should contain. See [Creating an Object Method](#creating-an-object-method) for information on how to create each method. | `methods = [...]` |
| props | Contains a list of all properties that the ORM object referencing the database table should contain. See [Creating an Object Property](#creating-an-object-property) for information on how to create each property. | `props = [...]` |

### Creating a Table in JSON
``` json file=example.json
"tables": [
    {
        "name": "Users",
        "title": "User Accounts",
        "desc": "Contains all of the user accounts for the application.",
        "trigger_update": "1",
        "columns": [
            {
                "col 1": "See `Creating a Column` for information on creating a column."
            }
        ],
        "constants": [
            {
                "constant 1": "See `Creating an Object Constant` for information on creating a constant."
            }
        ],
        "methods": [
            {
                "method 1": "See `Creating an Object Method` for information on creating a method."
            }
        ],
        "props": [
            {
                "property 1": "See `Creating an Object Property` for information on creating a property."
            }
        ]
    }
]
```

### Creating a Table in XML
``` xml file=example.xml
<tables>
    <table>
        <name>Users</name>
        <title>User Accounts</title>
        <desc>Contains all of the user accounts for the application.</desc>
        <trigger_update>1</trigger_update>
        <columns>
            <column>
                See `Creating a Column` for information on creating a column.
            </column>
        </columns>
        <constants>
            <constant>
                See `Creating an Object Constant` for information on creating a constant.
            </constant>
        </constants>
        <methods>
            <method>
                See `Creating an Object Method` for information on creating a method.
            </method>
        </methods>
        <props>
            <property>
                See `Creating an Object Property` for information on creating an object property.
            </property>
        </props>
    </table>
</tables>
```

### Creating a Table in YAML
``` yaml file=example.yaml
tables:
    -
        - name: "Users"
        - title: "User Accounts"
        - desc: "Contains all of the user accounts for the application."
        - trigger_update: "1"
        - columns:
            - column1: "See `Creating a Column` for information on creating a column."
        - constants:
            - constant1: "See `Creating an Object Constant` for information on creating a constant."
        - methods:
            - method1: "See `Creating an Object Method` for information on creating a method."
        - props:
            - property1: "See `Creating an Object Property` for information on creating a property."
```

## Creating a View
To create an individual view in the database model, you will need to create a
view object with the following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| name | Name of the view is it would appear in the database | `name = "Users"` |
| title | Comment title for the view. This should be only a couple of keywords that describe the purpose of the view | `title = "User Accounts"` |
| desc | Long-winded description of the view. This should be a single paragraph explaining the purpose of the view. | `desc = "Contains all of the user accounts for the application."` |
| columns | Contains a list of all columns in the view, in the order that they should be created in the database. See [Creating a Column](#creating-a-column) for information on how to create each column. | `columns = [...]` |
| constants | Contains a list of all constants that the ORM object referencing the database view should contain. See [Creating an Object Constant](#creating-an-object-constant) for information on how to create each constant. | `constants = [...]` |
| methods | Contains a list of all methods that the ORM object referencing the database view should contain. See [Creating an Object Method](#creating-an-object-method) for information on how to create each method. | `methods = [...]` |
| props | Contains a list of all properties that the ORM object referencing the database view should contain. See [Creating an Object Property](#creating-an-object-property) for information on how to create each property. | `props = [...]` |

### Creating a View in JSON
``` json file=example.json
"views": [
    {
        "name": "Users",
        "title": "User Accounts",
        "desc": "Contains all of the user accounts for the application.",
        "columns": [
            {
                "col 1": "See `Creating a Column` for information on creating a column."
            }
        ],
        "constants": [
            {
                "constant 1": "See `Creating an Object Constant` for information on creating a constant."
            }
        ],
        "methods": [
            {
                "method 1": "See `Creating an Object Method` for information on creating a method."
            }
        ],
        "props": [
            {
                "property 1": "See `Creating an Object Property` for information on creating a property."
            }
        ]
    }
]
```

### Creating a View in XML
``` xml file=example.xml
<views>
    <view>
        <name>Users</name>
        <title>User Accounts</title>
        <desc>Contains all of the user accounts for the application.</desc>
        <columns>
            <column>
                See `Creating a Column` for information on creating a column.
            </column>
        </columns>
        <constants>
            <constant>
                See `Creating an Object Constant` for information on creating a constant.
            </constant>
        </constants>
        <methods>
            <method>
                See `Creating an Object Method` for information on creating a method.
            </method>
        </methods>
        <props>
            <property>
                See `Creating an Object Property` for information on creating an object property.
            </property>
        </props>
    </view>
</views>
```

### Creating a View in YAML
``` yaml file=example.yaml
views:
    -
        - name: "Users"
        - title: "User Accounts"
        - desc: "Contains all of the user accounts for the application."
        - columns:
            - column1: "See `Creating a Column` for information on creating a column."
        - constants:
            - constant1: "See `Creating an Object Constant` for information on creating a constant."
        - methods:
            - method1: "See `Creating an Object Method` for information on creating a method."
        - props:
            - property1: "See `Creating an Object Property` for information on creating a property."
```

## Creating a Column
To create a column for a particular table or view in the database model, you
will need to create a column object with the following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| name | Column name (as it appears in the database). | `name = "user_id"` |
| type_ | Column data type (database language). | `type_ = "bigint"` |
| title | Column comment title, used in a comment block when defining the column. | `title = "User ID"` |
| desc | Column description. | `desc = "Unique identifier ID for the User."` |
| nullable | **OPTIONAL** Whether or not the column is nullable. Defaults to `True`, meaning that the column will accept null values. This is overwritten to `False` if the column is a primary key. | `nullable = "False"` |
| pk | **OPTIONAL** Whether or not the column is part of the primary key for the table. Defaults to `False`. | `pk = "True"` |
| identity | **OPTIONAL** Whether or not the column is an identity (AKA auto-increment) column. Defaults to `False`, however this value will only be checked if the `pk` flag is `True`. | `identity = "True"` |
| fk | **OPTIONAL** If not specified, then the current column does not have a foreign key reference to another primary key. If specified, it should be in the format "\<Table>.\<Column>", where the string contains the name of the table and primary key column that it is referencing. | `fk = "Users.user_id"` |
| unique | **OPTIONAL** Whether or not the column has a unique key constraint. Defaults to `False`, and overwritten to `False` if the `pk` flag is `True`. | `unique = "True"` |

### Creating a Column in JSON
``` json file=example.json
"columns": [
    {
        "name": "user_id",
        "type_": "bigint",
        "title": "User ID",
        "desc": "Primary Key Identifier for all Users.",
        "pk": "True",
        "identity": "True"
    },
    {
        "name": "status_id",
        "type_": "tinyint",
        "title": "User Status",
        "desc": "Status of the User.",
        "nullable": "False",
        "fk": "Statuses.status_id"
    },
    {
        "name": "username",
        "type_": "nvarchar(100)",
        "title": "User Username",
        "desc": "Username of the current user (must be unique).",
        "nullable": "False",
        "unique": "True"
    }
]
```

### Creating a Column in XML
``` xml file=example.xml
<columns>
    <column>
        <name>user_id</name>
        <type_>bigint</type_>
        <title>User ID</title>
        <desc>Primary Key Identifier for all Users.</desc>
        <pk>True</pk>
        <identity>True</identity>
    </column>
    <column>
        <name>status_id</name>
        <type_>tinyint</type_>
        <title>User Status</title>
        <desc>Status of the User.</desc>
        <nullable>False</nullable>
        <fk>Statuses.status_id</fk>
    </column>
    <column>
        <name>username</name>
        <type_>nvarchar(100)</type_>
        <title>User Username</title>
        <desc>Username of the current user (must be unique).</desc>
        <nullable>False</nullable>
        <unique>True</unique>
    </column>
</columns>
```

### Creating a Column in YAML
``` yaml file=example.yaml
columns:
    -
        - name: "user_id"
        - type_: "bigint"
        - title: "User ID"
        - desc: "Primary Key Identifier for all Users."
        - pk: "True"
        - identity: "True"
    -
        - name: "status_id"
        - type_: "tinyint"
        - title: "User Status"
        - desc: "Status of the User."
        - nullable: "False"
        - fk: "Statuses.status_id"
    -
        - name: "username"
        - type_: "nvarchar(100)"
        - title: "User Username"
        - desc: "Username of the current user (must be unique)."
        - nullable: "False"
        - unique: "True"
```

## Creating an Object Constant
To create a constant for a particular ORM object in the database model, you
will need to create a constant object with the following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| name | Variable name of the ORM object constant. | `name = "CONSTANT_1"` |
| type_ | Data type of the ORM object constant. | `type_ = "str"` |
| desc | Description of the ORM object constant. | `desc = "A short description about this constant."` |
| title | Comment title of the ORM object constant. This title will be placed above the constant as a comment. | `title = "Constant Title"` |
| default | **OPTIONAL**. If not specified, a `None` or `null` value will be assigned to the constant. If specified, this should contain the value of the constant. | `default = "Default Constant Value"` |

### Creating an Object Constant in JSON
``` json file=example.json
"constants": [
    {
        "name": "STATUS_ACTIVE",
        "type_": "int",
        "desc": "Contains the active status ID.",
        "title": "Active Status",
        "default": "1" // OPTIONAL
    }
]
```

### Creating an Object Constant in XML
``` xml file=example.xml
<constants>
    <constant>
        <name>STATUS_ACTIVE</name>
        <type_>int</type_>
        <desc>Contains the active status ID.</desc>
        <title>Active Status</title>
        <default>1</default> <!-- OPTIONAL -->
    </constant>
</constants>
```

### Creating an Object Constant in YAML
``` yaml file=example.yaml
constants:
    -
        - name: "STATUS_ACTIVE"
        - type_: "int"
        - desc: "Contains the active status ID."
        - title: "Active Status"
        - default: 1 # OPTIONAL
```

## Creating an Object Method
To create a method for a particular ORM object in the database model, you will
need to create a method object with the following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| name | Name of the method in the ORM object. | `name = "GetId"` |
| type_ | Return datatype of the method. | `type_ = "int"` |
| desc | Description of the method. | `desc = "Get the ID of the current user."` |
| title | Comment title of the model. Used in a comment block for the method. | `title = "Get ID"` |
| methodtype | **OPTIONAL** Type of method that is being created. Defaults to "instance", however other valid options are "static" and "class". | `methodtype = "static"` |
| params | Contains an ordered list of parameters that the method has. See [Creating an Object Method Parameter](#creating-an-object-method-parameter) for information on how to create each parameter. | `params = [...]` |
| default | **OPTIONAL** Default return value for the method. If not specified, the method will raise a custom exception stating that it's functionality has not yet been defined. | `default = "0"` |

### Creating an Object Method in JSON
``` json file=example.json
"methods": [
    {
        "name": "GetId",
        "type_": "int",
        "desc": "Get the ID of the current user.",
        "title": "Get ID",
        "methodtype": "instance", // OPTIONAL
        "params": [
            {
                "param1": "See `Creating an Object Method Parameter` for information on creating method parameters."
            }
        ],
        "default": "0" // OPTIONAL
    }
]
```

### Creating an Object Method in XML
``` xml file=example.xml
<methods>
    <method>
        <name>GetId</name>
        <type_>int</type_>
        <desc>Get the ID of the current user.</desc>
        <title>Get ID</title>
        <methodtype>instance</methodtype> <!-- OPTIONAL -->
        <params>
            <param>
                See `Creating an Object Method Parameter` for information on creating method parameters.
            </param>
        </params>
        <default>0</default> <!-- OPTIONAL -->
    </method>
</methods>
```

### Creating an Object Method in YAML
``` yaml file=example.yaml
methods:
    -
        - name: "GetId"
        - type_: "int"
        - desc: "Get the ID of the current user."
        - title: "Get ID"
        - methodtype: "instance" # OPTIONAL
        - params:
            - param1: "See `Creating an Object Method Parameter` for information on creating method parameters."
        - default: "0" # OPTIONAL
```

## Creating an Object Method Parameter
To create a parameter for a particular method within an ORM object in the
database model, you will need to create a method parameter object with the
following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| name | Parameter name. | `name = "add_one"` |
| type_ | Parameter data type (in the ORM language). | `type_ = "bool"` |
| desc | Parameter description. | `desc = "Flag for whether or not to add 1 to the value."` |
| default | **OPTIONAL** Default value for the parameter. If not specified, it means the parameter is a positional argument with no default value. If specified, the parameter is a keyword argument with the specified default value. | `default = "False"` |

### Creating an Object Method Parameter in JSON
``` json file=example.json
"params": [
    {
        "name": "add_one",
        "type_": "bool",
        "desc": "Flag for whether or not to add 1 to the value.",
        "default": "False", // OPTIONAL
    }
]
```

### Creating an Object Method Parameter in XML
``` xml file=example.xml
<params>
    <param>
        <name>add_one</name>
        <type_>bool</type_>
        <desc>Flag for whether or not to add 1 to the value.</desc>
        <default>False</default> <!-- OPTIONAL -->
    </param>
</params>
```

### Creating an Object Method Parameter in YAML
``` yaml file=example.yaml
params:
    -
        - name: "add_one"
        - type_: "bool"
        - desc: "Flag for whether or not to add 1 to the value."
        - default: "False"
```

## Creating an Object Property
To create a property for a particular ORM object in the database model, you
will need to create a property object with the following values:
| Data Label | Purpose | Example Value |
| :---: | :--- | :--- |
| name | Name of the ORM property. | `name = "id"` |
| type_ | Return data type of the ORM property (in the ORM language). | `type_ = "int"` |
| desc | Description of the ORM property. | `desc = "ID of the current user as an integer."` |
| title | Comment title of the ORM property, used as a comment block for the property definition. | `title = "User ID"` |
| default | **OPTIONAL** The default return value for the property. If not defined, a custom exception stating that the property has not been defined will be created. | `default = "0"` |

### Creating an Object Property in JSON
``` json file=example.json
"props": [
    {
        "name": "id",
        "type_": "int",
        "desc": "ID of the current user as an integer.",
        "title": "User ID",
        "default": "0" // OPTIONAL
    }
]
```

### Creating an Object Property in XML
``` xml file=example.xml
<props>
    <prop>
        <name>id</name>
        <type_>int</type_>
        <desc>ID of the current user as an integer.</desc>
        <title>User ID</title>
        <default>0</default>
    </prop>
</props>
```

### Creating an Object Property in YAML
``` yaml file=example.yaml
props:
    -
        - name: "id"
        - type_: "int"
        - desc: "ID of the current user as an integer."
        - title: "User ID"
        - default: "0"
```
