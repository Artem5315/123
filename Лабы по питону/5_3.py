'''Создать класс Student, предназначенный для обработки информации о
студентах группы (фамилия, имя, средний балл).
Конструктор класса должен задавать значения для трех атрибутов – surname, name
и ball. Атрибут ball по умолчанию должен быть «8».
Класс должен содержать метод вывода информации о студенте в виде:
Фамилия: Иванов, имя: Иван, средний балл – 8
Класс должен содержать метод для вывода общей численности студентов в
виде:
На данный момент всего студентов – 24
Создать несколько экземпляров класса Student.'''
import datetime
class Student:
    students_count = 0

    def __init__(self, surname, name, ball=8):
        self.surname = surname
        self.name = name
        self.ball = ball
        Student.students_count += 1

    def info(self):
        print(f"Фамилия: {self.surname}, имя: {self.name}, средний балл – {self.ball}")

    @staticmethod
    def total_students():
        print(f"На данный момент всего студентов – {Student.students_count}")

student1 = Student ("shilko", "artem",8)
student2 = Student ("sitko", "Andrey",5)
student3 = Student ("tvorovskiy", "vlad",10)
student4 = Student ("sadfasdg", "adsfa",2)
student1.info()
student2.info()
student3.info()
student4.info()
Student.total_students()
