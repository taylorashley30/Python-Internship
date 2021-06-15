from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

def myform(request):
    return render(request,'myform.html')

def process(request):
    print('Welcome')
    print(request.method)
    print(request.POST)
    a=str(request.POST['Fname'])
    b=str(request.POST['Mname'])
    c=str(request.POST['Lname'])
    d=str(request.POST['Email'])
    e=int(request.POST['Pnumber'])
    print(a,b,c,d,e)
    return render(request,'ans.html', {'mya':a,'myb':b,'myc':c, 'myd':d,'mye':e})
 
    