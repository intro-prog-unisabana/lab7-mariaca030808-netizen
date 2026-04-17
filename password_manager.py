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
    encrypt_passwords_in_file("examples/example2.txt")

#Parte 3

def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    fila= []
    with open(filename, "r", newline="") as f:
        lector= csv.reader(f)
        for fila in lector:
            if fila:
                fila.append(fila)
    if True:
        for numero, fila in enumerate(fila):
            if numero== 0:
                continue
            if len(fila) >= 1 and fila[0] == website:
                if len(fila) < 3:
                    fila += [""] * (3 - len(fila))
                fila[2]= caesar_encrypt(password)
                break
    with open(filename, "w", newline="") as f:
        escritor= csv.writer(f)
        escritor.writerows(fila)

    return True


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([website_name, username, caesar_encrypt(password)])
