import sys
import threading
import socket


class Server(socket.socket):

    def commands(self, client, command):
        message = command.decode('utf-8')
        if message == 'admin: list':
            client.send(f'{self.nicknames} are on server.'.encode('utf-8'))
        elif message == 'admin: exit':
            sys.exit(-1)
        else:
            self.broadcast(command)

    def handle(self, client):

        while True:
            index = self.clients.index(client)
            try:
                message = client.recv(2048)
                if self.nicknames[index] == 'admin':
                    print('Admin wants a command.')
                    self.commands(client, message)
                else:
                    self.broadcast(message)
            except:
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'Server >> {nickname} leaved chat.'.encode('utf-8'))
                self.nicknames.remove(nickname)
                break

    def receive(self):

        while True:
            client, address = self.accept()

            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(2048).decode('utf-8')

            if nickname:
                self.nicknames.append(nickname)
                self.clients.append(client)

                print(f'Connected with {address}, nickname is {nickname}.')
                client.send('Server >> Connected to server!'.encode('utf-8'))
                self.broadcast(f'Server >> {nickname} joined chat.'.encode('utf-8'))

                thread = threading.Thread(target=self.handle, args=(client,))
                thread.start()

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def connect_to(self, host, port):
        self.bind((host, port))
        self.listen()

    def __init__(self, host, port):
        super(Server, self).__init__(socket.AF_INET, socket.SOCK_STREAM)

        self.clients = []
        self.nicknames = []

        self.connect_to(host, port)
        print('Server is listening.')
        thread_receive = threading.Thread(target=self.receive, args=())
        thread_receive.start()


def main():
    Server('127.0.0.1', 1234)


if __name__ == "__main__":
    main()
