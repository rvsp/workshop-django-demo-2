from django.db import models

from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)

# Create your models here.

class showProfile(BaseUserManager):
    def show_profile(self):
        user = self.get_by_natural_key(self.username)
        return user