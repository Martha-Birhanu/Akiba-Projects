

Amount_USD=int(input("Enter USD amount: "))

Exchange_Rate=150

Exchange_Rate_fromUser=input("Enter Exchange Rate:[or just hit enter to use the default]: ")


if Exchange_Rate_fromUser:
    Exchange_Rate=int(Exchange_Rate_fromUser)


Amount_in_ETB= Exchange_Rate * Amount_USD

print(f"==============================  \n     CURRENCY EXCHANGE \n==============================")

print(f"USD Amount: {Amount_USD} \n\nExchange Rate: 1 USD = {Exchange_Rate} ETB \n\nETB Amount: {Amount_in_ETB} ETB ")

print("============================== ")
