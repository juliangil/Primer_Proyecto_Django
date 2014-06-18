from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^hello/', 'mysite.views.hello'), 
    url(r'^$', 'mysite.views.hello'), 
	'''r: La r le dice a Python que la cadena es una "cadena de texto" - su contenido no debera interpretar barras invertidas

		^ y $:
		El patron incluye un acento circunflejo (^) y un signo de dolar ($). Estos son caracteres de expresiones regulares 
		que tienen un significado especial: el simbolo de intercalacion significa "requiere que el patron coincide con el 
		inicio de la cadena", y el simbolo del dolar significa "requiere que el patron coincide con el final de la cadena.
	'''
]