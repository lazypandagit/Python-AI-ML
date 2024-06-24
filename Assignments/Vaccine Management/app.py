##important imports
import os
import pickle
from pathlib import Path

## importing for type annotations
from io import BufferedWriter

##File name Constants
MAIN_FILE_NAME = "Records.dat"
TEMP_FILE_NAME = "Temp_Records.dat"


def clear() -> None:
    os.system("cls")


def printRecord(record: dict[str, int | str | list[str]]) -> None:
    for key, value in record.items():
        print(f"{key} => {value}")


def insert(file: BufferedWriter) -> None:
    clear()
    aadhar: int = getAadhar()
    age: int = getAge()
    name: str = input("Enter Name: ")
    vaccines: list[str] = getVaccineTypes()
    record: dict[str, int | str | list[str]] = {
        "Aadhar Number": aadhar,
        "Name": name,
        "Age": age,
        "Vaccine type": vaccines,
    }
    pickle.dump(record, file)
    print("__Data Recorded__")


def display() -> None:
    clear()
    with open(MAIN_FILE_NAME, "rb") as file:
        aadhar: int = getAadhar("Enter Aadhar Number to search by: ")
        while True:
            try:
                records: dict[str, int | str | list[str]] = pickle.load(file)
                if records["Aadhar Number"] == aadhar:
                    print("Record Found\n")
                    printRecord(records)
                    input("\nPress Enter to continue")
                    break
            except EOFError:
                print("No Records Found\nCheck the details and try again.")
                input("Press Enter to continue")
                break
    # input("Press Enter to continue")


def update() -> None:
    clear()
    with open(MAIN_FILE_NAME, "rb") as mainfile, open(TEMP_FILE_NAME, "wb") as tempfile:
        aadhar: int = getAadhar("Enter Aadhar number to search by: ")
        recordUpdated = False
        while True:
            vaccineData: dict[str, int | str | list[str]] = pickle.load(mainfile)
            if vaccineData["Aadhar Number"] != aadhar:
                pickle.dump(vaccineData, tempfile)
            else:
                print("Record Found:")
                printRecord(vaccineData)
                c = input(
                    "Select Field to update:\n(1) Name\n(2) Age\n(3) Vaccine Type\nOption: "
                )
                if c == "1":
                    name: str = input("Enter New Name: ")
                    vaccineData["Name"] = name
                    print("imput done")
                    pickle.dump(vaccineData, tempfile)
                    recordUpdated = not recordUpdated
                elif c == "2":
                    age: int = getAge("Enter new age: ")
                    vaccineData["Age"] = age
                    pickle.dump(vaccineData, tempfile)
                    recordUpdated = not recordUpdated
                elif c == "3":
                    vaccineData["Vaccine Type"] = getVaccineTypes(
                        "Enter Updated Vaccines"
                    )
                    pickle.dump(vaccineData, tempfile)
                    recordUpdated = not recordUpdated
                else:
                    print("Invalid Choice!!\nRecord was not updates")
            try:
                if recordUpdated == False:
                    raise EOFError
                else:
                    Path.unlink(Path(MAIN_FILE_NAME))
                    Path.rename(Path(TEMP_FILE_NAME), MAIN_FILE_NAME)
            except EOFError:
                print("No Records Found\nCheck the details and try again.")
                break
    input("Press Enter to continue")


def delete() -> None:
    clear()
    with open(MAIN_FILE_NAME, "rb") as mainfile, open(TEMP_FILE_NAME, "wb") as tempfile:
        aadhar: int = getAadhar("Enter Aadhar number of record to delete: ")
        recordDeleted: bool = False
        while True:
            clear()
            database: dict[str, int | str | list[str]] = pickle.load(mainfile)
            if database["Aadhar Number"] != aadhar:
                pickle.dump(database, tempfile)
            else:
                print("Record Deleted!")
                recordDeleted = not recordDeleted
            try:
                if recordDeleted == True:
                    break
                else:
                    raise EOFError
            except EOFError:
                print(
                    "End of File reached\nNo Records Found\nCheck the details and try again."
                )
                break
    Path.unlink(Path(MAIN_FILE_NAME))
    Path.rename(Path(TEMP_FILE_NAME), MAIN_FILE_NAME)
    input("Press Enter to continue...")


def getAadhar(msg: str = "Enter Aadhar number: ") -> int:
    while True:
        try:
            aadhar: str = input(msg)
            if len(aadhar) != 4:
                raise ValueError
            elif aadhar.isnumeric() != True:
                raise TypeError
            elif int(aadhar) < 0:
                raise ValueError
            else:
                break
        except TypeError:
            print("Please enter valid Aadhar Number")
            continue
        except ValueError:
            print("Enter valid 4 digit Aadhar number")
            continue
        except EOFError:
            print("Please input something....")
            continue
    return int(aadhar)


def getAge(msg: str = "Enter Age: ") -> int:
    while True:
        try:
            age: str = input(msg)
            if age.isnumeric() != True:
                raise TypeError
            elif int(age) < 18:
                raise ValueError
            else:
                break
        except TypeError:
            print("Please enter valid Age")
            continue
        except ValueError:
            print("Age should be above 18 years old")
            continue
        except EOFError:
            print("Please input something....")
            continue
    return int(age)


def getVaccineTypes(msg: str = "Enter Vaccine Name: ") -> list[str]:
    vaccines: list[str] = []
    while True:
        clear()
        vaccines.append(input(msg))
        add: str = input("Do yo wish to add more Vaccines? (y/n): ")
        if add.lower() == "n":
            break
        elif add.lower() != "y":
            print("invalid choice\nNo more Vaccines will be added!")
            break
        else:
            pass
    return vaccines


def vaccineManagementMenu():
    while True:
        clear()
        choice = input(
            "\n---Vaccine Managemment System---\n\nMenu:\n(1) Insert Record\n(2) Display Record\n(3) Update Record\n(4) Delete Record\n(q) Quit programe: "
        )
        if choice == "1":
            with open(MAIN_FILE_NAME, "ab") as records:
                insert(records)
                while True:
                    yn = input("Do you want to add more records? (y/n/Y/N): ")
                    if yn.lower() == "n":
                        break
                    elif yn.lower() != "y":
                        print("Invalid choice. Please give a y/n answer.")
                    else:
                        insert(records)
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
            input("Press Enter to continue")


if __name__ == "__main__":
    vaccineManagementMenu()
