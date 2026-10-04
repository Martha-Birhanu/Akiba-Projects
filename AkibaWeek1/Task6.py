Employee_name = input("Enter Employee Full name: ")
Basic_Salary = int(input("Enter Basic Salary: "))
Transport_Allowance = int(input("Enter the Allowance for Transport: "))
Food_Allowance=int(input("Enter the Allowance for Food: "))


Gross_Salary = Basic_Salary + Transport_Allowance + Food_Allowance


print("========================================")
print("        EMPLOYEE PAYSLIP")
print("========================================\n")


print(f"""Employee: {Employee_name} \n\nBasic Salary:   {Basic_Salary} \nTransport Allowance: {Transport_Allowance} 
Food Allowance: {Food_Allowance} \n---------------------------------------- \nGross Salary: {Gross_Salary} 
========================================""")