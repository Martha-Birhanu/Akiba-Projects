Destination=input("Enter your destination: ")
Distance_KM=float(input("Enter the distance in kilometers: "))
Average_Speed=float(input("Enter Average Speed in Km/h: "))


Time = Distance_KM/Average_Speed

time_hr = int(Time)

minutes= int((Time - time_hr) * 60)

print(f"Destination: {Destination} \nDistance: {Distance_KM} km \nAverage Speed: {Average_Speed} km/h \n\nEstimated Travel Time: {time_hr} hours and {minutes} min. ")

