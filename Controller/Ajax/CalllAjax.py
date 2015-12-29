from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import json



def CallAjax(request):

     if request.POST:

        fname  = request.POST.get('fname')
        lname  = request.POST.get('lname')
        data = {'fname':fname,'lname':lname}
        print data

        return HttpResponse(json.dumps(data), content_type="application/json")

     else:

         return HttpResponse('Request is not POST')
