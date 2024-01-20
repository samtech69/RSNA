from django.db import models


class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60,unique=True)
    description=models.TextField()
    pic=models.ImageField(upload_to="uploads/product")

    def __str__(self):
        return str(self.id)+" | "+self.name

class Result(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60,unique=True)
    pic=models.ImageField(upload_to="uploads/items")

    def __str__(self):
        return str(self.id)+" | "+self.name
    
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60,unique=True)
    lastname=models.CharField(max_length=60,unique=True)
    email=models.EmailField()
    phone=models.CharField(max_length=12,unique=True)
    message=models.TextField()

    def __str__(self):  
        return str(self.id)+" | "+self.name
# passwrd:6261
    
class Newsletter(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField()

    def __str__(self):  
        return str(self.id)
    
class Gallery(models.Model):
     id=models.AutoField(primary_key=True)
     pic=models.ImageField(upload_to="uploads/gallery")