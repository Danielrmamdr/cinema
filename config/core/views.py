from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'core/base.html')

def SignUp(request):
    return render(request, 'core/SignUp.html')

def Signin(request):
    return render(request, 'core/SignIn.html')