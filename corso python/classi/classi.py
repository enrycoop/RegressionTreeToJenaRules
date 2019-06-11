'''
Python 3
Programmazione a Oggetti: CLASSI e ISTANZE
'''
class Studente:
    def __init__(self,nome,cognome,corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
    
    def scheda_personale(self):
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di studi:{self.corso_di_studi}\n"

studente_uno = Studente('Enry','Coop','programmazione')
studente_due = Studente('Marta','Stannis','Scienze politiche')

print(studente_uno.scheda_personale())
print(studente_due.scheda_personale())

#richiamare funzione attraverso la classe
print(Studente.scheda_personale(studente_uno))