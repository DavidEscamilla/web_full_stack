import paramiko


class Execute_command():
    """Metodo para ejecutar comandos por ssh"""
    def execute(self, l_metadata):
        respuesta = ''
        o_ssh = paramiko.SSHClient()
        l_result = []
        o_ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        o_ssh.connect(
            '009ut7y00.ddnsking.com',
            username='eljeros',
            password='1234'
        )
        ssh_stdin, ssh_stdout, ssh_stderr = o_ssh.exec_command(
            'echo ' + str(l_metadata) + '>metadatos.txt'
        )
        for v in ssh_stdout:
            l_result.append(v)
        if o_ssh:
            respuesta = ('Email enviado con éxito!')
        else:
            respuesta = ('KO')

        return respuesta
