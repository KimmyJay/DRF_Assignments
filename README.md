# DjangoRestAssignment

**Mutable vs Immutable Objects**

Whenever an object is instantiated, it is assigned a _unique object id_. The type of the object is defined at the runtime and it can’t be changed afterwards. However, it’s _state_ can be changed if it is a mutable object.

-   **mutable**:
    -   list, dictionary
-   **immutable**: 
    -   int, float, tuple, boolean, string

---

**DB Field Key Types**

-   **Parent Key(PK)**
    -   Used to serve as a unique identifier for each row in a table
    -   Cannot accept NULL values
    -   Creates clustered index
    -   A Primary key supports auto increment value
-   **Unique Key(UK)**
    -   Uniquely determines a row which isn’t primary key
    -   Can accepts NULL values
    -   Creates non-clustered index
    -   A unique key does not supports auto increment value
-   **Foreign Key(FK)**
    -   Field that refers to the PK in another table
    -   There can be multiple FKs in one table

---

**Django Filter() vs Get()**

-   **Filter()**
    -   Returns a _queryset_ object
    -   If no item was found matching your criteria, filter() returns an empty queryset instead of an error
-   **Get()**
    -   You expect _one and only one_ item that matches your criteria
    -   Returns an error if the item does not exist or if multiple items exist that match criteria
    -   Utilize _try/except_ block or _shortcut functions_ such as get\_object\_or\_404 in order to handle exceptions