


#Challenge:Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
#Input:Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
#Processing:Calculate the simple interest using the formula: Simple interest= (Principal*Rate*Time)/100.
#Output:Display the calculated simple interest.



#Input for  3 different variables

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

#Processing the simple interest

simple_interest = (principal * rate * time) / 100

#this is the output for simple interest
print("Simple interest is: ", simple_interest)

