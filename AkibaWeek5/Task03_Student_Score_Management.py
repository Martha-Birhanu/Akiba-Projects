class Student:
    school_name="Akiba Academy"

    def __init__(self,name,score,department):
        self.name=name
        self.score=score
        self.department=department


    def display(self):
        print(f"student name: {self.name}\nDepartment: {self.department}\nScore: {self.score}")
        

print(Student.school_name)
s1=Student("Ali",98,"Software")
s2=Student("Eyu",99,"Cs")
s3=Student("sina",97,"Electrical")

print("Before updating s2 score")

s1.display()
s2.display()
s3.display()

s2.score=100 # type: ignore             here i update the score of the s2 and it prints out the updated score but the score of the remainind students don't change.
print("After updating s2 score")

s1.display()
s2.display()
s3.display()


       # Question number1
# The difference between class attribute and instance attribute
# the class attribute belongs to the class and is shared by all abjects
# while instance attribute belongs to a specific object.
        
       # Question number2
# updating one students score doesn't change the score of other student 
# because every student are a separate objects so they have their own instance attribute

