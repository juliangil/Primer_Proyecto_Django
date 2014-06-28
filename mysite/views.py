from django.template import Template, Context
from django.http import HttpResponse
import datetime
print "Estas dentro de views.py"

def hello(request): #request: Solicitud por convencion y es una instancia de a clase django.http.HttpRequest
    return HttpResponse("Hello world") #No hacemos nada con el request, pero siempre debe de llevar un parametro

#FUNCION QUE RETORNA LA HORA DE NUESTRO SERVIDOR (CODIGO .PY)
'''def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{current_date}}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''
def current_datetime(request):
    now = datetime.datetime.now()
    #Manera simple de usar Templates desde un archivo#
    fp = open('/media/OS/Users/USUARIO/Mis documentos/JULIAN/ATHOM_HOUSE/DJANGO/Proyectos/mysite/mysite/mytemplate.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)   
