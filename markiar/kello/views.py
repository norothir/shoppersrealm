from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib import auth
from datetime import datetime
from django.core.context_processors import csrf

import base64



def kello(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render_to_response('kello.html',context_instance = RequestContext(request))
        else:
            return redirect('kello.views.login')
    else:
        return HttpResponseBadRequest()
    
def login(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'GET':
        return render_to_response('login.html',c)
    elif request.method == 'POST':
        try:
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user is None:
                c = {}
                c.update(csrf(request))
                x = RequestContext()
                return render_to_response('login.html',
                                         {'error': 'Invalid password','username':request.POST['username']})
            else:
                auth.login(request, user)
                x = RequestContext('kello.views.kello')
                return redirect('kello.views.kello')
        except KeyError:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()      
      
def logout(request):
    auth.logout(request)
    return redirect('kello.views.kello')

def challenge():
    response = HttpResponse(status=401)
    response['WWW-Authenticate'] = 'Basic realm="testi"'
    return response

def api_kello(request):
    if authorized(request):
        return HttpResponse(datetime.now().strftime("%H:%M:%S"), content_type="text/plain")
    else:
        return challenge()
   
def authorized(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        try:
            (type, b64) = request.META['HTTP_AUTHORIZATION'].split()
            if type.lower() == "basic":
                (uname, passwd) = base64.b64decode(b64).split(':')
                user = auth.authenticate(username=uname,password=passwd)
                if user is not None:
                    auth.login(request, user)
                    request.user = user
                    return True
                else:
                    return False
        except ValueError:
            return False
    else:
        return False   