from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def uploadimage(request):
    
    return render(request, 'uploadimage.html')
    
