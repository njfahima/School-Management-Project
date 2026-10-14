

class school:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {} 
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher 

    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >= 60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks < 60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_gpa(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.0
        }
        return grade_map.get(grade, 0.0)    

    @staticmethod
    def value_to_grade(value):
        if value >= 4.5 and value <= 5.0:
            return 'A+'
        elif value >= 4.0 and value < 4.5:
            return 'A'
        elif value >= 3.5 and value < 4.0:
            return 'A-'
        elif value >= 3.0 and value < 3.5:
            return 'B'
        elif value >= 2.0 and value < 3.0:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self):
        result = f"School Name: {self.name}, Address: {self.address}\n\n"
        
        result += "Classrooms:\n"
        for key in self.classrooms.keys():
            result += f"- {key}\n"

        result += "\n--- All Students ---\n"
        for key, value in self.classrooms.items():
            result += f"--- {key.upper()} classroom Students\n"
            for student in value.students:
                result += f"    {student.name} (ID: {student.id})\n"

        result += "\n--- All Subjects ---\n"
        for key, value in self.classrooms.items():
            result += f"--- {key.upper()} classroom Subjects\n"
            for sub in value.subjects:
                result += f"    {sub.name}\n"

        result += "\n--- Student Results ---\n"
        for key, value in self.classrooms.items():
            result += f"--- {key.upper()} classroom Results ---\n"
            for student in value.students:
                for k, i in student.marks.items():
                    result += f"    {student.name} | {k}: Marks={i}, Grade={student.subject_grades.get(k)}\n"
                result += f"    {student.calculate_final_grade()}\n"
                
        return result