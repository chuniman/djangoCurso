from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Profile(models.Model):
    # modelo proxy para el user de django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=150, blank=True)
    phone = models.CharField(max_length=50,blank=True)
    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)

    # auto_now_add es para que anote la fecha en la que se creo ahi
    created = models.DateTimeField(auto_now_add=True)

    # auto_now la fecha en la que se modifico el campo
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username