import tkinter as tk
from PIL import Image, ImageTk

from modulo_unico import Menu, Azione, Elemento, gioca, ringraziamenti


def mostra_menu():
    """Crea e mostra la finestra principale con il menu grafico."""
    # Dimensioni della finestra
    window_width = 474
    window_height = 457

    root = tk.Tk()
    root.title("Menu Pokémon")
    root.geometry(f"{window_width}x{window_height}")

    # Caricamento dell'immagine di sfondo
    bg_image = ImageTk.PhotoImage(Image.open("sfondo.jpg"))
    canvas = tk.Canvas(root, width=window_width, height=window_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Calcolo del centro della finestra
    center_x = window_width // 2
    center_y = window_height // 2

    # Offset per posizionare i bottoni
    button_spacing = 50

    # Pulsante per giocare
    btn_gioca = tk.Button(root, text="Gioca", command=gioca)
    canvas.create_window(center_x, center_y - button_spacing, window=btn_gioca)

    # Pulsante per i ringraziamenti
    btn_ringraziamenti = tk.Button(root, text="Ringraziamenti", command=ringraziamenti)
    canvas.create_window(center_x, center_y, window=btn_ringraziamenti)

    # Pulsante per uscire
    btn_esci = tk.Button(root, text="Esci", command=root.destroy)
    canvas.create_window(center_x, center_y + button_spacing, window=btn_esci)

    root.mainloop()


# Creazione del menu principale
menu = Menu()

# Aggiunta degli elementi al menu
elemento1 = Elemento("Gioca", Azione(gioca))  # Elemento per avviare il gioco
elemento3 = Elemento("Ringraziamenti", Azione(ringraziamenti))  # Ringraziamenti

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento3)

# Mostra il menu grafico
mostra_menu()
