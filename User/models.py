from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None, realname=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
            realname=realname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password=None, email=None, realname=None):
        user = self.create_user(
            username=username,
            password=password,
            realname=realname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField("username", max_length=50, unique=True)
    password = models.CharField("password", max_length=128)
    email = models.EmailField("email", max_length=50)
    realname = models.CharField("realname", max_length=50)
    join_date = models.DateTimeField("joindate", auto_now_add=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['realname']

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.realname}"

    objects = UserManager()

    # 로그인 사용자의 특정 테이블의 crud 권한을py 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True
    
    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label): 
        return True
    
    # admin 권한 설정
    @property
    def is_staff(self): 
        return self.is_admin


class Dish(models.Model):
    name = models.CharField("name", max_length=50)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='user', on_delete=models.CASCADE, default="")
    TMI = models.TextField('TMI', max_length=300, null=True)
    age = models.IntegerField('age', default=0)
    favorite_dish = models.ManyToManyField(Dish, verbose_name='favorite_dish')