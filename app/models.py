from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    Categoryname=models.CharField(max_length=100,primary_key=True)
    Categoryid=models.IntegerField()

    def __str__(self):
        return self.Categoryname

class Product(models.Model):
    Categoryname=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdate=models.DateField()

    def __str__(self):
        return self.Pname