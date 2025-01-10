#Create a Student class with attributes for name, age,
#and grades. Include methods to display details and
#calculate the average grade.

class Student:
  
   def Initialization(self,name,RollNo, M1,M2,M3,avgrage): # Here M1,M2,M3,M4,M5. Are refered to Marks in 5 subject 
     self.name =  name
     self.RollNo  =  RollNo
     self.M1   =  M1
     self.M2   =  M2
     self.M3   =  M3
     self.avgrage = avgrage
    
   def __str__(self):
      return f"name: {self.name} , RollNo:{self.RollNo} ,M1:{self.M1},M2:{self.M2},M3:{self.M3}, avgrage:{self.avgrage}"# This line is used to produce meaningfull   string representation 
    
class StudentManager:
  def __init__(self):
     self.student = []    # =[] is an empty list. This list can hold multiple student object allowing the program to manage a collection of students.
                          # i.e. It can hold multiple values 
def accept(self, name, rollno, marks1, marks2):
        """Accept and add a new student."""
        student = Student(name, rollno, marks1, marks2)
        self.students.append(student)