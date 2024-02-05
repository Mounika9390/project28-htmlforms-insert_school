from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def htmlforms(request):

    if request.method=='POST':
        UserName=request.POST=['un']

        return HttpResponse(UserName)

    return render(request,'htmlforms.html')
def insert_school(request):
    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST['sl']
        sp=request.POST['sp']
        
        so=School.objects.get_or_create(sname=sn,slocation=sl,sprincipal=sp)[0]
        so.save()
        return HttpResponse('school is inserted')
    return render(request,'insert_school.html')