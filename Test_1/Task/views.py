from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def RandCodeAutho(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    code = ''
    if num_visits > 1:
        request.session.flush()
    else:
        for i in range(4):
            code += str(randint(0, 9))
    context = {'result': code,
               'num_visits': num_visits}
    return render(request, 'index.html', context)


def RanCode(request):
    code = ''
    for i in range(4):
        code += str(randint(0, 9))
    context = {'result': code}
    return render(request, 'main.html', context)
