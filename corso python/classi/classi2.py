'''
variabili di istanza e di classe
le variabili di classe sono accedibili anche dalle istanze
'''
class Studente:

    ore_settimanali = 36
    corpo_studentesco = 0

    def __init__(self,nome,cognome,corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        Studente.corpo_studentesco += 1

    def scheda_personale(self):
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di studi:{self.corso_di_studi}\n Ore Settimanali:{self.ore_settimanali}\n"

studente_uno = Studente('Enry','Coop','programmazione')
studente_due = Studente('Marta','Stannis','Scienze politiche')
print(Studente.corpo_studentesco)
studente_uno.ore_settimanali += 4 #verrà influenzata solo la propria variabile
