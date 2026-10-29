Units= int(input("Enter Units: "))

def Charge_for_each_tier():
    
    if Units<=0:
            return "Enter Valid Units Consumed."
    if Units<=50:
            Total_bill=50*0.50 
            return f"First 50 units:  50*0.05ETB = {Total_bill} ETB"
    
    if 51<=Units<=150:
            First_50Pricing=50*0.50
            Next_100Pricing=(Units-50)*0.75
            
            return f"First 50 units:  50*0.05ETB = {First_50Pricing} ETB \nRemaining {Units-50} units: {Units-50} * 0.75ETB {Next_100Pricing} ETB"
    if Units>150:
            First_50Pricing=50*0.50
            Next_100Pricing=100*0.75
            RemainingPricing=(Units-150)*1.20
            return f"First 50 units: 50*0.05ETB = {First_50Pricing} ETB \nNext 100 units: 100*0.75ETB = {Next_100Pricing} ETB \nThe remaining {Units-150} units: {Units-150}*1.20ETB = {RemainingPricing} ETB"

def Billing_system(serviceFee):
    
    if Units<=0:
        return "Enter Valid Units Consumed."
    if Units<=50:
        Total_bill=50*0.50 + serviceFee
        return f"{Total_bill} ETB"

    if 51<=Units<=150:
        First_50Pricing=50*0.50
        Next_100Pricing=(Units-50)*0.75
        Total_bill=First_50Pricing+Next_100Pricing+serviceFee
        return f"{Total_bill} ETB"
    if Units>150:
        First_50Pricing=50*0.50
        Next_100Pricing=100*0.75
        RemainingPricing=(Units-150)*1.20
        Total_bill=First_50Pricing+Next_100Pricing+RemainingPricing+serviceFee
        return f"{Total_bill} ETB"

def options ():
      while True:
            print(f"1. Charge for each tier \n2. Total Bill \n3. Exit")
            ChooseOption=(input("Choose Option: "))
            if ChooseOption == "1":
                  print(Charge_for_each_tier())
            elif ChooseOption == "2":
                  print(Billing_system(20))
            elif ChooseOption == "3":
                  break
            else:
                  print("Invalid option!")
options ()
