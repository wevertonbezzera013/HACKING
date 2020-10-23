import socket

portas = [21, 23, 80, 443, 8080]

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(1.0)
    resposta = cliente.connect_ex(('bancocn.com', porta))

    if resposta == 0:
        print(porta, 'ABERTA')
    else:
        print(porta, 'FECHADA')