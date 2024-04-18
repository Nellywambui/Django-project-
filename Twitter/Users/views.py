from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def Aboutus(request):
    return render(request,'Aboutus.html')
def Contact(request):
    return render(request,'Contact.html')
def Login(request):
    return render(request,'Login.html')
def Register(request):
    return render(request,'Register.html')