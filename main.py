# Programmers:  Zain Huda, Hazel Osborne
# Course:  CS151
# Due Date: Oct. 2nd 2024
# Lab Assignment: Lab 03
# Problem Statement:  Determine Points and Distance Traveled based on Hill Type and Jumpers Speed
# Data In: Jumper's Speed, Hill Type
# Data Out:  Points, Distance, Message

import math

  #Prompt user to enter hill type and speed and height
hill_type = str(input("Which hill type did you ski on? Normal or Large?" ))
speed = float(input("What was your speed?"))

#Define par, points, and height
par = 0
points_per_meter = 0
height = 0

  #Determine par and points per meter based off of hill type.
if hill_type == "Normal" :
      par = 90
      points_per_meter = 2
      height = 46


elif hill_type == "Large" :
    par = 120
    points_per_meter = 1.8
    height = 70

else:
    print("Invalid hill type")

 # Calculate Time in Air
time_in_air = math.sqrt((2 * height) / 9.8)

# Calculate Distance
distance = speed * time_in_air

# Calculate Points Earned
points_earned = 60 + (distance - par) * points_per_meter

#Round up distance and points earned
distance = math.ceil(distance)
points_earned = math.ceil(points_earned)

#Determine output message.
if points_earned >= 61:
    print("Great job for doing better than par!")
elif points_earned > 10:
    print("What happened??")
else:
    print("Sorry you didn't go very far.")

#Output distance and points earned
print("You traveled", distance,".")

print("Your points are", points_earned,".")