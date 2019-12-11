from django.shortcuts import render,HttpResponse

def home(request):
    homePage ="HOME PAGE"
    return HttpResponse(homePage)
