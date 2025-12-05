# Lyle Osburne 9-18-2025
# Lab week 3 - This code is used to calculate distance
# Distance is speed x time
# Formula: distance = speed * time
# Citation - URL: https://www.bbc.co.uk/bitesize/guides/z2ndmp3/revision/1
# Citation - date Acessed: 9-18-2025

speed = int(input("enter a value for speed in meters per second:"))
time = int(input("enter a value for seconds of time: "))

distance = speed * time

print("Value for speed:",speed,"meters per second")
print("Value for time:",time,"seconds")
print(f"The distance traveled is {speed} x {time} = " + str(distance) + "m")