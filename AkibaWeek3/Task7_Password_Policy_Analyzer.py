
def minimum_length (password,minimumLength):
    if len(password) < minimumLength:
        return {"requirement": "Minimum length", "status": "Failed", "detail": f"passsword atleast{minimumLength} characters long."}
    return {"requirement": "Minimum length" , "status": "Passed", "detail": "passsword length is enough."}


def Uppercase_Lowercase(password):
    if password.isupper():
        return {"requirement": "UpperCase and LowerCase", "status": "Failed", "detail": "your passsword has only uppercase letters."}
    elif password.islower():
        return {"requirement": "UpperCase and LowerCase", "status": "Failed", "detail": "your passsword has only lowercase letters."}
    return {"requirement": "UpperCase and LowerCase", "status": "Passed", "detail": "your passsword did contain both uppercase and lowercase letters."}


def Digits(password):
    if any(char.isdigit() for char in password):
        return {"requirement": "Digits", "status": "Passed", "detail": "Password did contain digits."}
    return {"requirement": "Digits", "status": "Failed", "detail": "Password must contain at least one digit."}

def Special_characters(password):
    if any(not char.isalnum() for char in password):
        return {"requirement": "Special Characters", "status": "Passed", "detail": "your Password did contain special characters."}
           
    return {"requirement": "Special Characters", "status": "Failed", "detail": "your Password didn't contain special characters."}


def analyze_password(password,minimunLength):
    results=[]
    results.append(minimum_length(password,minimunLength))
    results.append(Uppercase_Lowercase(password))
    results.append(Digits(password))
    results.append(Special_characters(password))
    return results

user_password=input("Enter your password: ")
Analysis=analyze_password(user_password,8)
print(f"Analysis Report \n============================= ")

for a in Analysis:
    print(f"{a["requirement"]}: {a["status"]}, {a["detail"]}")



