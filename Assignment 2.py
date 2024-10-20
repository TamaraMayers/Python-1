


#Challenge:Implement error handling to ensure that the length and width entered by the user are positive numbers.
#Input:Ask the user to enter the length and width of a rectangle.
#Processing:Calculate the area of the rectangle using the formula:Area=Length*Width.
#Output:Display the calculated area of the rectangle.



#Input for 2 different variables

length = float(input("Enter the length of the rectangle: "))
width = float(input ("Enter the width of the rectangle: "))

#Error handling to ensure both values are positive numbers
if length <= 0 or width <= 0:
    print("Both length and width must be positive numbers greater than zero.")
else:
    #Processing the area of the rectangle
    area = length * width

    # This is the output for the area of the rectangle
    print("The area of the rectangle is:", area)