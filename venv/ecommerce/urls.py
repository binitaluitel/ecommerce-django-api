
from django.urls import path, include
from.views import *
urlpatterns = [
    
     path('',index),
     path('login/',SignIn),
     path('register/',register),
     path('shop/',shop),
     path('product/<int:id>',productDetails),
     path ('cart/',cart),
     path ('logout/',user_logout),
     path ('add-to-cart/<int:product_id>',addToCart),
     path('remove-from-cart/<int:cart_id>',removeFromCart),
     path('checkout/',checkout),
     path('orders/', orders),
    path('add-to-wishlist/<int:product_id>',addToWishlist),
    path('wishlist/',wishlist),
    path('remove-from-wishlist/<int:wishlist_id>',remove_from_wishlist),
    path('profile/',profile),

    

]