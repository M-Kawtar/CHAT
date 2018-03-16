#AdvancedPython2BA-Chat
## Binôme 10 : 	Mourad Bousfia  16340
## 				Kawtar Massaâdi 16033


Le but de cette application c'est de réaliser un moyen de chat via plusieurs commandes. Cette dernière a été réalisé sous deux modes : Mode Client/Server et le mode peer-to-peer.

Fonctionnement de l'application : 

1) Le serveur va mémoriser la liste des clients disponnible pour 'chatter'. Il arrive à retenir pour chaque client son pseudo (son nom), son adresse IP et son port de communication.

2) Une fois que le client se présente au serveur, il est considéré comme disponible pour commencer un chat. Il a l'autorisation de demander au serveur de parcourir la liste des utilisateurs qui sont également disponible.

3) Grâce à l'adresse IP d'une autre machine, notre machine est capable de lancer une conversation (un chat) avec une autre grâce au mode peer-to-peer.

Comment lancer le programme : 

> Pour un chat  (Clients/Serveur) : Lancer "server.py" dans la machine qui sera le serveur ensuite lancer "Client.py" qui permettra de nous montrer les personnes qui vont communiquer.

> Pour un chat (Clients/Clients ==> Peer-to-peer) : Lancer "client.py" sur les 2 machines et se connecter sur le "Server.py" pour avoir  l’adresse IP des 2 clients. Ensuite, envoyer les messages souhaités.

Pour discuter avec un des clients connecté, le plus important est de retenir son adresse IP , et de se joindre à celui-ci pour entamer une discussion en mode peer-to-peer !


Exemple : /join 'adresse IP du client' 'port'
