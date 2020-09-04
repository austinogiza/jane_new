from django.urls import path, include
from . import views

app_name ="jane"


urlpatterns = [

    path('', views.HomeView.as_view(), name="home" ),
    path('shop/', views.ShopView.as_view(), name="shop" ),
    path('about-us/', views.AboutView.as_view(), name="about" ),
    path('detail/', views.DetailView.as_view(), name="detail" ),
    path('cart/', views.CartView.as_view(), name="cart" ),
    path('checkout/', views.CheckoutView.as_view(), name="checkout" ),
    
    

]

