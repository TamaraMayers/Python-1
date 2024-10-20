


#Challenge:Implement error handling to ensure that the user enters a positive integer for the age.
#Input:Prompt the user to enter their age.
#Processing:Classify the age into different categories:
#Under 18:Minor
#18-65: Adult
#Above 65: Senior citizen
#Output:Display the category based on the entered age.



#Function to get a valid positive integer for the age
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Please enter a positive integer for age.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

#Function to classify the age into categories
def classify_age(age):
    if age < 18:
        return"Minor"
    elif 18 <= age <= 65:
        return "Adult"
    else:
        return "Senior citizen"

#Input: Ask the user to enter their age
age = get_valid_age()

#Processing: Classify the age into categories
category = classify_age(age)

#Output: Display the category based on the entered age
print(f"based on your age, ypu are classified as: {category}")