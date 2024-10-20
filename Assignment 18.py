


#Challenge: Ensure that the function works correctly with tuples of different lengths.
#Description: Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.



def concat_tuples(tuple1, tuple2):
    #Concatenate the two tuples using the + operator
    combined_tuple = tuple1 + tuple2

    #Return the concatenated tuple
    return combined_tuple

#Input: Prompt the user to enter two tuples (as space-separated values)
tuple1 = tuple(map(int, input("Enter the first tuple of elements separated by spaces: ").split()))
tuple2 = tuple(map(int, input("Enter the second tuple of elements separated by spaces: ").split()))

#Processing and Output: Concatenate the two tuples and display the result
result_tuple = concat_tuples(tuple1, tuple2)
print(f"Concatenated tuple: {result_tuple}")