from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default = True)
    
    def __str__(self) -> str:
        return self.title
    

class Services(models.Model):
    image = models.ImageField(upload_to='service', default='inside.jpeg')
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    description  = models.TextField()
    option = models.CharField(max_length=50)
    counted_viwe = models.CharField(max_length=50,default = 0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    status  = models.BooleanField(default = True)
    
    def __str__(self) -> str:
        return self.title

