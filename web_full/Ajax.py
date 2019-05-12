# coding=utf-8
from django.http import HttpResponse
import json


def test(request):
    print ('test')
    return HttpResponse()


def Paso_de_datos(request):
    d_respuesta = {}
    form = request.POST
    email = form.get('email', None)
    print (email)

    if request:
        d_respuesta['result'] = ('Email registrado')
    else:
        d_respuesta['result'] = ('Error')

    return HttpResponse(json.dumps(
                    d_respuesta), content_type='application/json')
