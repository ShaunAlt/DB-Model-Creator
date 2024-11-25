# DB Model Creator - Testing - Read File Testing
These files are used to test the ability of the package to read a database model from a provided file, and create the required objects that can accurately represent the database model.

## Test Database Model
Below is the database model that is being used to test the database modelling ability of this package.
``` mermaid
erDiagram
    Statuses {
        tinyint status_id PK "Primary Key of the Status."
        varchar(10) status_name UK "Type of the Status."
    }
    Users {
        bigint user_id PK "Primary Key of the User."
        nvarchar(50) user_name_first "First Name of the User."
        nvarchar(50) user_last "Last Name of the User."
        tinyint status_id FK "Status of the User."
    }
    Orders {
        bigint order_id PK "Primary Key of the Order."
        nvarchar(100) order_code UK "(NULLABLE) Code of the Order."
        tinyint status_id FK "Status of the Order."
    }
    UsersOrders {
        bigint user_id PK, FK "User who placed the order."
        bigint order_id PK, FK "Order placed by the user."
    }
    vwTable_Users {
        bigint user_id "ID of the User."
        int num_orders "Number of orders the user has created."
    }
    vwTable_Orders {
        bigint order_id "ID of the Order."
        int num_users "Number of users who placed the order."
    }
    Statuses ||--o{ Users : "Users.status_id-Statuses.status_id"
    Statuses ||--o{ Orders : "Orders.status_id-Statuses.status_id"
    Users ||--o{ UsersOrders : "UsersOrders.user_id-Users.user_id"
    Orders ||--o{ UsersOrders : "UsersOrders.order_id-Orders.order_id"
```

Below is the class diagram of the ORM that should be created from these tests.
``` mermaid
classDiagram
    class DB_Status {
        + col_status_id : Column
        + col_status_name : Column
        + id : int
        + name : str
        + STATUS_ACTIVE : int << static >>
        + DB_Status(id : int, name : str) << constructor >>
        + GetStatus(name : str) DB_Status << class >>
    }
    class DB_User {
        + col_user_id : Column
        + col_user_name_first : Column
        + col_user_name_last : Column
        + col_status_id : Column
        + id : int
        + name_first : str
        + name_full : str << readonly >>
        + name_last : str
        + status : DB_Status
        + DB_User(id : int, name_first : str, name_last : str, status : DB_Status) << constructor >>
        + GetView() VW_Table_User
    }
    class DB_Order {
        + col_order_id : Column
        + col_order_code : Column
        + col_status_id : Column
        + code : str | None
        + id : int
        + status : DB_Status
        + DB_Order(id : int, code : str, status : DB_Status) << constructor >>
    }
    class DB_UserOrder {
        + col_user_id : Column
        + col_order_id : Column
        + DB_UserOrder(user_id : int, order_id : int) << constructor >>
    }
    class VW_Table_User {
        + col_user_id : Column
        + col_num_orders : Column
    }
    class VW_Table_Order {
        + col_order_id : Column
        + col_num_users : Columns
    }
```