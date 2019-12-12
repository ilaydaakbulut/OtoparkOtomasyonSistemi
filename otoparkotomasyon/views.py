from django.shortcuts import render,HttpResponse

def home(request):
    homePage ="HOME PAGE"
    return HttpResponse(homePage)

def exit(request):
	outMessage = "Güle Güle :)"
	return HttpResponse(outMessage) 

