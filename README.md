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


    ------
    ------
    ------
1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.
2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요
3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요
4. blog라는 앱을 만든 후 settings.py에 등록해주세요
5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.
6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)
7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요
8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요
9. CBV 기반으로 로그인 / 로구아웃 기능을 구현해주세요
10. CBV 기반으로 로그인 한 사용자의 게시글의 제목을 리턴해주는 기능을 구현해주세요# DRF_Assignment_Two
