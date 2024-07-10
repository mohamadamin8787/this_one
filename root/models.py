from django.db import models

class ContactUs(models.Model):
    subject = models.CharField(max_length=50) 
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Services(models.Model):
    title = models.CharField(max_length=50)
    contacs = models.CharField(max_length= 50)
    status = models.BooleanField(default = True)
    def __str__(self) -> str:
        return self.title
