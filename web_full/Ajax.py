# coding=utf-8
from django.http import HttpResponse
# from web_full import SSH_connection
from web_full import send_email
import json


def test(request):
    print ('test')
    return HttpResponse()


def Send_message(request):
    d_respuesta = {}
    l_result = []
    form = request.POST
    metadata = request.META
    email = form.get('email', "anonymous")
    in_message = form.get('in_message', None)
    message = 'Subject:{}\n\n{}'.format(email, in_message)
    send_email.Send_Email().send(message)
    # o_exec = SSH_connection.Execute_command()

    for v, meta in metadata.items():
        result = (str(v) + '==>' + str(meta))
        l_result.append(result)
        # d_respuesta['result'] = str(v) + ':' + str(meta)

    if request:
        # result = o_exec.execute(l_result)
        d_respuesta['result'] = ('Email enviado con exito!')
        # d_respuesta['result'] = result
    else:
        d_respuesta['result'] = ('Error')

    return HttpResponse(json.dumps(
                    d_respuesta), content_type='application/json')
