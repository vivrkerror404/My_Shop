from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home),
    path('contact/',views.MyContact),
    path("product/<prod_id>", views.product),
    path('about/',views.About),
    path('checkout/',views.Checkout),
    path('tracker/',views.Tracker),
    path('sessionstore/',views.Sessionstore),
    path('myproducts/',views.ProdInCart),
    path('mywishlist/',views.Wishlist),
    path('RE/',views.RE),
    path('tc/',views.tc),
    path('policy/',views.policy)


]