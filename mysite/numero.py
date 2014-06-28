#from django.template.loader import get_template #Carga de Plantillas
#from django.template import Template, Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response

#print "Estas en numero.py"
class Numero:
    def __init__(self, numero, par):
        self.numero = numero
        self.par = par
 
    def __str__(self):
        return "numero=%d par=%s " % (self.numero, self.par)

listaNumeros=[]
numero = 101

def par(numero):
    for i in range(1, numero):
        if (i%2) == 0:
        	#Definimos el identificador como "1" para PAR
        	num = Numero(i, 1)
        	listaNumeros.append(num)
        else:
        	#Definimos el identificador como "0" para IMPAR
            num = Numero(i, 0)
            listaNumeros.append(num)

def imprimirLista():
    for i in range(0,len(listaNumeros)):
        print str(listaNumeros[i])

def imprimirLista2():
    for i in listaNumeros:
        print i.numero, i.par
    	print i

'''def mostrarNoPares(request):
    fp = open('/media/OS/Users/USUARIO/Mis documentos/JULIAN/ATHOM_HOUSE/DJANGO/Proyectos/mysite/mysite/templates/paresPlantilla.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'listaNumeros': listaNumeros}))
    return HttpResponse(html)'''

#Manera mas facil de hacer el response con render_to_response()
#Para ello tuvimos que modificar el TEMPLATE_DIRS en setting.py
#E importar: from django.shortcuts import render_to_response
#No hay necesidad de importar emplate, Context, o HttpResponse
def mostrarNoPares(request):
    return render_to_response('paresPlantilla.html', {'listaNumeros': listaNumeros})

par(numero)
imprimirLista2()