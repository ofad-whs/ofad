from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self, email, nickname, point, password):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            point = point,
        )

        # 비밀번호 유효성 검사
        '''
        try:
            validate_password(password, user)
        except ValidationError as e:
            raise ValueError(str(e))
        '''

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,nickname,point,password):
        user= self.create_user(
            email,
            password=password,
            nickname=nickname,
            point=point,
        )
        user.is_admin = True
        user.save(using=self._db)



  
  
"""
    *Model Name : Suser
    유저 커스텀 모델
    User 상속 받음
    추가된 필드 : email, nickname, point, is_admin
"""      
class SUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    nickname=models.CharField(
        verbose_name='nickname',
        max_length=255,
        unique=True,
    )
    point = models.BigIntegerField(
        verbose_name='point',
        default=2000,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects=UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname','point']
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    

