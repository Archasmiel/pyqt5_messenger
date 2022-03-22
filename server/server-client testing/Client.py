import socket
import sys
import threading


class Client(socket.socket):

    def receive(self):
        while True:
            try:
                message = self.recv(2048).decode('utf-8')
                if message == 'NICK':
                    self.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except Exception:
                print('Error occurred!')
                self.close()
                break

    def write(self):
        while True:
            message = input()
            if message == 'exit()':
                sys.exit(0)
            else:
                message = f'{self.nickname}: {message}'
            self.send(message.encode('utf-8'))

    def connect_to(self, host, port):
        try:
            self.connect((host, port))
            print('Connected to the server.')
            self.nickname = input('Choose a nickname: ')
        except Exception:
            print('Connection error.')

    def __init__(self, host, port):
        super(Client, self).__init__(socket.AF_INET, socket.SOCK_STREAM)

        self.nickname = ''

        self.connect_to(host, port)
        if self.nickname:
            receive_thread = threading.Thread(target=self.receive, args=())
            receive_thread.start()

            write_thread = threading.Thread(target=self.write, args=())
            write_thread.start()


def main():
    Client('127.0.0.1', 1234)


if __name__ == '__main__':
    main()
