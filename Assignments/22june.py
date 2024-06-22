### write a programe to add student details in a binary file and display those students whose marks are above 70.

import pickle
import os


def clear() -> None:
    os.system("cls")


def StudentInfo(file: str) -> None:
    students: list[list[str]] = []
    with open(file, "wb") as fw:
        while True:
            clear()
            choice = input("Do you want to add Student information:(y/n) ")
            if choice == "n" or choice == "N":
                clear()
                break
            elif choice == "y" or choice == "Y":
                clear()
                student: list[str] = []
                student.append(input("Enter Student Roll Number: "))
                student.append(input("Enter Student Name: "))
                student.append(input("Enter Marks obtained: ") + "\n")
                students.append(student)
            else:
                print("Invalid Choice")
        pickle.dump(students, fw)
        print("data Written")


def studentsAbove70(file: str) -> None:
    studentabv70: list[str] = []
    with open(file, "rb") as fr:
        students = pickle.load(fr)
        for student in students:
            if int(student[2]) > 70:
                studentabv70.append(student)

    print("list of students above 70 marks:\n", studentabv70)


if __name__ == "__main__":
    StudentInfo("studentdata.dat")
    studentsAbove70("studentdata.dat")
