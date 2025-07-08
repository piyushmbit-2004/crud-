from django.db import models

# Create your models here.
class Crudapp(models.Model):
    name=models.CharField(max_length=30)
    father=models.CharField(max_length=100)
    mother=models.CharField(max_length=30)
    email=models.CharField(max_length=300)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    images=models.ImageField(upload_to='images/')
    class meta:
        data_tables= 'crud' 