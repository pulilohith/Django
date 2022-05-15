from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotAllowed
import datetime
from django.views.decorators.http import require_http_methods
from django.template import loader


def hello(request):
    return HttpResponse("<h1>This is a Home Page</h1>")


@require_http_methods(["GET"])
def super_man(request):
    now = datetime.datetime.now()
    val = "<h1> The Time you logged into website %s </h1>" % now
    return HttpResponse(val)


def first_template(request):
    name = {'name': 'Django World'}
    return HttpResponse(loader.get_template('index.html').render(name))
# Create your views here.
