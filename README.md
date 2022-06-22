# Collection of assignments for learning Django Rest Framework

## Basic Concepts for DRF

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

    ## Assignment 2(Class Based Views)

    1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.
    2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요
    3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요
    4. blog라는 앱을 만든 후 settings.py에 등록해주세요
    5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.
    6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)
    7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요
    8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요
    9. CBV 기반으로 로그인 / 로구아웃 기능을 구현해주세요
    10. CBV 기반으로 로그인 한 사용자의 게시글의 제목을 리턴해주는 기능을 구현해주세요

    ## Assignment 3(Serializers)
    1. blog 앱에 <게시글, 사용자, 내용>이 포함된 comment 테이블을 작성해주세요
    2. 외래 키를 사용해서 Article, User 테이블과 관계를 맺어주세요
    3. admin.py에 comment를 추가해 자유롭게 생성, 수정 할 수 있도록 해주세요
    4. serializer를 활용해 로그인 한 사용자의 기본 정보와 상세 정보를 리턴해 주는 기능을 만들어주세요
    5. 4번의 serializer에 추가로 로그인 한 사용자의 게시글, 댓글을 리턴해주는 기능을 구현해주세요
    6. blog 앱에 title / category / contents를 입력받아서 게시글을 작성하는 기능을 구현해주세요
    - 만약 title이 5자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
    - 만약 contents가 20자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
    - 만약 카테고리가 지정되지 않았다면 카테고리를 지정해야 한다고 리턴해주세요
    7. custom permission class를 활용해 가입 후 3일 이상 지난 사용자만 게시글을 쓸 수 있도록 해주세요
    - 테스트 할 때에는 가입 후 3분 이상 지난 사용자가 게시글을 쓸 수 있게 해주세요
    - join_date는 datetime field로 만들어주세요


    ## Assignment 4(Django Admin)
    1. admin 페이지에 user admin을 등록하고, userprofile 테이블을 user admin 페이지에서 같이 보고 설정 할 수 있도록 해주세요
    2. article 테이블에 <노출 시작 일자, 노출 종료 일자>를 추가해주세요
    3. article view에 게시글 조회 기능을 만들되, 현재 일자를 기준으로 노출 시작 일자와 노출 종료 일자 사이에 있는 항목들만 리턴해주도록 필터를 설정해주세요
    - 리턴 데이터는 게시글 작성일 기준으로 정렬하여 최근 쓴 글이 가장 먼저 올라오도록 해주세요
    4. 기존 article 생성 기능을 유지하되, article은 admin user 혹은 가입 후 7일이 지난 사용자만 생성 가능하도록 해주세요
    - 조회는 로그인 한 사용자에 대해서만 가능하도록 설정해주세요

    ## Assignment 5(CRUD w/ Serializer Validation)
    1. product라는 앱을 새로 생성해주세요
    2. product 앱에서 <작성자, 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일>가 포함된 product 테이블을 생성해주세요
    3. django serializer에서 기본적으로 제공하는 validate / create / update 기능을 사용해 event 테이블의 생성/수정 기능을 구현해주세요
    * postman으로 파일을 업로드 할 때는 raw 대신 form-data를 사용하고, Key type을 File로 설정해주세요
    4. 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있거나, 로그인 한 사용자가 작성한 product 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요
    5. product field를 admin에서 관리할 수 있도록 등록해주세요
    
    ## Assignment 6(CRUD w/ Serializer Validation Cont.)
    1. product 앱의 product 테이블 구성을 <작성자, 썸네일, 상품 설명, 등록일자, 노출 종료 일자, 가격, 수정 일자, 활성화 여부>로 변경해주세요
    2. django serializer를 사용해 validate / create / update 하는 기능을 구현해주세요
        a) custom validation 기능을 사용해 노출 종료 일자가 현재보다 더 이전 시점이라면 상품을 등록할 수 없도록 해주세요
        b) custom creator 기능을 사용해 상품 설명의 마지막에 "<등록 일자>에 등록된 상품입니다." 라는 문구를 추가해주세요
        c) custom update 기능을 사용해 상품이 update 됐을 때 상품 설명의 가장 첫줄에 "<수정 일자>에 수정되었습니다." 라는 문구를 추가해주세요
    3. product 앱에서 <작성자, 상품, 내용, 평점, 작성일>을 담고 있는 review 테이블을 만들어주세요
    4. review 테이블을 관리자 페이지에서 자유롭게 추가/수정 할 수 있도록 설정해주세요
    5. 현재 날짜를 기준으로, 노출 종료 날짜가 지나지 않았고 활성화 여부가 True이거나 로그인 한 사용자가 등록 한 상품들의 정보를 serializer를 사용해 리턴해주세요
    6. 5번 상품 정보를 리턴 할 때 상품에 달린 review와 평균 점수를 함께 리턴해주세요
        a) 평균 점수는 (리뷰 평점의 합/리뷰 갯수)로 구해주세요
        b) 작성 된 리뷰는 모두 return하는 것이 아닌, 가장 최근 리뷰 1개만 리턴해주세요
    7. 로그인 하지 않은 사용자는 상품 조회만 가능하고, 회원가입 이후 3일 이상 지난 사용자만 상품을 등록 할 수 있도록 권한을 설정해주세요