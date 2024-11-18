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
| trigger_update | Boolean flag indicating whether or not the table should have an Update table created for it. An update table is a table with the same name (with `UPDATE_` prefixed) with a trigger which stores any data changes to the original table in the update table. | `trigger_update = 1` |
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
    - Users:
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
    - Users:
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
| :---: | | :--- | :--- |

### Creating a Column in JSON
### Creating a Column in XML
### Creating a Column in YAML

## Creating an Object Constant
To create a constant for a particular ORM object in the database model, you
will need to create a constant object with the following values:
| Data Label | Purpose | Example Value |
| :---: | | :--- | :--- |

### Creating an Object Constant in JSON
### Creating an Object Constant in XML
### Creating an Object Constant in YAML

## Creating an Object Method
To create a method for a particular ORM object in the database model, you will
need to create a method object with the following values:
| Data Label | Purpose | Example Value |
| :---: | | :--- | :--- |

### Creating an Object Method in JSON
### Creating an Object Method in XML
### Creating an Object Method in YAML

## Creating an Object Method Parameter
To create a parameter for a particular method within an ORM object in the
database model, you will need to create a method parameter object with the
following values:
| Data Label | Purpose | Example Value |
| :---: | | :--- | :--- |

### Creating an Object Method Parameter in JSON
### Creating an Object Method Parameter in XML
### Creating an Object Method Parameter in YAML

## Creating an Object Property
To create a property for a particular ORM object in the database model, you
will need to create a property object with the following values:
| Data Label | Purpose | Example Value |
| :---: | | :--- | :--- |

### Creating an Object Property in JSON
### Creating an Object Property in XML
### Creating an Object Property in YAML