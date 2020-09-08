from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Item, 
    Wishlist, 
    Reviews,
    OrderItem,
    Order,
    Address,
    Payment,
    Coupon,
    Refund,
    UserProfile,
    Category,
    HomepageBanner,
    HomesideBanner,
    ShoptopBanner,
    ShopbottomBanner,
  
    Contact,
    Slider,
    Newsletter
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm, CheckoutForm, RefundForm, CouponForm, ContactForm, NewsletterForm
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from .filters import ProductFilter
# Create your views here.

class HomeView(ListView):
    model = Item
    context_object_name ='product'
    template_name = 'index.html'

    def get_queryset(self):
        qs = Item.objects.order_by('-pub_date')
        return qs


class ShopView(ListView):
    model = Item
    context_object_name = 'product'
    paginate_by = 18
    template_name = 'shop-sidebar.html'

    def get_queryset(self):
        qs = Item.objects.order_by('-pub_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        context.update({
            'filter': ProductFilter(self.request.GET, queryset=self.get_queryset())
          
        })
        return context
    

        

class AboutView(TemplateView):
    template_name = 'about.html'




class DetailView(DetailView):
    model = Item
    context_object_name = 'product'
    template_name = 'product-single.html'

    
    def post(self, request, *args, **kwargs):
        form = ReviewForm(self.request.POST)

        if form.is_valid():
            review = form.cleaned_data.get('review')
            user = self.request.user
            item = self.get_object()

            review = Reviews(
                user=user,
                item=item,
                review=review
            )
            review.save()
            messages.success(self.request,'Yay, you are amazing for the review')
            return redirect('core:details', slug=item.slug)
        messages.error(self.request,'Oh no, you didn\'t any review')
        return redirect('core:details', slug=self.get_object().slug)

    def get_object(self, **kwargs):
        qs = super().get_object(**kwargs)
        return qs
    

  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
                'form': ReviewForm(),
           
            }) 
        return context


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout.html'
    
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
     
            context = {
                'form': form,
                'couponform': CouponForm(),
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("core:checkout")

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context.update({
            'form': CheckoutForm()
        })
        return context

    def post(self,request, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        order = Order.objects.get(user=self.request.user, ordered=False)

        if form.is_valid():
            user = self.request.user
            address = form.cleaned_data.get('address')
            country  = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            state = form.cleaned_data.get('state')
            phone = form.cleaned_data.get('phone')
            default = form.cleaned_data.get(
                    'use_default_billing')
 
            if default:
                checkout = Address(
                user=user,
                address = address,
                country = country,
                state=state,
                zip=zip,
                phone=phone,
                default=True,
            ) 
                checkout.save()
                order.address = checkout
                order.save()
                
            else:
                checkout = Address(
                user=user,
                address = address,
                country = country,
                state=state,
                zip=zip,
                phone=phone,
       
            ) 
                checkout.save()
                order.address = checkout
                order.save()
            return redirect('core:payment')
        messages.error(self.request, 'You didn\'t enter any address')
        return redirect('core:checkout')
    

  





class CartView(TemplateView):
    template_name = 'cart.html'

    def get(self, *args, **kwargs):
        try:
            shoptop = ShoptopBanner.objects.all()[:2]
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order,
          
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")


class FaqView(TemplateView):
    template_name = 'faq.html'



class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': ContactForm()
        })
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(self.request.POST or None)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            contact = Contact(
                name=name,
                email=email,
                subject=subject,
                message=message

            )
            contact.save()
            return redirect('core:contact-success')


class ContactSuccessView(TemplateView):
    template_name = "contact-success.html"



class LoginView(TemplateView):
    template_name = 'login.html'


class SignupView(TemplateView):
    template_name = 'signin.html'



class ForgotView(TemplateView):
    template_name = 'forget-password.html'





class ConfirmView(TemplateView):
    template_name = 'confirmation.html'



class PaystackView(TemplateView):
    template_name =   "purchase-confirmation.html"

    def get(self, request, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)

        user = self.request.user

        email = self.request.user.email
        amount = order.get_total()

        context = {
            'order':order,
            "email":email,
            "amount":amount
        }

        if order.address:
            return render(self.request,  "purchase-confirmation.html", context)
        else:
            messages.error(self.request, "You have no billing address")
            return redirect('core:checkout')    

        



class OrderView(LoginRequiredMixin, TemplateView):
    template_name =   "order.html"

    
    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context.update({
            'order': Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context

class OrderDetailView(LoginRequiredMixin,DetailView):
    queryset = Order.objects.all()
    context_object_name ='order'
    template_name = "order_details.html"



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name =   "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context.update({
            'wishlist': Wishlist.objects.filter(user=self.request.user)
        })
        return context

    

def click(request):
    
    return render(request, 'contact.html')


# class PricingView(TemplateView):
#     template_name =   "pricing.html"

class AddressView(LoginRequiredMixin, TemplateView):
    template_name =   "address.html"

    def get_context_data(self, **kwargs):
        context = super(AddressView, self).get_context_data(**kwargs)
        context.update({
            'order': Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context



def handler404(request, exception):
    return render(request, '404.html')

@login_required
def wishlist_home(request, slug):
    item = get_object_or_404(Item, slug=slug)
    wish_qs = Wishlist.objects.filter(user=request.user, item=item)
    if wish_qs.exists():
        wish_qs[0].delete()
        messages.error(request, "You have removed an item to your wishlist")
        return redirect('core:home')
    Wishlist.objects.create(user=request.user, item=item)
    messages.success(request, "You have added an item to your wishlist")
    return redirect('core:home')



@login_required
def wishlist(request, slug):
    item = get_object_or_404(Item, slug=slug)
    wish_qs = Wishlist.objects.filter(user=request.user, item=item)
    if wish_qs.exists():
        wish_qs[0].delete()
        messages.error(request, "You have removed an item to your wishlist")
        return redirect('core:shop')
    Wishlist.objects.create(user=request.user, item=item)
    messages.success(request, "You have added an item to your wishlist")
    return redirect('core:shop')

     

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:cart")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:cart")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:cart")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:details", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:details", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:details", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:details", slug=slug)


def newsletter(request):
    query = request.POST.get('email')
    if query:
        email = query
        newsletter = Newsletter(
            email=email
        )
        newsletter.save()
        messages.success(request, 'You have signup for the newsletter')
        return reverse_lazy('core:home')
    messages.error(request, 'You haven\'t for the newsletter')
    return reverse_lazy('core:home')

    return render(request, 'newsletter-success.html')

    