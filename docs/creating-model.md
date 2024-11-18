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
| Data Name | Purpose | Example Value |
| :---: | :--- | :--- |
| lang_db | Defines the language that the database will be written in (e.g. MSSQL, PostgreSQL). | `lang_db = "mssql"` |
| lang_orm | Defines the language that the ORM will be written in (e.g. Python-SQLAlchemy, C++). | `lang_orm = "python-sqlalchemy"` |
| tables | Contains a list of all of the tables in the database. See [Creating a Table](#creating-a-table) for information on how to create each table | `tables = [...]` |
| views | Contains a list of all of the views in the database. See [Creating a View](#creating-a-view) for information on how to create each view | `views = [...]` |

### Creating the Overall Model in JSON
See below for an example of how to create the overall database model in JSON.
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

## Creating a View

## Creating a Column
## Creating an Object Constant
## Creating an Object Method
## Creating an Object Method Parameter
## Creating an Object Property