from django.urls import path
from .views import ImgBankList

imgbank_patterns = ([
    path('', ImgBankList.as_view(), name='imgbank'),    
], 'imgbank')