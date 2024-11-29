import tkinter as tk

window = tk.Tk()
window.title("Etichetta")
window.geometry("600x600")
window.resizable(False, False)
window.configure(background="black")

etichetta=tk.Label(window, text="Etichetta di prova", fg="red", font=("Helvetica", 32))

etichetta.grid(row=0, column=0, sticky="N", padx=10, pady=10) #sticky è come la bussola (N, S, E, W) e serve per la posizione

window.grid_rowconfigure(0, weight=1)    # Rende la riga 0 espandibile
window.grid_columnconfigure(0, weight=1)  # Rende la colonna 0 espandibile


# Facciamo la Label con una funzione, la funzione deve essere dichiarata prima del bottone
def stampaEtichetta():
    text = "Etichetta da funzione"
    text_output = tk.Label(window, text=text, fg="purple", font=("Hevetica", 10) )
    
    text_output.grid(row=1, column=1, sticky="W")
    
# Primo bottone
first_button = tk.Button(text="Clicca", command=stampaEtichetta)   
first_button.grid(row=1, column=0, sticky="W")

# Funzione per stampare etichetta Input
def stampaEtichettaInput():
    testo = input_text.get()
    text_output1 = tk.Label(window, text=testo, fg="Blue", font=("Helvetica, 16"))
    text_output1.grid(row=3, column=1, sticky="W")

# Input Box
input_text = tk.Entry(window)
input_text.grid(row=3, column=0, sticky="S")

# Secondo bottone
second_button = tk.Button(window, text="Clicca Input", command=stampaEtichettaInput)   
second_button.grid(row=3, column=0, sticky="W")



# Avvio finestra
if __name__ == "__main__":
    window.mainloop()