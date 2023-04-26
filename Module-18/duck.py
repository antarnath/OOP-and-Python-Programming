class Teacher:
    def __init__(self, name):
        self.teacherName = name
        self.students = []

    def entry_student(self, studentObj):
        self.students.append(studentObj)


class Student:
    def __init__(self, name):
        self.studentName = name

    def enter_in_a_teacher(self, teacherObj):
        teacherObj.students.append(self)

    def __repr__(self):
        return f'Student({self.studentName})'

rahim_mia = Teacher('Rahim Mia')
ms_rahima = Teacher("Rahim Mia")
solaiman_sir = Teacher("Solaiman Mia")
student = Student("rahim")
student.enter_in_a_teacher(rahim_mia)
student.enter_in_a_teacher(ms_rahima)
print(rahim_mia.students)
print(ms_rahima.students)