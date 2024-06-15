fw = open("Employees_data.txt", "a")
employee: list[str] = []
while True:
    emp: str = ""
    c = input("Add Employee data(Y/N): ")
    if c == "N" or c == "n":
        fw.writelines(employee)
        fw.close()
        break
    elif c != "Y" and c != "y":
        print("invalid choice")
    else:
        id: str = input("Enter Employee ID: ")
        emp += id + ","
        name: str = input("Enter Employee Name: ")
        emp += name + ","
        dept: str = input("Enter Employee Department: ")
        emp += dept + ","
        salary: str = input("Enter Employee Salary: ")
        emp += salary + "\n"
        employee.append(emp)
print("Data recorded")
