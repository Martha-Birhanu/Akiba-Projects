def validate_score(students):
    for student in students:
        if student["score"]<1 or student["score"]> 100:
             return f"Invalid score detected for {student['name']}: {student['score']}"
        else:
            return True


def Calculate_grade(students):
    grades={}
    for student in students:
        if 90<=student["score"]<=100:
            grades[student["name"]]="A"
        elif 80<=student["score"]<=89:
            grades[student["name"]]="B"
        elif 70<=student["score"]<=79:
            grades[student["name"]]="C"
        elif 60<=student["score"]<=69:
            grades[student["name"]]="D"
        else:
            grades[student["name"]]="F"
    return grades
def Average_score(students):
    sum =0
    lst=[]
    for student in students:
        sum = sum + student["score"]
    Average=sum/len(students)
    for student in students:
        if student["score"] > Average:
            lst.append(student["name"])
    return f"Average score ={round(Average,2)} \nThe list of students scored above average: {lst}"


def Highest_and_Lowest(students):
    highest=students[0]["score"]
    lowest=students[0]["score"]
    for student in students:
        if student["score"] > highest:
            highest=student["score"]

        if student["score"] < lowest:
            lowest=student["score"]

    return f"The highest score : {highest} \nThe lowest score: {lowest}"

def passed_and_failed(students):
    passed=0
    failed=0

    for student in students:
        if student["score"] < 50:
            failed +=1
        else:
            passed+=1

    if passed >1 and failed >1:
        return f"{passed} students passed.\n{failed} students failed"
    elif passed >1 and failed ==1:
        return f"{passed} students passed.\n{failed} student failed"
    elif failed >1 and passed ==1:
        return f"{passed} student passed.\n{failed} students failed"  

    return f"{passed} student passed.\n{failed} student failed"



def Generate_report(students):

    validation=validate_score(students)
    if validation is True: 
        print("=========================")
        print("      Class Report       ")
        print("=========================")
        average=Average_score(students)
        passedFailed=passed_and_failed(students)
        highestLowest = Highest_and_Lowest(students)
        grade=Calculate_grade(students)
    

        print(average)
        print(passedFailed)
        print(highestLowest)
        print("Grades:",grade)
    else:
        print(validation)

students_lst = []
n= int(input(" How many Students do you want to enter:"))
for i in range(n):
    name=input("Enter name of student: ")
    score=int(input(f"enter score of {name}: "))
    students_lst.append({"name": name, "score": score})

Generate_report(students_lst)