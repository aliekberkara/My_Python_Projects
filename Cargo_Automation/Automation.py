# 20010011068 / Ali Ekber / KARA

def show_main_menu():
    print("\n******************   ATT CARGO AUTOMATION   ******************")
    print("1) SENDER OPERATIONS")
    print("2) RECEIVER OPERATIONS")
    print("3) OTHER OPERATIONS")
    print("4) Exit")
    a = int(input("Your choice: "))
    return a


def sender_operations():
    def add_cargo():
        cargo_ID = random.randint(1000000000000, 9999999999999)
        cargo["cargo ID"] = cargo_ID
        sender_name = input("Cargo Sender's Name: ")
        cargo["sender name"] = sender_name
        sender_surname = input("Cargo Sender's Surname: ")
        cargo["sender surname"] = sender_surname
        sender_address = input("Cargo Sender's Address: ")
        cargo["sender address"] = sender_address
        receiver_name = input("Cargo Receiver's Name: ")
        cargo["receiver name"] = receiver_name
        receiver_surname = input("Cargo Receiver's Surname: ")
        cargo["receiver surname"] = receiver_surname
        receiver_address = input("Cargo Receiver's Address: ")
        cargo["receiver address"] = receiver_address
        receiver_phone_number = input("Cargo Receiver's Phone Number: ")
        cargo["receiver phone number"] = receiver_phone_number
        file = open("20010011068.txt", "a")
        file.write(str(cargo) + "\n")
        print("Cargo Information Added Successfully...")
        file.close()

    def search_cargo():
        phone = input("Receiver's phone number in the cargo information you want to search: ")
        file = open("20010011068.txt", "r")
        rows = []  # Empty list to add lines in a file to the list
        for i in file:
            rows.append(i)  # Add rows
        file.close()
        index = 0
        for i in rows:
            index = index + 1  # Find the index of the entered TC ID number
            if phone in i:
                break
        try:
            if phone in rows[index - 1]:
                print(rows[index - 1], "\nYour cargo will be delivered as soon as possible.")
            else:
                print("There is no cargo belonging to this phone number...")
        except IndexError:
            print("No cargo information available.")

    def update_cargo():
        phone = input("Receiver's phone number in the cargo information you want to update: ")
        file = open("20010011068.txt", "r")
        rows = []  # Empty list to add lines in a file to the list

        for i in file:
            rows.append(i)  # Add rows
        file.close()
        index = 0
        for i in rows:
            index = index + 1  # Find the index of the entered TC ID number
            if phone in i:
                break
        try:
            if phone in rows[index - 1]:
                new_data = ""
                k = open("20010011068.txt", "r")
                source = k.read().splitlines()
                for n, s in enumerate(source, 1):
                    if n == index:
                        continue
                    new_data = new_data + s + "\n"
                k.close()
                with open("20010011068.txt", "w") as k:
                    k.write(new_data)
                k.close()

                cargo_ID = random.randint(1000000000000, 9999999999999)
                cargo["cargo ID"] = cargo_ID
                sender_name = input("Cargo Sender's Name: ")
                cargo["sender name"] = sender_name
                sender_surname = input("Cargo Sender's Surname: ")
                cargo["sender surname"] = sender_surname
                sender_address = input("Cargo Sender's Address: ")
                cargo["sender address"] = sender_address
                receiver_name = input("Cargo Receiver's Name: ")
                cargo["receiver name"] = receiver_name
                receiver_surname = input("Cargo Receiver's Surname: ")
                cargo["receiver surname"] = receiver_surname
                receiver_address = input("Cargo Receiver's Address: ")
                cargo["receiver address"] = receiver_address
                receiver_phone_number = input("Cargo Receiver's Phone Number: ")
                cargo["receiver phone number"] = receiver_phone_number
                file = open("20010011068.txt", "a")
                file.write(str(cargo) + "\n")
                print("Cargo Information Updated Successfully...")
                file.close()
            else:
                print("There is no cargo belonging to this phone number...")
        except IndexError:
            print("No cargo information available.")

    while True:
        print("\n******************   ATT CARGO AUTOMATION   ******************")
        print("1) Add Cargo Information")
        print("2) Search Cargo Information")
        print("3) Update Cargo Information")
        print("4) Main Menu")
        a = int(input("Your choice: "))

        if a == 1:
            add_cargo()
        elif a == 2:
            search_cargo()
        elif a == 3:
            update_cargo()
        elif a == 4:
            break
        else:
            print("Please, Try Again...")


def receiver_operations():
    def search_cargo():
        phone = input("Receiver's phone number in the cargo information you want to search: ")
        file = open("20010011068.txt", "r")
        rows = []  # Empty list to add lines in a file to the list
        for i in file:
            rows.append(i)  # Add rows
        file.close()
        index = 0
        for i in rows:
            index = index + 1  # Find the index of the entered TC ID number
            if phone in i:
                break
        try:
            if phone in rows[index - 1]:
                print(rows[index - 1], "\nYour cargo will be delivered as soon as possible.")
            else:
                print("There is no cargo belonging to this phone number...")
        except IndexError:
            print("No cargo information available.")

    def delete_cargo():
        phone = input("Receiver's phone number in the cargo information you want to delete: ")
        file = open("20010011068.txt", "r")
        rows = []  # Empty list to add lines in a file to the list

        for i in file:
            rows.append(i)  # Add rows
        file.close()
        index = 0
        for i in rows:
            index = index + 1  # Find the index of the entered phone number
            if phone in i:
                break
        try:
            if phone in rows[index - 1]:
                new_data = ""
                k = open("20010011068.txt", "r")
                source = k.read().splitlines()
                for n, s in enumerate(source, 1):
                    if n == index:
                        continue
                    new_data = new_data + s + "\n"
                k.close()
                with open("20010011068.txt", "w") as k:
                    k.write(new_data)
                k.close()
                print("Cargo Information Successfully Deleted...")
            else:
                print("There is no cargo belonging to this phone number...")
        except IndexError:
            print("No cargo information available.")

    while True:
        print("\n******************   ATT CARGO AUTOMATION   ******************")
        print("1) Search Cargo Information")
        print("2) Delete Cargo Information")
        print("3) Main Menu")
        a = int(input("Your choice: "))

        if a == 1:
            search_cargo()
        elif a == 2:
            delete_cargo()
        elif a == 3:
            break
        else:
            print("Please, Try Again...")


def other_operations():
    def calculate_cargo_fee():
        cargo_width = int(input("Cargo Width (cm): "))
        cargo_height = int(input("Cargo Height (cm): "))
        cargo_lenght = int(input("Cargo Length(cm): "))
        desi = (cargo_width * cargo_lenght * cargo_height) / 3000
        cargo_fee = (desi - 1) * 1.80 + 16
        print("Your Cargo Fee:", cargo_fee, "TL")

    def listing_cargo():
        file = open("20010011068.txt", "r")
        for i in file:
            print(i)
        file.close()

    while True:
        print("\n******************   ATT CARGO AUTOMATION   ******************")
        print("1) Calculate Cargo Fee")
        print("2) Listing Cargo")
        print("3) Main Menu")
        a = int(input("Your choice: "))

        if a == 1:
            calculate_cargo_fee()
        elif a == 2:
            listing_cargo()
        elif a == 3:
            break
        else:
            print("Please, Try Again...")


import random

cargo = {}

choice = show_main_menu()

while True:
    if choice == 1:
        sender_operations()
    elif choice == 2:
        receiver_operations()
    elif choice == 3:
        other_operations()
    elif choice == 4:
        break
    else:
        print("Please, Try Again...")

    if choice != 4:
        choice = show_main_menu()
