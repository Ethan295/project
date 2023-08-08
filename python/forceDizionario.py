

def cerca_stringa(stringa, file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        for numero_linea, linea in enumerate(file, 1):
            if linea.startswith(stringa):
                print(f"Trovato: '{stringa}' alla linea {numero_linea}")
                return
    print(f"La stringa '{stringa}' non è stata trovata nel file.")


stringa_cercata = "Ethan"
file_da_controllare = "password.txt"

cerca_stringa(stringa_cercata, file_da_controllare)

#       1
# julia
#  b1tch3s  
