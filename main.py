from unittest import result

from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
filename= input("Enter the CSV file name:\n")
encrypt_passwords_in_file(filename)
while True:
    print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
    optionUsuario= input()

    if optionUsuario == "1":
        print("Enter the website and the new password:")
        data= input().split()
        if len(data) < 2:
            print("Input is in the wrong format!")
            continue

        website= data[0]
        password= data[1]

        if len(password) < 12:
            print("Password is too short!")
            continue

        operación= change_password(filename, website, password)
        if operación== False:
            print("Website not found! Operation failed.")
        else:
            print("Password changed.")
            
    elif optionUsuario == "2":
        print("Enter the website, username, and password:")
        data = input().split()
        if len(data) < 3:
            print("Input is in the wrong format!")
            continue
        website= data[0]
        username= data[1]
        password= data[2]
        if len(password) < 12:
            print("Password is too short!")
            continue
        add_login(filename, website, username, password)
        print("Login added.")

    elif optionUsuario== "3":
        break
    else:
        print("Invalid option selected!")


if __name__ == "__main__":
    main()
