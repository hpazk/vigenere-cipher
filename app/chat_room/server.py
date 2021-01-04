import socket
import threading  # Libraries import
import os

from modules.vigenere_chiper import VigenereChiper


class ChatServer:
    def __init__(self, port, key):
        self.host = '127.0.0.1'
        self.port = port
        self.key = key

        self._clients = []
        self._nicknames = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run_server(self):
        self.server.bind((self.host, self.port))
        self.server.listen()

        self._msg_receiver()
        # return server

    def _broadcaster(self, msg):
        vc = VigenereChiper()
        enc = vc.encrypt(str(msg.decode('utf-8')), self.key)

        for client in self._clients:
            client.send(enc.encode('utf-8'))

    def _msg_handler(self, client):
        while True:
            try:
                msg = client.recv(1024)
                self._broadcaster(msg)
            except:
                index = self._clients.index(client)
                self._clients.remove(client)
                client.close()

                nickname = self._nicknames[index]
                self._broadcaster('{} left!'.format(nickname).encode('utf-8'))
                self._nicknames.remove(nickname)
                break

    def _msg_receiver(self):
        while True:
            # server = self._server()

            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))
            client.send('NICKNAME'.encode('utf-8'))

            nickname = client.recv(1024).decode('utf-8')
            self._nicknames.append(nickname)

            self._clients.append(client)
            print("Nickname is {}".format(nickname))
            self._broadcaster("{} joined! ".format(nickname).encode('utf-8'))

            # client.send('Connected to server!\n'.encode('utf-8'))
            thread = threading.Thread(
                target=self._msg_handler,
                args=(client,)
            )

            thread.start()
