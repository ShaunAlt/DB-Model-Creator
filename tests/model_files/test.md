# DB Model Creator - Testing - Read File Testing
These files are used to test the ability of the package to read a database model from a provided file, and create the required objects that can accurately represent the database model.

## Test Database Model
Below is the database model that is being used to test the database modelling ability of this package.
``` mermaid
erDiagram
    Statuses {
        tinyint status_id PK
        varchar(10) status_name UK
    }
    Users {
        bigint user_id PK
        nvarchar(50) user_name_first
        nvarchar(50) user_last
        tinyint status_id FK
    }
    Orders {
        bigint order_id PK
        nvarchar(100) order_code UK "NULLABLE"
        tinyint status_id FK
    }
    UsersOrders {
        %% No Update Trigger
        bigint user_id PK, FK
        bigint order_id PK, FK
    }
    vwTable_Users {
        bigint user_id
        int num_orders
    }
    vwTable_Orders {
        bigint order_id
        int num_users
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
        + id : int << readonly >>
        + name : str << readonly >>
        + STATUS_ACTIVE : str << static >>
        + DB_Status(id : int, name : str) << constructor >>
        + GetStatus(name : str) DB_Status << class >>
    }
    class DB_User {
        + col_user_id : Column
        + col_user_name_first : Column
        + col_user_name_last : Column
        + col_status_id : Column
        + id : int << readonly >>
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
        + id : int << readonly >>
        + status : DB_Status
        + DB_Order(id : int, status : DB_Status, code : str | None = None) << constructor >>
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
        + col_num_users : Column
    }
```