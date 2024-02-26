from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def inner(request):
    return render(request,'sample-inner-page.html')