


#Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.
#Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.




def get_valid_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_character(prompt):
    while True:
        char = input(prompt)
        if len(char) != 1:
            print("please enter a single character.")
        else:
            return char

#Input: Get the number of rows for the pattern
rows = get_valid_integer("Enter the number of rows for the pattern: ")

#Input: Get the character to use for the pattern
pattern_char = get_valid_character("Enter the character to use for the pattern: ")

#Processing: Print the pattern using nested loops
for i in range(1, rows + 1):
    for j in range (i):
        print(pattern_char, end='')
    print() #Move tp the next line after printing each row