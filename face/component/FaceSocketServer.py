import os
import socket


class FaceSocketServer:
    def __init__(self, host, port):
        self.address = (host, port)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(self.address)
            s.listen(1)
            con, clientAddress = s.accept()
            with con:
                while True:
                    data = con.recv(1024)
                    print(data)


if __name__ == '__main__':
    socketServer = FaceSocketServer('127.0.0.1', 3000)
    socketServer.run()
