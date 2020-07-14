from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Product,offer,bestseller,brand,Contact,CheckoutOrder,OrderTracker
from django.contrib.auth.models import User
from django.core import serializers
import json,uuid
import ast
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
	if request.user.is_authenticated:

   
		if request.method == "POST":
			name=request.POST['checkoutname']
			address1=request.POST['address1']
			address2=request.POST['address2']
			city=request.POST['city']
			state=request.POST['state']
			zip_code=request.POST['zip_code']
			price=request.session['totalprice']
			prods_quant=request.session['prodid']
			orderid=uuid.uuid4() 
			print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print(orderid)

			checkout=CheckoutOrder(orderid=orderid,name=name,email=request.user.email,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,total=price,products=prods_quant)

			checkout.save()
			ordertracker=OrderTracker(orderid=orderid,status="Under Processing")
			ordertracker.save()
			return redirect('/checkout/')


		cartitems=request.session['prodid']
		print(cartitems)
		totalprice=0
		product_ids=[]
		for i,j in cartitems.items():
			product_ids.append(i)
		allprods=Product.objects.filter(product_id__in=product_ids)
		for i in allprods:
			totalprice+=i.prod_price * cartitems[i.product_id]
		request.session['totalprice']=totalprice

		return render(request,'Checkout.html',{"cartitems":allprods,"quantityid":cartitems,"totalprice":totalprice})
	else:
		return HttpResponse("please Login First before checkout")


def Tracker(request):
	if request.method=="POST":
		print("insdie Tracker++++++++++++++++++++++++++++++++++++++++",json.loads(request.body))
		data = json.loads(request.body)
		try:
			orderid=data['orderId']
		except Exception as e:
			print(e)
		orderemail=OrderTracker.objects.filter(orderid=orderid)
		orderdetail=CheckoutOrder.objects.filter(orderid=orderid)
		prodid=[]
		for i in orderdetail:
			data=ast.literal_eval(i.products)
			for i in data.keys():
				prodid.append(i)

		allprods=Product.objects.filter(product_id__in=prodid)
		prodname=[]
		for i in allprods:
			prodname.append(i.prod_name)






		if len(orderemail) > 0:
			mylist=[orderemail[0].status,orderdetail[0].total,prodname]
			return HttpResponse(json.dumps(mylist))
		else:
			return HttpResponse("Sorry We Unable To Find Your Order")
			



	return render(request,'tracker.html')


def ListviewInOrderid(request):
	orderedprod=CheckoutOrder.objects.filter(email=request.user.email)
	tmpJson = serializers.serialize("json",orderedprod)
	tmpObj = json.loads(tmpJson)
	print(tmpObj)

	return HttpResponse(json.dumps(tmpObj))



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
	


