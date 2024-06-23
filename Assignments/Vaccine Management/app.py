import os
import pickle


def clear() -> None:
    os.system("cls")


def insert() -> None:
    clear()
    with open("Records.dat", "ab") as file:
        aadhar: int = int(input("Enter Aadhar Number: "))
        age: int = int(input("Enter Age: "))
        name: str = input("Enter Name: ")
        vaccineType: str = input("Enter Vaccine Type: ")
        record: dict[str, int | str] = {
            "Aadhar Number": aadhar,
            "Name": name,
            "Age": age,
            "Vaccine type": vaccineType,
        }
        pickle.dump(record, file)
        print("__Data Recorded__")
        input("Press enter to continue")


def display() -> None:
    clear()
    with open("Records.dat", "rb") as file:
        aadhar: int = int(input("Enter Aadhar Number to search by: "))
        while True:
            try:
                records: dict[str, int | str] = pickle.load(file)
                if records["Aadhar Number"] == aadhar:
                    for key, value in records.items():
                        print(f"{key} => {value}")
                    break
            except EOFError:
                print("end of File reached")
                break
        input("Press any key to continue")


def update() -> None:
    # with open("Records.dat", "rb") as file, open("Temp Records", "wb") as tempfile:
    #     aadhar: int = int(input("Enter Aadhar Number to search by: "))
    #     while True:
    #         try:
    #             database: dict[str, int | str] = pickle.load(file)
    #             if database["Aadhar Number"] != aadhar:
    #                 pickle.dump(database, tempfile)
    #             else:
    #                 c = input("What do you want to update:\n(1) Name\n(2) Age\n(3) Vaccine Type:\t")
    #                 age: int = int(input("Enter New Age: "))
    #                 name: str = input("Enter Name: ")
    #                 vaccineType: str = input("Enter Vaccine Type: ")
    #                 record: dict[str, int | str] = {
    #                 "Aadhar Number": aadhar,
    #                 "Name": name,
    #                 "Age": age,
    #                 "Vaccine type": vaccineType,
    #                 }
    #                 pickle.dump(record, tempfile)
    #         except EOFError:
    #             print("end of File reached")
    #             break
    #     input("Press any key to continue")
    pass


def delete() -> None:
    pass


if __name__ == "__main__":
    while True:
        clear()
        choice = input(
            "\n---Vaccine Managemment System---\n\nMenu:\n(1) Insert Record\n(2) Display Record\n(3) Update Record\n(4) Delete Record\n(q/Q) Quit programe:\t"
        )
        if choice == "1":
            insert()
        elif choice == "2":
            display()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "q" or choice == "Q":
            print("Exiting programe")
            break
        else:
            print("invalid Choice")
            input("Press any key to continue")
