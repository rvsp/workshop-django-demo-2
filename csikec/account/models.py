from django.db import models
from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)
from django.core.validators import RegexValidator

# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
ICODE_REGEX = '^[a-zA-Z.+-]*$'

class UserDetailsManager(BaseUserManager):
    def create_user(self, username, i_code, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(username = username, i_code = i_code,
                            email = self.normalize_email(email))
        user.set_created_by(username)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class UserDetails(AbstractBaseUser):

    username = models.CharField(
					max_length=10,
					validators = [
                    RegexValidator(regex = USERNAME_REGEX,
                    message='Username must be alphanumeric or contain numbers',
                    code='invalid_username')],unique=True)
    
    firstname = models.CharField(max_length=50, null=False,
                validators = [
                RegexValidator(regex = ICODE_REGEX,
                message='Firstname must be Alphabet.',
                code='invalid_first_name')])
    lastname = models.CharField(max_length=50, null=False,
                validators = [
                RegexValidator(regex = ICODE_REGEX,
                message='Lastname must be Alphabet.',
                code='invalid_last_name')])
	
    email = models.EmailField(max_length=255,unique=False,
			verbose_name='email address')

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    mobile=models.CharField(max_length=10,null= True)
    branch=models.CharField(max_length=50,null= True )
    created_by = models.CharField(max_length=50,null= True )
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50,null= True )
    modified_ts = models.DateTimeField(auto_now_add=True)
    
    objects = UserDetailsManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table='user_details'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return None

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

