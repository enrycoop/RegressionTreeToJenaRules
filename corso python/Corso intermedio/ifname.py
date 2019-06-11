"""
lo utilizziamo nel caso in cui vogliamo
che il nostro codice assuma una doppia valenza
sia come libreria esterna che come programma principale.
"""
def main():
    print('codice da testare.')
    print('come programma')
    print('Lanciato automaticamente')

def print_tre_volte(parola):
    for i in range(3):
        print(parola)

if __name__ == '__main__':
    main()
