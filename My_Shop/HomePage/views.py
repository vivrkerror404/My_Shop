from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product,offer,bestseller,brand,Contact
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def Home(request):
	products=Product.objects.all();
	offers=offer.objects.all();
	bestsellers=bestseller.objects.all();
	brands=brand.objects.all();
	category=set()
	for i in products:
		category.add(i.prod_category)
	print(products)
	return render(request,'Home.html',{"products":products,"offers":offers,"bestsellers":bestsellers,"brands":brands,"category":category})

def MyContact(request):
	if request.method == "POST":
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		desc=request.POST['desc']
		contact= Contact(name=name,email=email,phone_number=phone,Reason=desc)
		contact.save()
		return redirect('/contact/')

	return render(request,'Contact.html')

def RE(request):
	return render(request,'RE.html')

def tc(request):
	return render(request,'tc.html')

def policy(request):
	return render(request,'policy.html')


def product(request,prod_id):
	product = Product.objects.filter(product_id=prod_id)
	return render(request,'productDetail.html',{"product":product[0]})


def About(request):
	return render(request,'About.html')

	
def Checkout(request):
	cartitems=request.session['prodid']
	print(cartitems)
	totalprice=0
	product_ids=[]
	for i,j in cartitems.items():
		product_ids.append(i)
	allprods=Product.objects.filter(product_id__in=product_ids)
	for i in allprods:
		totalprice+=i.prod_price

	return render(request,'Checkout.html',{"cartitems":allprods,"quantityid":cartitems,"totalprice":totalprice})


def Tracker(request):
	return render(request,'tracker.html')


@csrf_exempt
def Sessionstore(request):
	if request.method == "POST":
		try:
			data = json.loads(request.body)
			print(data)
			if('Cart' in data):
				request.session['prodid'] = data['Cart']
			elif('Wish' in data):
				request.session['prodidwishlist'] = data['Wish']
			# del request.session['prodid']
			# print(request.session['prodid'])
			success="product successfully added to the cart"
			return HttpResponse(success)
		except Exception as e:
			print("error in data ______________________________________")
			success="Some error occur please try again"
			return HttpResponse(e)


def ProdInCart(request):
	#prodids is a dictionary of prodid:quantity pair
	prodid_quant=request.session['prodid']
	print(prodid_quant)
	print(type(prodid_quant))
	prod_id=[]
	prod_quant=[]
	for i,j in prodid_quant.items():
		prod_id.append(i) 
		prod_quant.append(j)
	if len(prod_id) < 1:
		return HttpResponse("NO product added to the cart")
	# print(type(prod_id))
	allprods=Product.objects.filter(product_id__in=prod_id)
	context = {"products":allprods,"prodid_quant":prodid_quant}
	
	return render(request,'myproducts.html',context)



def Wishlist(request):
	try:
		wishlist=request.session['prodidwishlist']
		keys=wishlist.keys();
		allprods=Product.objects.filter(product_id__in=keys)
		# print(request.session.keys())
	except Exception as e:
		# print(request.session['prodid'])
		return HttpResponse("no Wishlist item")
	return render(request,'wishlist.html',{"wishlist":allprods})
	


