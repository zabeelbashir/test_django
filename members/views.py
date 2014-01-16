from django.shortcuts import render
from models import Member
from django.http import HttpResponse
from django.shortcuts import render_to_response
from form import NameForm
# Create your views here.
values = {"members": Member.objects.all()}

def myFirstView(request):
    return HttpResponse("Hello world!")

def membersList(request):
    variables = {"members": Member.objects.all() }
    return render_to_response("members/list.html",variables)
#    result = ""
#    for m in Member.objects.all():
#        result += "%s --- study: %s<br />" %(m,m.study)
#    return HttpResponse(result)
def formView(request):
    f = NameForm(request.GET)
    if f.is_valid():
        return render_to_response("members/welcome.html", {"name": f.getName()})
    return render_to_response("members/form.html", {"form": f})