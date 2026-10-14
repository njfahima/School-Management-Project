


import random
import School

class person:
    def __init__(self, name) -> None:
        self.name = name

class teacher(person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evalute_exam(self):
        return random.randint(0, 100)

class student(person):
    def __init__(self, name, age, gender, classroom) -> None:
        super().__init__(name)
        self.age = age
        self.gender = gender
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grades = {}
        self.grade = None

    def calculate_final_grade(self):
        total_points = 0
        for grade in self.subject_grades.values():
            point = School.school.grade_to_gpa(grade) # Corrected method name
            total_points += point
            
        if len(self.subject_grades) == 0:
            gpa = 0.0
            self.grade = 'F'
        else:
            gpa = total_points / len(self.subject_grades)
            self.grade = School.school.value_to_grade(gpa)
            
        return f"{self.name} , final GPA: {gpa:.2f} , Final Grade: {self.grade}"

    @property
    def id(self):
        return self.__id  

    @id.setter
    def id(self, value):
        self.__id = value