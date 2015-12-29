from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import json



def index(request):



    return render(request,'index.html')


