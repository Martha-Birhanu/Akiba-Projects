Name=input("Enter Your Name: ")
Weight_kg=int(input(" Enter Your weight in kg: "))
Height_m=float(input(" Enter Your Height in m: "))


BMI= Weight_kg/(Height_m *Height_m)


print(f"==============================  \n     BMI REPORT \n============================== \n")

print(f"Name: {Name} \nWeight = {Weight_kg} kg\nHeight: {Height_m} m  \n\nBMI: {round(BMI,2)}")



print("============================== ")