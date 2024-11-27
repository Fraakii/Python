def AggiuntaLibro(libri):
    nLibri = int(input("Quanti libri vuoi inserire? "))
    for i in range(nLibri):
        libro = input(f"Inserisci il libro {i+1}:")
        libri.append(libro)
        print(f"libro {i+1}: {libri[i]}")
    return libri
    
def PrestitoLibro(libri, libriPrestito):
    nLibriPrestito = int(input("Quanti libri vuoi in prestito? "))
    for i in range(nLibriPrestito):
        libroPrestito = input("Quale libro vuoi in prestito? ")
        
        # if libroPrestito==libri[f"{libroPrestito}"]:
        
        if libroPrestito in libri:
            libriPrestito.append(libroPrestito)
            libri.remove(libroPrestito)
            print(f"Hai preso in prestito il libro: {libroPrestito}")
        else:
            print(f"Il libro '{libroPrestito}' non è disponibile.")
    
    print(f"Libri rimanenti: {libri}")
    print(f"Libri in prestito: {libriPrestito}")
    
    # print(f"{libri}")
    # print(f"{libriPrestito}")
        

def RiportaLibro(libri):
    riporta = input("Quale libro riporti? ")
    
    
        
