from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def pricing(request):
    return render(request,'pricing.html')
def services(request):
    return render(request,'services.html')

# Create your views here.
