Student_name=input("Enter Student name: ")
Python_Score=int(input("Enter your python score: "))
English_Score=int(input("Enter your English score: "))
Mathematics_Score=int(input("Enter your Mathematics score: "))


Average= (Python_Score + English_Score + Mathematics_Score)/3



print(f"======================================== \n     STUDENT RESULT   \n======================================== ")

print(f"Student: {Student_name} \n\nPython:   {Python_Score} \nEnglish:   {English_Score}  \nMathematics: {Mathematics_Score}")
print(f"----------------------------------------  \n Average:   {round(Average,2)} \n========================================")