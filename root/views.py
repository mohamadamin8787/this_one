from django.shortcuts import render , redirect
from .forms import ContactUsForm 
from .models import Services
from root.models import ContactUs
from django.contrib import messages
def index(request):
    context = {
        'service' : Services.objects.filter(status =True)
    }

    return render(request,'index.html', context=context)



def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            new_content = ContactUs()
            new_content.name = name
            new_content.email = email
            new_content.message = message
            new_content.subject = subject
            new_content.save()
            messages.add_message(request, messages.SUCCESS,'your message was sucsses')
            return redirect('root:contact')
        else:
            messages.add_message(request, messages.ERROR,'your message was not sucsses')
            return redirect('root:contact')
        
    else:
        return render(request,'contact.html')
         


   
 
def about(request):
    return render(request,'about.html')
