# prova.py

from abc import ABC, abstractmethod
from modulo_menu import Menu, Elemento, Azione
import pprint, random, time, json





class Utente:

    def __init__(self, nome):

        self.__nome = nome
        self.__punteggio = 0
        self.__alias = ""

    def get_nome(self):

        return self.__nome
    
    def get_alias(self):

        return self.__alias
    
    def __set_alias(self, alias):

        self.__alias = alias

    def nome_utente(self):

        alias = input("Inserisci uno username: ")

        self.__set_alias(alias)


    def get_punteggio(self):

        return self.__punteggio
    
    def __set_punteggio(self, punti):

        self.__punteggio += punti

    
    def aggiungi_punti(self, punti):

        self.__set_punteggio(punti)
    
    def stampa_punteggio(self):

        print(self.__get_punteggio())


class Classifica:


    def __init__(self):

        with open("classifica.json", "r") as file:
            self.__classifica = json.load(file)
            

    def __get_classifica(self):

        return self.__classifica
    
    def __set_classifica(self, utente):

        if utente in self.__classifica:

            self.__classifica[utente.get_nome()].append(utente.get_punteggio())

        else:

            print("Ora sei in classifica!")
            self.__classifica[utente.get_nome()] = [utente.get_punteggio()]
        
    def aggiungi_a_classifica(self, utente):

        self.__set_classifica(utente)

    def stampa_classifica(self):

        pprint.pprint(self.__get_classifica())

    def salva_classifica(self):

        with open("dizionario.json", "w") as file:
            json.dump(self.__get_classifica(), file, indent=4)


class Gioco(ABC):

  

    @abstractmethod
    def calcola_punteggio(self):
        pass
 

class IndovinaIlNumero(Gioco):

            

    def start(self, utente):
        numero_segreto = random.randint(1, 100)
        tentativi = 0
        print("Benvenuto a 'Indovina il Numero'!")
        while True:
            tentativo = int(input("Indovina il numero (1-100): "))
            tentativi += 1
            if tentativo < numero_segreto:
                print("Troppo basso!")
            elif tentativo > numero_segreto:
                print("Troppo alto!")
            else:
                print(f"Complimenti! Hai indovinato il numero in {tentativi} tentativi.")

                self.calcola_punteggio(tentativi, utente)

                break

    def calcola_punteggio(self, tentativi, utente):

        if tentativi <= 5:

            utente.aggiungi_punti(100)
            print("ECCEZIONALE! 100 punti per te!")

        elif 5 < tentativi <= 10:

            utente.aggiungi_punti(50)
            print("BRAVISSIMO! 50 punti per te!")

        elif 10 < tentativi <=20:

            utente.aggiungi_punti(25)
            print("Bravo! 25 punti per te!")

        else:

            utente.aggiungi_punti(5)
            print("Potevi fare di meglio... 5 punti per te!")


class IndovinaEquazioni(Gioco):




    def calcola_punteggio(self, utente, punteggio):
        
        if punteggio <= 20:

            print("BRAVISSIMO! 100 punti per te!")
            utente.aggiungi_punti(100)
                
        elif 20 < punteggio <= 100:

            print("Bravo! 50 punti per te!")
            utente.aggiungi_punti(50)

        elif 100 < punteggio <= 200:

            print("Bene! 25 punti per te!")
            utente.aggiungi_punti(25)

        else:

            print("Insomma... 55 punti per te!")
            utente.aggiungi_punti(5)


    def start(self, utente):
        print(f"Ciao {utente.get_nome()}! In questo gioco dovrai risolvere un'equazione di primo grado. Se il risultato è con la virgola approssima alle prime due cifre significative! FAI VELOCE!")

        a = 0
        while a == 0:
            a = random.randint(-10,10)

        b = random.randint(-100, 100)

        print(f"Risolvi l'equazione {a}x + {b} = 0 \n")

        sol = round(-b/a, 2)

        while True:
            t1 = time.time()
            #print(sol)
            x = float(input("Qual è la tua soluzione? "))
            x=round(x, 2)

            punteggio = time.time() - t1
            punteggio = round(punteggio, 3)
            if x  == sol:
                print(utente.get_nome(), "ci hai messo ", punteggio, " secondi per completarlo!")
                break
            else:
                print("Ritenta!")

        self.calcola_punteggio(utente, punteggio)






# Definizione delle azioni di esempio
def numero():

    num.start(utente)    

def equazione():

    eq.start(utente)   

def ringrazia():
    print("Grazie per aver utilizzato il menu!")

# Creazione del menu e aggiunta degli elementi
menu = Menu()
utente = Utente("stefi")
classifica = Classifica()
num = IndovinaIlNumero()
eq = IndovinaEquazioni()


elemento1 = Elemento("Indovina il Numero", Azione(numero))
elemento2 = Elemento("Addio", Azione(equazione))
elemento3 = Elemento("Ringraziamento", Azione(ringrazia))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento2)
menu.aggiungi_elemento(elemento3)

# Mostra il menu ripetibile
menu.mostra_menu()
