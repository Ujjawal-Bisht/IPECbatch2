from django.shortcuts import render
from .models import Students
# Create your views here.
def getalldata(request):
    data = Students.objects.all()
    return render(request, "viewall.html", {'data': data})