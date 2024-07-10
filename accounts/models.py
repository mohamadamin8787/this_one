from django.db import models
from django.contrib.auth.models import AbstractUser

class PersonUser(AbstractUser):
    id_coad  = models.CharField(max_length = 10)
    phone  = models.CharField(max_length = 11)
    address  = models.CharField(max_length = 100, null = True , blank = True)
    image  = models.ImageField(upload_to='user', default='inside.jpeg')

    def __str__(self):
        return self.username

    

