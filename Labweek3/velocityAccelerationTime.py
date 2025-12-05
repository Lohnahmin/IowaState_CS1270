# Lyle Osburne 9-18-2025
# Lab week 3 - This code is used to calculate initial velocity
# velocity calculator uses the equation that the final velocity of an object is equal to its initial velocity added to its acceleration multiplied by time of travel
# Formula: initial_velocity + (acceleration * time)
# Citation - URL: https://www.calculatorsoup.com/calculators/physics/velocity_a_t.php
# Citation - Date Posted: 08/01/2025
# Citation - Date Acessed: 9-18-2025

initial_velocity = int(input("enter value for 'initial velocity':"))
acceleration = int(input("enter value for 'acceleration':"))
time = int(input("enter value for 'time':"))
 
final_velocity = initial_velocity + (acceleration * time)

print("Value for initial_velocity:",initial_velocity,"meters per second")
print("Value for acceleration:",acceleration,"meters per second squared")
print("Value for time:",time,"seconds")
print(f"The final velocity is {initial_velocity} + ({acceleration} x {time}) = ", str(final_velocity),"meters per second")