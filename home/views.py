from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': "this is sent",
        'variable2': "you are great"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')