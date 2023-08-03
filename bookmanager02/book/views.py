from django.http import HttpResponse
from django.shortcuts import render
import json as jsonn


def create_book(request):
    return HttpResponse('create')


def shop(request, city_id, shop_id):
    print(request.GET)
    print(request.GET.getlist('order'))
    print(request.GET.get('order'))
    return HttpResponse(city_id + shop_id)


def register(request):
    data = request.POST
    print(data)
    print(data.get('username'))
    return HttpResponse('OK')


def json(request):
    print(request.body, ' === bytes 类型')
    print(request.body.decode(), ' === json形式的字符串')
    # import json as jsonn
    print(jsonn.loads(request.body.decode()), ' === json形式的字符串可以转换为字典')
    return HttpResponse('OK')
