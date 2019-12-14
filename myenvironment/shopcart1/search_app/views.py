from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResult(request):
