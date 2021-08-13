import socket

from executor import Executor


class AutoChangeLogServer:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 6465))
        self.socket.listen(5)

        while True:
            (connected_socket, address) = self.socket.accept()
            print('Connection from: ' + str(address[0]) + ':' + str(address[1]))
            Executor().start()
            connected_socket.close()


if __name__ == "__main__":
    AutoChangeLogServer()