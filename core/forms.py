from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class ReviewForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':  "Drop Your Review",
        'class': "form-control",
        'row': 16,
        'style': "resize:none;"
    }))



class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
 
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    state = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    country = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    default = forms.BooleanField(required=False)


class CouponForm(forms.Form):
    code = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    subject = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(max_length=300, required=True, widget=forms.Textarea(attrs={
         'style': 'resize:none;',
        'rows': '25',
        'class': 'form-control',
        'placeholder': 'Message',
      
    }))



class NewsletterForm(forms.Form):
    email = forms.CharField(max_length=100, required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Email Address'
    }))