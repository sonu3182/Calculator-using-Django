from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


def add(request):
    if request.method=='POST':
        k=int(request.POST["num3"])
        if k==1:
            a=int(request.POST["num1"])
            b=int(request.POST["num2"])
            res = a + b
            desc=f'Addition of {a} and {b} is '
            return render(request,'home.html',{'output':res,'remain':desc})
        if k==2:
            a=int(request.POST["num1"])
            b=int(request.POST["num2"])
            res = a - b
            desc=f'Substraction of {a} and {b} is '
            return render(request,'home.html',{'output':res,'remain':desc})
        if k==3:
            a=int(request.POST["num1"])
            b=int(request.POST["num2"])
            res = a * b
            desc=f'Multiplication of {a} and {b} is '
            return render(request,'home.html',{'output':res,'remain':desc})
        if k==4:
            a=int(request.POST["num1"])
            b=int(request.POST["num2"])
            res = a / b
            desc=f'Division of {a} and {b} is '
            return render(request,'home.html',{'output':res,'remain':desc})
    else:
        return HttpResponse("your choice is wrong please choice correct option")