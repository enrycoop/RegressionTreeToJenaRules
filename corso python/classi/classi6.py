"""
metodi speciali o magici o dunder (da double underscore)
permettono di creare funzionalità simili agli oggetti già presenti in python
"""

class Studente:
    
    def __init__(self, nome, cognome, corso_di_studio):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studio = corso_di_studio
    
    def scheda_personale(self):
        return f"""
        Scheda studente
        Nome: {self.nome}
        Cognome: {self.cognome}
        Corso di studi:{self.corso_di_studio}
        """
    
    def __add__(self, other):
        """Solo per fini dattici"""
        return self.nome + " " + other.cognome

    def __str__(self):
        """Rappresentazione leggibile - per pubblico"""
        return f"Lo studente {self.nome} {self.cognome}"
    
    def __repr__(self):
        """rappresentazione non ambigua - per sviluppatori"""
        return f"Studente('{self.nome}', '{self.cognome}', '{self.corso_di_studio}')"

studente_uno = Studente('Peter','Malkovich','Psicologia')
studente_due = Studente('John','Snow','Antropologia')

print(studente_due.__str__())
print(repr(studente_due))
    
