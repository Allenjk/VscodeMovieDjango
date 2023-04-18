from django.shortcuts import render,HttpResponse

# Create your views here.
def server(request):
    return HttpResponse("server")