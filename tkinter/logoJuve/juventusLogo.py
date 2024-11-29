import tkinter as tk
from PIL import Image, ImageTk

# Creazione della finestra principale
window = tk.Tk()
window.title("Finestra Juventus")
window.geometry("500x500")
window.resizable(False, False)
window.configure(background="white")

# Caricamento e ridimensionamento dell'immagine
try:
    img = Image.open("juventus_logo.png")  # Inserire il nome del file immagine
    img = img.resize((500, 500), Image.Resampling.LANCZOS)  # Usa LANCZOS invece di ANTIALIAS
    img_tk = ImageTk.PhotoImage(img)
except FileNotFoundError:
    print("Immagine non trovata! Assicurati che il file 'juventus_logo.png' sia nella stessa cartella.")

# Creazione di un'etichetta per visualizzare l'immagine
label_img = tk.Label(window, image=img_tk, bg="white")
label_img.pack(pady=20) #Aggiunge uno spazio verticale (padding) di 20 pixel sopra e sotto l'immagine

# Avvio della finestra
if __name__ == "__main__":
    window.mainloop()
    
    



