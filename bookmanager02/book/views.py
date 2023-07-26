from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def create_book(request):
    return HttpResponse('create')


def shop(request, city_id, shop_id):
    query_params = request.GET
    print(query_params)
    print(query_params.getlist('order'))
    return HttpResponse(city_id + shop_id)
