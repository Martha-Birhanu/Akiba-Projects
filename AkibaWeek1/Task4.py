Temp_in_Celsius= float(input("Enter Temperature in Celsius: "))


Fahrenheit = (Temp_in_Celsius * 9/5) + 32


Celsius_Unit="\u00b0C"

print(f"Celsius: {Temp_in_Celsius}{Celsius_Unit} \nFahrenheit: {round(Fahrenheit,2)}F")



Temp_in_Fahrenheit= float(input("Enter Temperature in Fahrenheit: "))

Celsius = (Temp_in_Fahrenheit - 32) * 5/9

print(f"Fahrenheit: {Temp_in_Fahrenheit}F \nCelsius: {round(Celsius,2)}{Celsius_Unit}")