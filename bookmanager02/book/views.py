from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def create_book(request):
    return HttpResponse('create')


def shop(request, city_id, shop_id):
    print(city_id, shop_id)
    return HttpResponse(city_id + shop_id)
