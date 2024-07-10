from django import forms


class ContactUsForm(forms.Form):
    subject = forms.CharField(max_length=50) 
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=50)
    # message = forms.Textarea()

