# Lyle Osburne 9-19-2025
# Lab week 4 - This code is utilizes a function to calculate distance
# Distance is speed x time
# Formula: distance = speed * time

def distanceSpeedTime(speed,time):
    # Citation - URL: https://www.bbc.co.uk/bitesize/guides/z2ndmp3/revision/1
    # Citation - date Acessed: 9-18-
    distance = speed * time
    return distance

def main():
    speed = int(input("enter a value for speed in meters per second:"))
    time = int(input("enter a value for seconds of time: "))
    distance = distanceSpeedTime(speed,time)
    print("Value for speed:",speed,"meters per second")
    print("Value for time:",time,"seconds")
    print(f"The distance traveled is {speed} x {time} = " + str(distance) + "m")

if __name__ == "__main__":
    main()