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



try:
    img = Image.open("calculator.png")  # Usa il percorso assoluto
    img_tk = ImageTk.PhotoImage(img)
    label_img = tk.Label(window, image=img_tk, bg="white")
    label_img.pack(pady=20)
except FileNotFoundError:
    print("Immagine non trovata! Assicurati che il file sia nella posizione corretta.")
    img_tk = None
    label_img = tk.Label(window, text="Nessuna immagine disponibile", bg="white", font=("Arial", 16))
    label_img.pack(pady=20)


 
# Casella di testo per il primo numero 
entry1 = tk.Entry(window, width=15) 
entry1.pack(pady=5) 

# Casella di testo per il secondo numero 
entry2 = tk.Entry(window, width=15) 
entry2.pack(pady=5) 
 
# Frame per contenere i pulsanti
frame_pulsanti = tk.Frame(window)
frame_pulsanti.pack(pady=5)

# Pulsanti per le operazioni
button_somma = tk.Button(frame_pulsanti, text="+", command=lambda: calcolatrice('+')) 
button_somma.pack(side=tk.LEFT, padx=5)

button_sottrazione = tk.Button(frame_pulsanti, text="-", command=lambda: calcolatrice('-')) 
button_sottrazione.pack(side=tk.LEFT, padx=5)

button_prodotto = tk.Button(frame_pulsanti, text="*", command=lambda: calcolatrice('*')) 
button_prodotto.pack(side=tk.LEFT, padx=5)

button_divisione = tk.Button(frame_pulsanti, text="/", command=lambda: calcolatrice('/')) 
button_divisione.pack(side=tk.LEFT, padx=5)


# Etichetta per mostrare il risultato 
label_risultato = tk.Label(window, text="Risultato: ") 
label_risultato.pack(pady=10)


if __name__ == "__main__":
    window.mainloop()