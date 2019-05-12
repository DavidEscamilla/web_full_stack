# coding=utf-8
from django.http import HttpResponse
from . import send_email
import json


def test(request):
    print ('test')
    return HttpResponse()


def Send_message(request):
    d_respuesta = {}
    form = request.POST
    email = form.get('email', "anonymous")
    in_message = form.get('in_message', None)
    message = 'Subject:{}\n\n{}'.format(email, in_message)
    print (message)
    send_email.Send_Email().send(message)

    if request:
        d_respuesta['result'] = ('Email registrado')
    else:
        d_respuesta['result'] = ('Error')

    return HttpResponse(json.dumps(
                    d_respuesta), content_type='application/json')
