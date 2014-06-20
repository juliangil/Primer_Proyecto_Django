from django.http import HttpResponse
import datetime

def hello(request): #request: Solicitud por convencion y es una instancia de a clase django.http.HttpRequest
    return HttpResponse("Hello world") #No hacemos nada con el request, pero siempre debe de llevar un parametro

#FUNCION QUE RETORNA LA HORA DE NUESTRO SERVIDOR (CODIGO .PY)
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)