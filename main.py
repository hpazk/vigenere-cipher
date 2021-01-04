from app.chat_room.server import ChatServer
from getpass import getpass


def main():

    port = int(input('enter port address: '))
    key = getpass('enter the key: ')

    room_server = ChatServer(port, key)
    room_server.run()


if __name__ == "__main__":
    main()
