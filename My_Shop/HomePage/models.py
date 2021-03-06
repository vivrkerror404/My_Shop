from django.db import models
import uuid 
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


class Contact(models.Model):
	name=models.CharField(max_length=50,default="")
	email=models.EmailField(max_length=100)
	phone_number = models.CharField(max_length=12) # validators should be a list
	Reason=models.TextField()

	def __str__(self):
		return self.name

class CheckoutOrder(models.Model):
	orderid = models.UUIDField(default = uuid.uuid4,editable = False)
	name=models.CharField(max_length=50,default="")
	email=models.EmailField(max_length=100,default="")
	address1=models.CharField(max_length=500,default="")
	address2=models.CharField(max_length=500,default="")
	city=models.CharField(max_length=50,default="")
	state=models.CharField(max_length=50,default="")
	zip_code=models.CharField(max_length=10,default="")
	total=models.CharField(max_length=50,default="")
	products=models.CharField(max_length=1000,default="")

	def __str__(self):
		return self.name


class OrderTracker(models.Model):
	orderid=models.UUIDField(default = uuid.uuid4,editable = False)
	status=models.CharField(max_length=100)
