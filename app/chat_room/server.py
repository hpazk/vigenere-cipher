import socket
import threading  # Libraries import
import os

from vigenere_chiper import VigenereChiper

vc = VigenereChiper()

host = '127.0.0.1'
port = 7976

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))  # binding host and port to socket
server.listen()

clients = []
nicknames = []


def broadcast(message):
    enc = vc.encrypt(str(message.decode('utf-8')), os.environ.get('VC_KEY'))

    for client in clients:
        client.send(enc.encode('utf-8'))
        # client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        client.send('NICKNAME'.encode('utf-8'))

        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)

        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined! ".format(nickname).encode('utf-8'))

        # client.send('Connected to server!\n'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
