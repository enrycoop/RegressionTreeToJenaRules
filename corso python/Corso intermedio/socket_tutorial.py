import socket
"""
s.recv() riceve i messaggi
s.send() trasmette i messaggi
s.close() chiude connessione
socket.gethostname() restituisce l'hostname della macchina su cui sta girando l'interprete
socket.gethostbyname() restituisce l'IP associato al nome passato
"""
#creazione oggetto socket
s = socket.socket()

s.connect(('www.google.it',80))

richiesta = "GET / HTTP/1.1\nHost: www.google.it\n\n"
s.send(richiesta.encode())

risposta = s.recv(2048)
print(risposta)
while len(risposta) > 0:
    print(risposta)
    risposta = s.recv(2048)
s.close()
