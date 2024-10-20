


#Challenge:Write the function using recursion.
#Description:Create a function named is_palindrome that takes a string as input and returns True if it is a palindrome, and False otherwise.



def is_palindrome (s):
    #Convert the string to lowercase to make the check case-insensitive
    s = s.lower()

    #Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True

    #Recursive case: compare the first and last characters
    if s[0] == s[-1]:
        #Recursively call is_palindrome on the substring without the first and last characters
        return is_palindrome(s[1:-1])
    else:
        return False

#Input: Prompt the user to enter a string
user_input = input("Enter a string to check it it's a palindrome: ")

#Processing and Output: Check if the string is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome. ")
else:
    print(f"'{user_input}' is not a palindrome.")
