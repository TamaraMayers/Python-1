


#Challenge:Handle negative exponents efficiently.
#Description:Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.



def power(base, exponent):
    #Handle the case where the exponent is negative
    if exponent < 0:
        return 1 / power(base, -exponent)

    #Handle the base case where the exponent is 0
    if exponent ==0:
        return 1

    #Recursively calculate base raised to the exponent
    result = 1
    for _ in range(exponent):
        result *= base
    return result

#Input:Prompt the user to enter the base and exponent
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

#Processing and Output: Calculate base^exponent and display the result
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
