


#Challenge:Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
#Input:Ask the user to enter their marks for three subjects.
#Processing:Calculate the average of the marks. Determine the grade based on the average:
#90 abd above:A
#80-89:B
#70-79:C
#60-69:D
#Below 60:F
#Output:Display the calculated grade.



#Function to get valid marks between 0 and 100
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter  marks for {subject} (between 0 and 100): "))
            if 0 <= marks <=100:
                return marks
            else:
                print("Marks must be between 0 and 100. please try again. ")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Function to calculate the grade based on average
def calculate_grade(average):
     if average >= 90:
         return "A"
     elif 80 <= average < 90:
         return "B"
     elif 70 <= average < 80:
         return "C"
     elif 60 <= average < 70:
         return "D"
     else:
         return "F"

#Input: Get valid marks for three subjects
subject1 = get_valid_marks("Subject 1")
subject2 = get_valid_marks("Subject 2")
subject3 = get_valid_marks("Subject 3")

#Processing: Calculate the average marks
average_marks = (subject1 + subject2 + subject3) / 3

#Determine the grade based on the average
grade = calculate_grade(average_marks)

#Output: Display the calculated grade
print(f"Your average marks are: {average_marks:.2f}")
print(f"Your grade is {grade}")