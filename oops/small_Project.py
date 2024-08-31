class Student:
    def __init__(self,name,roll_Number,Class):
        self.name = name
        self.roll_Number = roll_Number
        self.Class= Class
        self.marks = {}
        
    def add_Marks(self,subject,marks):
        if subject in self.marks:
            print(f"{self.marks} already marks exist for {subject}")
        else:
            self.marks[subject] = marks
    
    def calculate_Averarge(self):
        
        if not self.marks:
            print(f"There is no avilable marks")
            
        else:
            all_mark = sum(self.marks.values())
            average = (all_mark/len(self.marks))
            return average
    
    def showDetails(self):
        print(f"name : {self.name}")
        print(f"Roll Number  : {self.roll_Number}")
        print(f"Class  : {self.Class}")
        print(f"Marks : {self.marks}")
        print(f"Average  : {self.calculate_Averarge()}")
        
        
stu1 = Student("Ayush" , 1,"10th")
stu2 = Student("Lakshit", 2,"10th")

stu1.add_Marks("Math",98)
stu1.add_Marks("science",95)

stu2.add_Marks("english", 97)
stu2.add_Marks("Hindi",90)

stu1.showDetails()