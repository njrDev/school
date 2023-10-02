from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category',related_name='subcategories',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category',related_name='products',on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory',related_name='products',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name