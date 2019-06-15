import socket
import sys

def invia_comandi(s):
    while True:
        comando = input('-> ')
        if comando == 'ESC':
            print('Sto chiudendo la connessione col server.')
            s.close()
            sys.exit()
        else:
            s.send(comando.encode())
            data = s.recv(4096)
            print(str(data))

def conn_sub_server(indirizzo_server):
    try:
        s = socket.socket() #creazione del socket client
        s.connect(indirizzo_server) #connessione al server
        print(f'Connessione al server {indirizzo_server} stabilita.')
    except socket.error as errore:
        print(f"qualcosa è andato storto, sto uscendo... \n{errore}")
        sys.exit()
    invia_comandi(s)

if __name__ == '__main__':
    conn_sub_server(('192.168.1.7',15000)) #scegliere una porta tra 1025 e 65535

