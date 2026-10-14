


from person import teacher
from School import school

class subject:
    def __init__(self, name, teacher_obj):
        self.name = name
        self.teacher = teacher_obj
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evalute_exam()
            student.marks[self.name] = mark
            student.subject_grades[self.name] = school.calculate_grade(mark)
