import pickle
import struct
import sys
import socket
import threading


class Client():
    def __init__(self, host=socket.gethostname(), port=3500, pseudo= 'BOB'):
        self.__pseudo=pseudo
        self.__socket=socket.socket()
        self.__socket.bind((host, port))
        print('Ecoute sur {}:{}'.format(host, port))

    def run(self):
        handlers = {
            '/exit': self._exit,
            '/quit': self._quit,
            '/join': self._join,
            '/send': self._send,

        }
        self.__running = True
        self.__address = None
        #threading.Thread(target=self._receive).start()
        while self.__running:
            L = sys.stdin.readline().rstrip() + ' '
            command = L[:L.index(' ')]
            param = L[L.index(' ') + 1:].rstrip()
            if command in handlers:
                try:
                    handlers[command]() if param == '' else handlers[command](param)
                except:
                    print("Erreur lors de l'exécution de la commande.")
            else:
                print('Commande inconnue:', command)

    def _quit(self):
        self.__send("/quit")
        self.__address=None

    def _exit(self):
        self.__running = False
        self.__address = None
        self.__socket.close()

    def _join(self, param):
        self.__pseudo=input("Introduis ton pseudo:")
        tokens = param.split(' ')
        if len(tokens) == 2:
            try:
                self.__address = (tokens(tokens[0])[0], int(tokens[1]))
                self.__socket.connect(self.__address)
                print('Connecté à {}:{}'.format(*self.__address))
            except OSError:
                print("Echec d'envoi.")

    def _send(self, param):
        if self.__address is not None:
            try:
                message = param.encode()
                totalsent = 0
                while totalsent < len(message):
                    sent = self.__socket.sendto(message[totalsent:], self.__address)
                    totalsent += sent
            except OSError:
                print('Erreur lors de la réception du message.')

    def _receive(self):
        while self.__running:
            try:
                data, address = self.__socket.recv(1024).decode
                print(data)
            except socket.timeout:
                pass

    def _client(self):
        print(self.__address)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        Client(sys.argv[1], int(sys.argv[2])).run()
    else:
        Client().run()