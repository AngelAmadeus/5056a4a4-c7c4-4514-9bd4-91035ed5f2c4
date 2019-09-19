

class SchoolMember:
    ROLE = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"My name is {self.name} and I´m {self.age} years olf")

    def get_role(self):
        if not self.ROLE:
            raise NotImplementedError("Cannot get role from abstract")
        else:
            print(self.ROLE)


class Student(SchoolMember):

    ROLE = "Student"


class Professor(SchoolMember):

    ROLE = "Professor"


school_member = SchoolMember(name='A', age=22)
school_member.get_info()

student_a = Student(name='Student a',  age=23)
student_a.get_role()
