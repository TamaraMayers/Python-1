


#Challenge: Optimize the function to handle large input lists efficiently
#Description:Develop a function called find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.



def find_common_elements(list1, list2):
    #Convert list1 to a set for efficient lookups
    set1 =set(list1)

    #Initalize an empty list to store common elements
    common = []

    #Loop through elements in list2 and check for common elements
    for element in list2:
        if element in set1:
            common.append(element)

    #Return the list of common elements
    return common

#Input: Prompt the user to enter two lists
list1 = input("Enter the first list of elements separated by spaces: ").split()
list2 = input("Enter the second list of elements separated by spaces: ").split()

#Processing and Output: Find and display common elements
common_elements = find_common_elements(list1, list2)
if common_elements:
    print(f"Common elements: {', '.join(common_elements)}")
else:
    print("No common elements found.")
