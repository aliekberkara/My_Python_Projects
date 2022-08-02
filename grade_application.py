from operator import le


def calculate_grade(line):
    line = line[:-1]
    list = line.split(":")
    name = list[0]
    grades = list[1].split(" ")
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    average = (grade1 + grade2 + grade3) / 3

    if average >= 90 and average <= 100:
        letter = "AA"
    elif average >= 85 and average <= 89:
        letter = "BA"
    elif average >= 75 and average <= 84:
        letter = "BB"
    elif average >= 70 and average <= 74:
        letter = "CB"
    elif average >= 60 and average <= 69:
        letter = "CC"
    elif average >= 55 and average <= 59:
        letter = "DC"
    elif average >= 50 and average <= 54:
        letter = "DD"
    elif average >= 45 and average <= 49:
        letter = "FD"
    else:
        letter = "FF"

    return name + ": " + letter + "\n"



def read_grades():
    with open("C:/Workspace/Python/Projeler/Dosya_Islemleri/grade_application.txt", "r", encoding="utf-8") as file:
        for i in file:
            print(calculate_grade(i), end="")


def enter_grade():
    name = input('Student Name: ')
    surname = input('Student Surname: ')
    grade1 = input('Grade1: ')
    grade2 = input('Grade2: ')
    grade3 = input('Grade3: ')

    with open("C:/Workspace/Python/Projeler/Dosya_Islemleri/grade_application.txt", "a", encoding="utf-8") as file:
        file.write(name + " " + surname + ":" + grade1 + " " + grade2 + " " + grade3 +"\n")


def save_grade():
    with open("C:/Workspace/Python/Projeler/Dosya_Islemleri/grade_application.txt", "r", encoding="utf-8") as file:
        list = []
        for i in file:
            list.append(calculate_grade(i))
        with open("C:/Workspace/Python/Projeler/Dosya_Islemleri/results.txt", "w", encoding="utf-8") as file2:
            for i in list:
                file2.write(i)

while True:
    process = input('1-Read Grades\n2-Enter Grade\n3-Save Grades\n4-Exit\n')

    if process == '1':
        read_grades()
    elif process == '2':
        enter_grade()
    elif process == '3':
        save_grade()
    elif process == '4':
        print('Exiting...')
        break
    else:
        pass