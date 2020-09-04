from django.shortcuts import render
from django.views.generic import TemplateView

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

def handler404(request, exception):
    return render(request, '404.html')