from django.conf.urls import patterns, include, url
from ostokset import views
from markiar import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import ostokset
admin.autodiscover()
from django.views.static import * 
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
 #    url(r'^$', 'ostokset.views.lista_d2', name='listaus'),
    # url(r'^markiar/', include('markiar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^$', 'kauppa.views.index'),
     url(r'^admin/', include(admin.site.urls)),
     url(r'ostokset/','ostokset.views.lista_d2'),
     url(r'^lisaa/','ostokset.views.lisaa'),
     url(r'kauppa/','kauppa.views.index'),
     url(r'^kori/','kauppa.views.kori'),
     url(r'^poista/','ostokset.views.poista_ostos'),
     url(r'^kello/$','kello.views.kello'),
     url(r'^kello/login/$','kello.views.login'),
     url(r'^kello/logout/$','kello.views.logout'),
     url(r'^api/kello/$','kello.views.api_kello'),
        
     
)

urlpatterns += patterns('',
        (r'^ostokset/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    )