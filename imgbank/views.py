from django.shortcuts import render
from django.views.generic import ListView
from .models import Imgbank

# Create your views here.

class ImgBankList(ListView):
   model = Imgbank
   template_name = 'imgbank/imgbank_list.html'