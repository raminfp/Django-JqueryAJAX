import json

from django.http.response import HttpResponse


def CallAjax(request):
    if request.POST:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        data = {'fname': fname, 'lname': lname}
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponse('Request is not POST')
