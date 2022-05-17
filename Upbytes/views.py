from django.shortcuts import render
from Upbytes.functions.functions import handle_file_upload
from django.http import HttpResponse, HttpResponseNotAllowed
import datetime
from django.views.decorators.http import require_http_methods
from django.template import loader
from Upbytes.forms import EmpForm, StudForm


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

def auto_template(request):
    if request.method == 'POST':
        emp = EmpForm(request.POST, request.FILE)
        if emp.is_valid():
            handle_file_upload(request.FILE['file'])
            return HttpResponse("Details Saved Successfully!")
    else:
        emp = EmpForm()
    return render(request, "index.html", {'form': emp, 'name': 'Django World'})


def stud_form(request):
    if request.method == 'POST':
        stu = StudForm(request.POST, request.FILES)
        if stu.is_valid():
            # print(request.POST)
            handle_file_upload(request.FILES['file_upload'])
            return HttpResponse('Details Saved Successfully')
    else:
        stu = StudForm()
    return render(request, "Student.html", {'form': stu, 'name': 'Junior Django'})
