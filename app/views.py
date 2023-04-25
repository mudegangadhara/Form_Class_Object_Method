from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def Student(request):
    SFD=StudentForms()
    d={'SFD':SFD}
    if request.method == 'POST':
        SDO=StudentForms(request.POST)
        if SDO.is_valid():
            return HttpResponse(str(SDO.cleaned_data))
        else:
            return HttpResponse('data is not valid')
    return render(request,'Student.html',d)