from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
# def home(request):
#     return render(request,'home.html')
def about(request):
    return render(request,'AboutAs.html')

    # return HttpResponse("this is about page")


def services(request):
    pass
    # return HttpResponse("this is services page")

def VideoRecord(request):
    return render(request,'videoRecord.html')
def VoiceRecord(request):
    return render(request,'audioRecord.html')
def ClickPhotos(request):
    return render(request,'photoClick.html')


def contact(request):
    return render(request,'contact.html')
