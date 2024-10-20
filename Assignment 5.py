


#Challenge:Implement error handling to ensure that the user enters a non-negative number for the time duration.
#Input:Prompt the user to enter a time duration in hours.
#Processing:Convert the time duration to minutes and seconds.
#Output:Display the converted time duration in minutes and seconds.



#Input: Prompt the user to enter a time duration in hours
time_in_hours = float(input("Enter the time duration in hours: "))

#Error handling to ensure the user enters a non-negative number
if time_in_hours < 0:
    print("The time duration must be a non-negative number.")
else:
    #Processing: Convert the time duration to minutes and seconds
    time_in_minutes = time_in_hours * 60
    time_in_seconds = time_in_hours * 3600

    #Output: Display the converted time duration
    print(f"The duration is {time_in_minutes:.2f} minutes or {time_in_seconds:.2f} seconds.")