groupmates = [
    {
        "name": "Игнатий",
        "surname": "Глушков",
        "exams": ["Философия", "ВвИТ", "АиГ"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Павел",
        "surname": "Пляго",
        "exams": ["История", "ЭВМ", "ВМ"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Демид",
        "surname": "Смирнов",
        "exams": ["РусЯз", "АнгЯз", "КГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Андрей",
        "surname": "Ковалёв",
        "exams": ["Философия", "Web", "Алгоритмы"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Александр",
        "surname": "Плешаков",
        "exams": ["ПИ", "История", "ВМ"],
        "marks": [5, 4, 5]
    }
]


def printStudentsAvarageScoreHigher(students, score):
    index = 0
    
    for student in students:
    
        marks = student["marks"]
        avarageScore = sum(marks)/len(marks)
        
        if avarageScore > float(score):
            index+=1
            print(str(index) + '.', student["surname"], student["name"])

while True:
    try:
        downScore = float(input("Введите нижний порог среднего балла студента: "))
        break
    except BaseException:
        ...
printStudentsAvarageScoreHigher(groupmates, downScore)

