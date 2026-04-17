import csv

from caesar import caesar_encrypt

#Parte 1
def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, "r") as f:
        password= f.read().strip()

    encryptedPassword= caesar_encrypt(password) 
    with open (filename, "w") as f:
        f.write(encryptedPassword)

if __name__ == "__main__":
    encrypt_single_pass("examples/example1.txt")
    
#Parte 2

def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    with open(filename, "r") as f:
        reader= csv.reader(f)
        rows= []
        for row in reader:
            if row:
                rows.append(row)
    for index, row in enumerate(rows):
        if index != 0:
            row[2] = caesar_encrypt(row[2])
    print(rows)

    with open(filename, "w") as f:
        writer= csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    encrypt_passwords_in_file("examples/example2.csv")

#Parte 3

def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    fila= []
    with open(filename, "r") as f:
        lector= csv.reader(f)
        for linea in lector:
            if linea:
                fila.append(linea)
    found= False
    for num in range(len(fila)):
        if num == 0:
            continue 
        if fila[num][0]== website:
            fila[num][2]= caesar_encrypt(password)
            found= True
            break
    if not found:
        return False

    with open(filename, "w") as f:
        escritor= csv.writer(f)
        escritor.writerows(fila)
        return True

#Parte 4

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([website_name, username, caesar_encrypt(password)])
