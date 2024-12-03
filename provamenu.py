# import tkinter as tk
# from tkinter import messagebox

# class MenuGrafico:
#     def __init__(self, root):
#         self.root = root
#         self.elementi = []  # Lista di elementi del menu
#         self.root.title("Menu Grafico")
#         self.root.geometry("400x400")
#         self.root.configure(bg="yellow")  # Colore dello sfondo

#         self.label = tk.Label(self.root, text="Benvenuto nel Menu!", font=("Comic Sans", 16), bg="yellow", fg="white")
#         self.label.pack(pady=10)

#     def aggiungi_elemento(self, elemento):
#         """Aggiunge un elemento al menu grafico."""
#         if isinstance(elemento, Elemento):
#             self.elementi.append(elemento)
#         else:
#             raise TypeError("L'elemento deve essere un'istanza della classe Elemento")

#     def mostra_menu(self):
#         """Mostra gli elementi del menu come pulsanti."""
#         for elemento in self.elementi:
#             btn = tk.Button(
#                 self.root,
#                 text=elemento.get_nome(),
#                 font=("Comic Sans", 14),
#                 bg="white",  # Colore dei pulsanti
#                 fg="black",  # Colore del testo
#                 command=elemento.esegui_azione
#             )
#             btn.pack(pady=5)

# class Elemento:
#     def __init__(self, nome, azione=None):
#         self.__nome = nome
#         self.__azione = azione

#     def get_nome(self):
#         return self.__nome

#     def esegui_azione(self):
#         """Esegue l'azione associata a questo elemento."""
#         if self.__azione:
#             self.__azione()
#         else:
#             print(f"{self.__nome} non ha alcuna azione associata.")

# # Esempio di utilizzo
# def esempio_azione_1():
#     messagebox.showinfo("Azione 1", "Azione 1 eseguita!")

# def esempio_azione_2():
#     messagebox.showinfo("Azione 2", "Azione 2 eseguita!")

# root = tk.Tk()
# menu = MenuGrafico(root)

# menu.aggiungi_elemento(Elemento("Opzione 1", azione=esempio_azione_1))
# menu.aggiungi_elemento(Elemento("Opzione 2", azione=esempio_azione_2))
# menu.aggiungi_elemento(Elemento("Esci", azione=root.destroy))

# menu.mostra_menu()

# root.mainloop() 


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MenuGrafico:
    def __init__(self, root):
        self.root = root
        self.elementi = []  # Lista di elementi del menu
        self.root.title("Menu Grafico")
        self.root.geometry("400x400")

        # Caricamento dell'immagine di sfondo
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = ImageTk.PhotoImage(Image.open("sfondo.jpg"))
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.label = tk.Label(self.root, text="Benvenuto nel Menu!", font=("Comic Sans", 16), fg="black")
        self.label_window = self.canvas.create_window(200, 50, window=self.label)

    def aggiungi_elemento(self, elemento):
        """Aggiunge un elemento al menu grafico."""
        if isinstance(elemento, Elemento):
            self.elementi.append(elemento)
        else:
            raise TypeError("L'elemento deve essere un'istanza della classe Elemento")

    def mostra_menu(self):
        """Mostra gli elementi del menu come pulsanti."""
        y_position = 100
        for elemento in self.elementi:
            btn = tk.Button(
                self.root,
                text=elemento.get_nome(),
                font=("Comic Sans", 14),
                bg="white",  # Colore dei pulsanti
                fg="black",  # Colore del testo
                command=elemento.esegui_azione
            )
            self.canvas.create_window(200, y_position, window=btn)
            y_position += 50

class Elemento:
    def __init__(self, nome, azione=None):
        self.__nome = nome
        self.__azione = azione

    def get_nome(self):
        return self.__nome

    def esegui_azione(self):
        """Esegue l'azione associata a questo elemento."""
        if self.__azione:
            self.__azione()
        else:
            print(f"{self.__nome} non ha alcuna azione associata.")

# Esempio di utilizzo
def esempio_azione_1():
    messagebox.showinfo("Azione 1", "Azione 1 eseguita!")

def esempio_azione_2():
    messagebox.showinfo("Azione 2", "Azione 2 eseguita!")

root = tk.Tk()
menu = MenuGrafico(root)

menu.aggiungi_elemento(Elemento("Opzione 1", azione=esempio_azione_1))
menu.aggiungi_elemento(Elemento("Opzione 2", azione=esempio_azione_2))
menu.aggiungi_elemento(Elemento("Esci", azione=root.destroy))

menu.mostra_menu()

root.mainloop()

