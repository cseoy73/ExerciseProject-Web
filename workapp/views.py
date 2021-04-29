from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def exercise1(request):
    return HttpResponse("<h1>안녕하세요? 최서영이 만든 첫 장고 웹페이지입니다.</h1>")
# Create your views here.

def exercise2(request):
    if request.method == 'POST':
        na = request.POST['name']
        opi = request.POST['opinion']
        context = {'na' : na, 'opi' : opi}
    else:
        context = None
    return render(request, 'exercise2.html', context)

def product1(request):
    template = loader.get_template('product1.html')
    context = {'pid' : ['p001','p002','p003','p004','p005','p006','p007','p008','p009','p010']}
    return HttpResponse(template.render(context, request))

def basket1(request, pid):
    context = {
        'pid': pid,
    }
    return render(request, 'basket1.html', context)