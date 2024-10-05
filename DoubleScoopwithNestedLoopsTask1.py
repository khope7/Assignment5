#Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week.
# Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day.
# For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.
#Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

#Writing code for mood tracker

#Copying mood list from TheRangeRiddleTask1
moods = ["Happy", "Sad", "Energetic", "Calm"]

#Creating list for each day of the week
dayofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Creating list for time of day
timeofday = ["morning", "afternoon", "evening"]

#Importing random
import random

#Creating code to show for day of week along with random time and random mood along a single line print
for today in dayofweek:
   for time in range(1):
        time_today = random.choice(timeofday)
        for mood in range(1):
            mood_today = random.choice(moods)
            print("On " + today , time_today + " I was " + mood_today + ".")
