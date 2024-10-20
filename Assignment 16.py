


#Challenge:Optimize the function to handle large input numbers efficiently
#Description:Develop a function called is_prime that takes a positive integer and returns True if it is a prime number, and False otherwise.



def is_prime(n):
    #Handle cases where n is less than 2
    if n < 2:
        return False

    #Calculate the integer square root of n without using imports
    limit = int(n ** 0.5) + 1 #Equivalent to math.sqrt(n) + 1

    #Check divisibility from 2 up to the square root of n
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True

#Input: Prompt the user to enter a positive integer
number = int(input("Enter a positive integer: "))

#Processing and Output: Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")