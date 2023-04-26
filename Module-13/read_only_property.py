class Student:
    def __init__(self, name, id, marks):
        self._name = name
        self.__id = id
        self.marks = marks
    @property
    def student_id(self):
        return self.__id

    def return_marks(self):
        return self.marks
    
    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name



arnob = Student("Arnob", 15, 55)
print(arnob.student_id)
# arnob.student_id = 77
print(arnob.student_id)
# del arnob.name 
# print(arnob.name)
print(dir(arnob))
