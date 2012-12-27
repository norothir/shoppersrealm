from django.http import HttpResponse, HttpResponseBadRequest, Http404
from ostokset.models import Ostos
from django.shortcuts import render_to_response, render, redirect
from django.core.context_processors import csrf
from django.template import Context,loader, RequestContext
from ostokset.tables import OstosTable


def getostoksetview(request):
    return HttpResponse("mikan yritys nro n")

#def listaus(request):
#    variables = {"ostokset": Ostos.objects.all() }
#    return render_to_response("ostokset.html",variables)

def lisaa(request):
    if 'item' in request.POST:
        itemName = request.POST['item']
    
    if 'maara' in request.POST:
        luku = request.POST['maara']
        maara = int(luku)
    
    if 'category' in request.POST:
        cat = request.POST['category']
     
    tavara = Ostos(item=itemName,amount=luku,category=cat,buyer='mina',active='1',listid='0')
    tavara.save()    
    return render(request,'ostokset.html', {"ostokset": Ostos.objects.all() }, context_instance=RequestContext(request))   

def lista_d2(request):
    return render(request,'ostokset.html', {"ostokset": Ostos.objects.all() }, context_instance=RequestContext(request))

def poista_ostos(request):
     
        if request.method == 'POST':
            try:
                idk = int(request.POST['id'])
                poistaTavaraID=idk
                tavara = Ostos.objects.get(id=poistaTavaraID)
                tavara.delete() 
                return redirect('ostokset.views.lista_d2')
            except (ValueError, KeyError, Ostos.DoesNotExist):
                return HttpResponseBadRequest()
        elif request.method == 'GET':
                ps = request.session.get('products', [])
                sum = reduce(lambda x, y: x + y.price, ps, 0)
                return render_to_response('kori.html',
                                         {'products': ps,
                                          'total': sum})
        else:
             raise Http404 
    
    