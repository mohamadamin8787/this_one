from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
    path('',services,name= 'service'),
    path('detail/',services_details,name= 'detail'),
    path('get_a_quot',get_a_quote,name= 'get_a_quot')
]
