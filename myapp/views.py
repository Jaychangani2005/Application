from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm

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

def Success_page(request):
    return render(request,'success_page.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  
    else:
        form = ContactForm()
    
    return render(request, 'success_page.html', {'form': form})