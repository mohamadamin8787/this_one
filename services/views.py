from django.shortcuts import render
from .models import *

def services(request):
    if request.GET.get('category') is not None:
        all = Services.objects.filter(category__title = request.GET.get('category'))
    
    elif request.GET.get('search'):
        all = Services.objects.filter(description__contains = request.GET.get('search'))

    else:
        all = Services.objects.filter(status = True)
    
    context = {
        'service' : all
    }
    
    return render(request,'services.html',context=context)


def services_details(request):
    
    if request.GET.get(id) is not None:
        all = Services.objects.get(id=id)
        all.counted_viwe += 1
        all.save()
        
    else:
        all = Services.objects.filter(status = True)

    context = {
        'detail' : all
    }

    return render(request,'service-details.html', context=context)


def get_a_quote(request):
    return render(request,'get-a-quote.html')
