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
    path('faq/', views.FaqView.as_view(), name="faq" ),
       path('contact/', views.ContactView.as_view(), name="contact" ),
        path('login/', views.LoginView.as_view(), name="login" ),
        path('signup/', views.SignupView.as_view(), name="signup" ),
            path('forgot-password/', views.ForgotView.as_view(), name="forgot" ),
         path('blog/', views.BlogView.as_view(), name="blog" ),
       path('blog/detail/', views.BlogDetailView.as_view(), name="blog-detail" ),
              path('payment/success/', views.ConfirmView.as_view(), name="pay" ),
                 path('payment/receipt/', views.PaystackView.as_view(), name="receipt" ),
                 path('dashboard/', views.DashboardView.as_view(), name="dashboard" ),
       path('dashboard/orders/', views.OrderView.as_view(), name="order" ),

      path('dashboard/address/', views.AddressView.as_view(), name="address" ),
    #    path('pricing/', views.PricingView.as_view(), name="pricing" ),



       

       
                 


       
        





        

       
    

    
    
    

]

