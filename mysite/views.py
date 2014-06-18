from django.http import HttpResponse

def hello(request): #request: Solicitud por convencion y es una instancia de a clase django.http.HttpRequest
    return HttpResponse("Hello world") #No hacemos nada con el request, pero siempre debe de llevar un parametro