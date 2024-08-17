import csv


def getData() -> list:
    data: list = []
    while True:
        empl: list = []
        empl.append(input("Enter employee ID: "))
        empl.append(input("Enter employee Name: "))
        empl.append(int(input("Enter employee Department Number: ")))
        empl.append(int(input("Enter Employee Salary: ")))
        data.append(empl)
        c = input("Would you like to enter more rows?(y/n) ")
        if c.lower() == "n":
            break
    return data


if __name__ == "__main__":
    c = input("Options\n1. Add Data\n2. Read Data\n")
    match c.lower():
        case "1":
            data = getData()
            head = ["eid", "ename", "dept no.", "salary"]
            with open("emp.csv", mode="w", newline="") as records:
                pen = csv.writer(records)
                pen.writerow(head)
                pen.writerows(data)
            print("Data Written")
        case "2":
            print("Reading Data...")
            with open("emp.csv", mode="r") as records:
                reader = csv.reader(records)
                for rec in reader:
                    print(rec)
        case _:
            print("Exiting Program")
    dept10 = []
    salaryInRange = []
    with open("emp.csv", mode="r") as records:
        reader = csv.reader(records)
        for rec in reader:
            if rec[2] == "10":
                dept10.append(rec)
            try:
                salary = int(rec[3])
                if salary >= 3000 and salary <= 5000:
                    salaryInRange.append(rec)
            except:
                pass

    print("\nEmployess from department 10:-")
    for i in range(len(dept10)):
        print(dept10[i])
    print("\nEmplyoyees whose salaries are in the range 3000-5000:-")
    for i in range(len(salaryInRange)):
        print(salaryInRange[i])
