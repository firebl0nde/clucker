from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
            max_length = 30,
            unique = True,
            validators = [RegexValidator(
                regex = r'^@\w{3,}$',
                message = 'username must consist of @ followed by 3 alphanumericals'
                )]
    )
    first_name = models.CharField(max_length = 50, blank = False)
    last_name = models.CharField(max_length = 50, blank = False)
    email = models.EmailField(
            blank = False,
            unique = True,
    )
    bio = models.CharField(
            blank = True,
            max_length = 520, ##does not enforce it
    )
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
             User,
             on_delete=models.CASCADE,
             blank = False,
            )
    text = models.CharField(
            blank = True, 
            max_length = 280,
            )
    created_at = models.DateTimeField(auto_now_add=True)

