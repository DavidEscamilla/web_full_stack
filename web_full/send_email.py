# -*- coding: utf-8 -*-
import smtplib
import ssl
import paramiko


class Send_Email():
    """Metodo para recibir preguntas
       en el correo electronico.
    """

    def send(self, message):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        receiver_email = "hashcrackhelp@gmail.com"  # Enter receiver address
        password = "P454h4shcr4ck"
        message_2 = str.encode(message, "utf-8")  # codificar en UTF-8
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(receiver_email, password)
            server.sendmail(receiver_email, receiver_email, message_2)
