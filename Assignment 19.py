


#Challenge:Implement the sorting algorithm without using any built-in sorting functions.
#Description:Develop a function called sort_list that takes a list of numbers as input and returns a new list containing the same elements sorted in ascending order.



def sort_list(numbers):
    #Get the length of the input list
    n = len(numbers)

    #Perform bubble sort
    for i in range(n):
        #Set a flag to check if any swagging happens
        swapped = False

        #Traverse the list from 0 to n-i-1 (last i elements are already sorted)
        for j in range(0, n-i-1):
            #Swap if the element is greater than the next element
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

        #If no swapping occurred in the inner loop, the list is already sorted
        if not swapped:
            break

    #Return the sorted list
    return numbers

#Input: Prompt the user to enter a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

#Processing and Output: Sort the list and display the result
sorted_numbers = sort_list(numbers)
print(f"Sorted list: {sorted_numbers}")