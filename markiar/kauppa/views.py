from django.http import HttpResponseBadRequest,Http404, HttpResponse
from django.core.context_processors import csrf
from django.template import Context,loader, RequestContext
from django.shortcuts import render_to_response, redirect
from kauppa.models import Product

def index(request):
    
    return render_to_response('index.html',
                              {'products': Product.objects.all()}, context_instance=RequestContext(request)) # Create your views here.
def kori(request):
    if request.method == 'POST':
        try:
            idk = int(request.POST['id'])
            p = Product.objects.get(pk=idk)
            ps = request.session.get('products', [])
            ps.append(p)
            request.session['products'] = ps
            return redirect('kauppa.views.index')
        except (ValueError, KeyError, Product.DoesNotExist):
            return HttpResponseBadRequest()
    elif request.method == 'GET':
            ps = request.session.get('products', [])
            sum = reduce(lambda x, y: x + y.price, ps, 0)
            return render_to_response('kori.html',
                                     {'products': ps,
                                      'total': sum})
    else:
        raise Http404