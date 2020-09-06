from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib import messages
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


class ShopView(TemplateView):
    template_name = 'shop-sidebar.html'

class AboutView(TemplateView):
    template_name = 'about.html'



class DetailView(TemplateView):
    template_name = 'product-single.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'



class CartView(TemplateView):
    template_name = 'cart.html'


class FaqView(TemplateView):
    template_name = 'faq.html'



class ContactView(TemplateView):
    template_name = 'contact.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class SignupView(TemplateView):
    template_name = 'signin.html'



class ForgotView(TemplateView):
    template_name = 'forget-password.html'


class BlogView(TemplateView):
    template_name = 'blog-grid.html'


class BlogDetailView(TemplateView):
    template_name = 'blog-single.html'


class ConfirmView(TemplateView):
    template_name = 'confirmation.html'



class PaystackView(TemplateView):
    template_name =   "purchase-confirmation.html"

class OrderView(TemplateView):
    template_name =   "order.html"

class DashboardView(TemplateView):
    template_name =   "dashboard.html"

def click(request):
    messa
    return render(request, 'contact.html')


# class PricingView(TemplateView):
#     template_name =   "pricing.html"

class AddressView(TemplateView):
    template_name =   "address.html"



def handler404(request, exception):
    return render(request, '404.html')