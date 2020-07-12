from django.db import models

# Create your models here.
class Product(models.Model):
	product_id = models.CharField(max_length=50,default="")
	prod_name = models.CharField(max_length=50,default="")
	prod_desc = models.CharField(max_length=1000,default="")
	prod_price=models.IntegerField()
	prod_category=models.CharField(max_length=100,default="")
	prod_image=models.ImageField(upload_to="images",default="")


	def __str__(self):
		return self.prod_name

class offer(models.Model):
	offer_name = models.CharField(max_length=50,default="")
	offer_desc=models.CharField(max_length=100,default="")
	offer_image=models.ImageField(upload_to="images",default="")

	def __str__(self):
		return self.offer_name

class bestseller(models.Model):
	bestseller_name = models.CharField(max_length=50,default="")
	bestseller_image=models.ImageField(upload_to="images",default="")

	def __str__(self):
		return self.bestseller_name

class brand(models.Model):
	brand_name = models.CharField(max_length=50,default="")
	brand_image=models.ImageField(upload_to="images",default="")

	def __str__(self):
		return self.brand_name