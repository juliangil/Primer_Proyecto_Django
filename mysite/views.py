#from django.template.loader import get_template #Carga de Plantillas
#from django.template import Template, Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response
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
'''def current_datetime(request):
    now = datetime.datetime.now()
    #Manera simple de usar Templates desde un archivo#
    fp = open('mytemplate.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''

#Manera mas facil de hacer el response con render_to_response()
#Para ello tuvimos que modificar el TEMPLATE_DIRS en setting.py
#E importar: from django.shortcuts import render_to_response
#No hay necesidad de importar emplate, Context, o HttpResponse
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)   
