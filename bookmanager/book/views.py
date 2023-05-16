from django.shortcuts import render


def index(request):
    """
    所谓的视图 其实就是python函数
    视图函数有2个要求：
        1. 视图函数的第一个参数就是接收请求，这个请求就是从 django.http 导入的 HttpRequest 类的对象
        2. 必须返回一个响应
    # render(请求，模板名字，上下文?)
    """
    context = {
        'name': '动态值'
    }
    return render(request, 'book/index.html', context)





















