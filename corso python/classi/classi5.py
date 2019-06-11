"""
metodi di classe
"""
class Persona:

    def __init__(self,nome,cognome,età,residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
    
    @classmethod
    def from_string(cls,stringa_persona, *args):
        nome, cognome, età, residenza = stringa_persona.split("-")
        return cls(nome, cognome, età, residenza, *args)
    
    @classmethod
    def occupazione(cls):
        if cls.__name__=='Studente':
            return 'Studente'
        else:
            return 'Insegnante'

    @staticmethod
    def info_prog():
        info= """
        Nome: Persona
        Creato da : EnryCoop
        Sito: www.enrycoop.com
        commenti: scritto usando python"""
        return info
    
    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}"""
        return scheda
    
    def modifica_scheda(self):
        print("""Modifica Sheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")

        scelta = input("cosa desideri modificare?")
        if scelta=="1":
            self.nome = input("Nuovo nome --> ")
        if scelta=="2":
            self.cognome = input("Nuovo cognome --> ")
        if scelta=="3":
            self.età = input("Nuova età --> ")
        if scelta=="4":
            self.residenza = input("Nuova residenza --> ")


class Studente(Persona):
    profilo = "Studente"
    
    def __init__(self, nome, cognome, età, residenza,corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio
    
    def scheda_personale(self):
        scheda = f"""
        profilo:{Studente.profilo}
        Corso di studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda
    
    def cambio_corso(self,corso):
        self.corso_di_studio = corso
        print("corso aggiornato.")

class Insegnante(Persona):
    profilo = "Insegnante"
    
    def __init__(self, nome, cognome, età, residenza,materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie
    
    def scheda_personale(self):
        scheda = f"""
        profilo:{Insegnante.profilo}
        Corso di studi:{self.materie}
        ***"""
        return super().scheda_personale() + scheda

    def aggiungi_materia(self,nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco materie aggiornato.")

print(Persona.info_prog())