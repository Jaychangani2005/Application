from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def Index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'Aboutus.html')

def Services(request):
    return HttpResponse("this is services page")

def VideoRecord(request):
    return render(request,'videoRecord.html')

def AudioRecord(request):
    return render(request,'audioRecord.html')

def ClickPhotos(request):
    return render(request,'photoClick.html')

def Contact(request):
    return render(request,'contact.html')

def Payment(request):
    return render(request,'payment.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_page.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page upon successful login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
