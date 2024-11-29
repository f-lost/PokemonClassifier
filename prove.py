import tkinter as tk
import random

class Gioco:
    def __init__(self, nome):
        self.nome = nome

    def start(self):
        raise NotImplementedError("Questo metodo deve essere implementato dalle classi derivate")

class Saltacavallo(Gioco):
    def __init__(self, root):
        super().__init__("Saltacavallo")
        self.root = root
        self.root.configure(bg="brown")  # Cambia il colore dello sfondo
        self.label = tk.Label(root, text="Benvenuto a Saltacavallo!", font=("Comic Sans", 16), bg="brown", fg="white")
        self.label.pack(pady=10)
        self.num_giocatori_label = tk.Label(root, text="Quanti giocatori partecipano?", font=("Comic Sans", 14), bg="brown", fg="white")
        self.num_giocatori_label.pack(pady=5)
        self.num_giocatori_entry = tk.Entry(root, font=("Comic Sans", 14))
        self.num_giocatori_entry.pack(pady=5)
        self.start_button = tk.Button(root, text="Inizia Gioco", command=self.inizia_gioco, font=("Comic Sans", 14), bg="brown", fg="white")
        self.start_button.pack(pady=10)
        self.info_label = tk.Label(root, text="", font=("Comic Sans", 12), bg="brown", fg="white")
        self.info_label.pack(pady=10)
        self.vite_label = tk.Label(root, text="", font=("Comic Sans", 12), bg="brown", fg="white")
        self.vite_label.pack(pady=10)


    def distribuisci_carte(self):
        mazzo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4  # 2-10, Fante, Cavallo, Re, Asso
        random.shuffle(mazzo)
        return [mazzo.pop() for _ in range(len(self.giocatori))]

    def inizia_gioco(self):
        try:
            self.num_giocatori = int(self.num_giocatori_entry.get())
            if self.num_giocatori < 2:
                raise ValueError("Il numero di giocatori deve essere almeno 2.")
        except ValueError as e:
            self.info_label.config(text=f"Errore: {e}")
            return

        self.giocatori = list(range(1, self.num_giocatori + 1))
        self.vite = [2] * self.num_giocatori  # Ogni giocatore inizia con 2 vite
        self.num_giocatori_label.pack_forget()
        self.num_giocatori_entry.pack_forget()
        self.start_button.pack_forget()  # Nasconde il pulsante di inizio
        self.turno()

    def turno(self):
        if len(self.giocatori) > 1:
            carte = self.distribuisci_carte()
            distribuzione = "\nCarte distribuite:\n"
            for i, carta in enumerate(carte):
                distribuzione += f"Giocatore {self.giocatori[i]} ha ricevuto una carta di valore {carta}\n"
            self.info_label.config(text=distribuzione)

            for i, carta in enumerate(carte):
                if 2 <= carta <= 7:
                    continue
                elif carta == 11:  # Cavallo
                    destinatario = (i - 2) % len(self.giocatori)
                    self.vite[destinatario] += 1
                    self.vite[i] -= 1
                elif carta == 12:  # Fante
                    destinatario = (i + 1) % len(self.giocatori)
                    self.vite[destinatario] += 1
                    self.vite[i] -= 1
                elif carta == 13:  # Re
                    self.vite[i] += 1
                elif carta == 1:  # Asso
                    self.vite[i] -= 1

            # Rimuovi i giocatori senza vite
            self.giocatori = [g for g, v in zip(self.giocatori, self.vite) if v > 0]
            self.vite = [v for v in self.vite if v > 0]

            stato_vite = "\nStato delle vite:\n"
            for i, vite in enumerate(self.vite):
                stato_vite += f"Giocatore {self.giocatori[i]} ha {vite} vite\n"
            self.vite_label.config(text=stato_vite)

            self.root.after(2000, self.turno)  # Attende 2 secondi prima del prossimo turno
        else:
            self.info_label.config(text=f"\nIl vincitore Ã¨ il Giocatore {self.giocatori[0]}!")
            self.vite_label.config(text="")

# Esempio di utilizzo
root = tk.Tk()
root.title("Saltacavallo")
root.geometry("400x400")
gioco = Saltacavallo(root)
root.mainloop()