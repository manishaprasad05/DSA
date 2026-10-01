#create student class and 4 variable -rollno,name,program,semester

class Student:
    def __init__(self):
        self.rollno=0
        self.name=""
        self.program=""
        self.sem=0

    def get_Data(self):
        self.rollno=int(input("Enter Your Roll No:"))
        self.name=input("Enter Your Name:")
        self.Program=input("Enter Program Name:")
        self.sem=int(input("Enter Semester:"))
    
    def put_Data(self):
        print("======= Student Information =======")
        print(f"Student Rollno: {self.rollno}")
        print(f"Student Name: {self.name}")
        print(f"Student Program: {self.program}")
        print(f"Student Semester: {self.sem}")


student1 = Student()
student1.get_Data()
student1.put_Data()
    
    
    
