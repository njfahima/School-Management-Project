


from School import school
from person import student, teacher
from subject import subject
from classroom import Classroom

School = school("ABCDEFGH", "Dhaka, Bangladesh")

#adding classrooms
eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

School.add_classroom(eight)
School.add_classroom(nine)
School.add_classroom(ten)

#adding student (passing name, age, gender, classroom)
fahima = student("Fahima", 12, "Female", eight)
ifran = student("Ifran", 13, "Male", nine)
nur = student("Nur", 14, "Male", ten)
washifa = student("Washifa", 12, "Female", eight)

School.student_admission(fahima)
School.student_admission(ifran)
School.student_admission(nur)
School.student_admission(washifa)

#adding teacher
nondo = teacher("Nondo")
supro = teacher("Supro")
nitu = teacher("Nitu")
jibon = teacher("Jibon")

#adding subjects
bangla = subject("Bangla", nondo)
english = subject("English", supro)
math = subject("Math", nitu)
science = subject("Science", jibon)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(math)
eight.add_subject(science)

nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(math)
nine.add_subject(science)

ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(math)
ten.add_subject(science)

eight.take_semester_exam()
nine.take_semester_exam()
ten.take_semester_exam()

print(School)