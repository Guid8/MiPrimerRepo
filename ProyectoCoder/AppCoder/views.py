from django.shortcuts import render
from AppCoder.models import Abuelo
from AppCoder.models import Primo
from AppCoder.models import Tio
from django.http import HttpResponse





def abuelo(self):

    abuelo=Abuelo (nombre="Lucas Choque", edad=78)
    abuelo.save()
    texto= f"Familiar creado:  {abuelo.nombre} {abuelo.edad}"
    return HttpResponse(texto)

def primo(self):

    primo=Primo  (nombre="Euge Pidal", edad=22)
    primo.save()
    texto= f"Familiar creado:  {primo.nombre} {primo.edad}"
    return HttpResponse(texto)

def tio(self):

    tio=Tio  (nombre= "Diego Ocampo", edad= 46)
    tio.save()
    texto= f"Familia creado:  {tio.nombre} {tio.edad}"
    return HttpResponse(texto)   