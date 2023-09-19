from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import people


# Create your views here.
# def demo(request):
#     return render(request,"add.html")
# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("i am contact")
#
#
# def addition(request):
#     number1=int(request.GET['num1'])
#     number2=int(request.GET['num2'])
#     s=number1+number2
#     return render(request,"result.html",{"dis":s})

def demo(request):
    abc=place.objects.all()
    sup=people.objects.all()
    return render(request,"index.html",{'result':abc,'re':sup})




