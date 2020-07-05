from django.http import HttpResponse
import time

def fecha(request): # primera vista

    print(time.strftime("%H:%M:%S")) #Formato de 24 horas
    print (time.strftime("%d/%m/%y"))
    return 