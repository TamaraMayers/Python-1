


#Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non=numeric input.
#Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated interactively by repeatedly applying the following rules:
#If the current number is even, divide it by 2.
#If the current number is odd, multiply it by 3 and add 1.




def get_valid_number():
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number <= 0:
                print("please enter a postiive integer greater than zero.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def generate_collatz_sequence(start):
    sequence = []
    while start != 1:
        sequence.append(start)
        if start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1
    sequence.append(1)  # Append the final 1 in the sequence
    return sequence

#Input: Get a valid positive integer from the user
number = get_valid_number()

#Processing: Generate the Collatz sequence
collatz_sequence = generate_collatz_sequence(number)

#Output: Display the Collatz sequence
print("The Collatz sequence is:", collatz_sequence)