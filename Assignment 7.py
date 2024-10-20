


#Challenge: Handle cases where the user enters a non-numeric input for the year and provide appropriate error messages.
#Input:Prompt the user to enter a year.
##Processing: Determine whether the entered year is a leap year or not. Al eap year is divisible by 4 but not by 100 unless it is also divisible by 400.
#Output:Display whether the entered year is a leap year or not.



#Input: Prompt the user to enter a year
year_input = input("Enter a year: ")

#Error handling for non-numeric input
try:
    year = int(year_input)

    #Processing: Determine if the year is a leap year
    if year < 0:
        print("Please enter a valid postive year.")
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            #Output: Display if the year is a leap year
            print(f"{year} is a leap year.")
        else:
            #Output: Display of the year is not a leap year
            print(f"{year} is not a leap year.")

except ValueError:
    print("Invalid input. Please enter a numeric value for the year.")