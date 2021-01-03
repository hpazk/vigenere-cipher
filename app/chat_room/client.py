import socket
import threading
import os

import getpass
from vigenere_chiper import VigenereChiper

vc = VigenereChiper()

nickname = input('username: ')
key = getpass.getpass(
    'Enter the correct key if you want to see the conversation: ')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))


def receive():

    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                dec = vc.decrypt(message, key)
                if key != os.environ.get('VC_KEY'):
                    print('')
                print(dec)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))

        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
