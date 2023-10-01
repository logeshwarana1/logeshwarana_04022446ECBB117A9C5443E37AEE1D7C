class student:

    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa =cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    return sorted_students

students = [
    student("logeshwarn","A123",8.5),
    student("kather","A124",8.7),
    student("mala","A125",9.3),
    student("rajakopal","A126", 9.8),
]
sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {}, Roll Number: {},CGPA: {}".format(student.name,student.roll_number,student.cgpa))
