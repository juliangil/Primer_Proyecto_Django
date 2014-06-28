from django.template import Template, Context
from django.http import HttpResponse

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

def mostrarNoPares(request):
    fp = open('/media/OS/Users/USUARIO/Mis documentos/JULIAN/ATHOM_HOUSE/DJANGO/Proyectos/mysite/mysite/paresPlantilla.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'listaNumeros': listaNumeros}))
    return HttpResponse(html)

par(numero)
imprimirLista2()