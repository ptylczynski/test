import socket

from GeneratorExecutor import GeneratorExecutor


class AutoChangeLogServer:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 6466))
        self.socket.listen(5)

        while True:
            (connected_socket, address) = self.socket.accept()
            print('Connection from: ' + str(address[0]) + ':' + str(address[1]))
            GeneratorExecutor().start()
            connected_socket.close()


if __name__ == "__main__":
    AutoChangeLogServer()