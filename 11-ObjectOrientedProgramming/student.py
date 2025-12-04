# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.number = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.number = 11234
    student2.name = "Olivia"
    student2.age = 21
    student2.number = 345678
    student3.name = "Anna"
    student3.age = 20
    student3.number = 685496

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, number of album: {student1.number}')
    print(f'{student2.name}, {student2.age} years old, number of album: {student2.number}')
    print(f'{student3.name}, {student3.age} years old, number of album: {student3.number}')

if __name__ == "__main__":
    main()