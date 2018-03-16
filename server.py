import pickle
import struct
import sys
import socket
import threading

SERVERADRESS = (socket.gethostname(), 6000)
utilisateur_list={}

class Server():
    def __init__(self):
        self.__server=socket.socket()
        try:
            self.__server.bind(SERVERADRESS)
        except socket.error:
            print( 'Fail {}' .format(socket.error))

        self.__server.listen(20)

    def run(self):
        print("En écoute ...{}".format(SERVERADRESS))
        while True:
            client, address =self .__server.accept()
            td = ThreadClient(client, address)
            td.start()
            client.send("\nHEllO from the other side\n".encode())

    def exit(self):
        self.__server.close()


class ThreadClient(threading.Thread):
    def __init__(self,connexion,address):
        threading.Thread.__init__(self)
        self.address=address
        self.connexion= connexion
        self.commands={
            '/list': self._list,
            '/aka':self._aka,
        }

    def run(self):
        utilisateur_list[self.address]=[self.connexion,"", "En ligne"]
        while True:
            nbr = self.connexion.recv(1024).decode()
            if nbr[0]=="/":
                k=nbr.rstrip()+ ''
                commande=k[k.index(' ')]
                parametre=k[k.index('')+1].rstrip()
                parametres=[parametre,self.address]
                if commande in self.commands:
                    try:
                        self.commands[commande](self.connexion) if parametre==''else self.commands[commande](params)
                    except Exception as e:
                        print( "Erreur d'execution")

                else :
                    print('Commande introuvable:'),commande
            elif not nbr:
                break
            else :
                message="{}>{}".format(utilisateur_list[self.address][1],nbr)
                print(message)
                for key in utilisateur_list:
                    if key != self.address:
                        utilisateur_list[key][0].send(message.endcode())
                        

    def _aka(self,parametres):
        utilisateur_list[parametres[1][1]]=parametres[0]
        stg= "{} est maintenant en ligne".format (parametres[0])
        for key in utilisateur_list:
            if key!= self.address:
                utilisateur_list[key][0].send(stg.endcode())

    def _list(self, client):
        utilisateur= ""
        for k in utilisateur_list:
            utilisateur += "- {} - [{}]\n".format(utilisateur_list[k][1],k,utilisateur[k][2])
        self.connexion.send(("{} utilisateurs sont actuellemnt connectés".format(len(utilisateur_list))).endcode())
        self.connexion.send(utilisateur.endcode())


if __name__=='__main__':
    Server().run()
