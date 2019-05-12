import smtplib
import ssl


class Send_Email():
    """docstring for ."""

    def send(self, message):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        receiver_email = "hashcrackhelp@gmail.com"
        password = "P454h4shcr4ck"  # Enter receiver address
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(receiver_email, password)
            server.sendmail(receiver_email, receiver_email, message)
