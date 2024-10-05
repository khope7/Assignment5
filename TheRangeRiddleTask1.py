#Task 1: Your Mood Today Write a program that prints off different moods for each day of the week.
#Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it.
#Ensure that your program includes the use of the random module to select the mood

#Writing code for moods

#Importing random gen
import random

#Creating list for moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

#Created ranged random loop to randomly select mood for days 1-7 of the week and printing
for day in range(7):
    mood_today = random.choice(moods)
    print(f"For day {day + 1}: My mood is {mood_today}.")