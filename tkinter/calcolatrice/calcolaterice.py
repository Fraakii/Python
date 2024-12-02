import tkinter as tk
from PIL import Image, ImageTk

def calcolatrice(operazione):
    num1 = float(entry1.get()) 
    num2 = float(entry2.get())
    
    risultato = ""
        
    if operazione == '+':
        risultato = f"{num1} + {num2} = {num1 + num2}"

    elif operazione == '-':
        risultato = f"{num1} - {num2} = {num1 - num2}"

    elif operazione == '*': 
        risultato = f"{num1} * {num2} = {num1 * num2}"

    elif operazione == '/':
        if (num2 != 0):
            risultato = f"{num1} / {num2} = {num1 / num2}"
        else:
            risultato = "Errore: divisione per zero non consentita."
        
    # Aggiornare la label con il risultato
    label_risultato.config(text="Risultato: " + risultato)

# Creazione della finestra principale 
window = tk.Tk() 
window.title("Calcolatrice Semplice") 
window.geometry("500x350")

# Aggiungere immagine come sfondo
try:
    img = Image.open("calculator.png")
    img = img.resize((500, 350), Image.Resampling.LANCZOS)  # Ridimensiona l'immagine alle dimensioni della finestra
    bg_img = ImageTk.PhotoImage(img)
    
# Canvas per gestire lo sfondo
    canvas = tk.Canvas(window, width=500, height=350)      # width=500, height=350: Imposta la larghezza e l'altezza del Canvas.
    canvas.pack(fill="both", expand=True)                  # fill="both": Il Canvas si espande per occupare tutto lo spazio disponibile nella finestra.
                                                           # expand=True: Il Canvas si ridimensiona automaticamente quando la finestra viene ridimensionata.    
    canvas.create_image(0, 0, image=bg_img, anchor="nw")   # inserisce l'
except FileNotFoundError:
    print("Immagine non trovata! Assicurati che il file sia nella posizione corretta.")
    bg_img = None
    canvas = tk.Canvas(window, width=500, height=350, bg="white")
    canvas.pack(fill="both", expand=True)

# Aggiungere widget sopra lo sfondo
entry1 = tk.Entry(window, width=15) 
entry2 = tk.Entry(window, width=15) 

label_risultato = tk.Label(window, text="Risultato: ", bg="white", font=("Arial", 12))

frame_pulsanti = tk.Frame(window, bg="white")
button_somma = tk.Button(frame_pulsanti, text="+", command=lambda: calcolatrice('+')) 
button_sottrazione = tk.Button(frame_pulsanti, text="-", command=lambda: calcolatrice('-')) 
button_prodotto = tk.Button(frame_pulsanti, text="*", command=lambda: calcolatrice('*')) 
button_divisione = tk.Button(frame_pulsanti, text="/", command=lambda: calcolatrice('/'))

# Posizionamento dei widget sul canvas (spostati verso destra aumentando il valore di x)
canvas.create_window(350, 50, window=entry1)  # Posizione degli input (spostato a x=300)
canvas.create_window(350, 100, window=entry2)

canvas.create_window(350, 150, window=frame_pulsanti)  # Posizione del frame con i pulsanti
button_somma.pack(side=tk.LEFT, padx=5)
button_sottrazione.pack(side=tk.LEFT, padx=5)
button_prodotto.pack(side=tk.LEFT, padx=5)
button_divisione.pack(side=tk.LEFT, padx=5)

canvas.create_window(350, 200, window=label_risultato)  # Posizione del risultato

if __name__ == "__main__":
    window.mainloop()
