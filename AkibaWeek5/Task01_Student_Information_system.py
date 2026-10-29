class Student:
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department

    def Display_info(self):
        print(f"student name: {self.name}\nAge: {self.age}\nDepartment: {self.department}")


s1=Student("Hana",23,"Software Engineering")
s2=Student("Alem",24,"Computer Science")
s3=Student("Eyob",25,"Electrical")

s1.Display_info()
s2.Display_info()
s3.Display_info()