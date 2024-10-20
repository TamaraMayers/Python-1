


#Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
#Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.




def is_palindrome(s):
    #Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    left = 0
    right = len(s) - 1

    #Compare characters from both ends
    while left  < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

#Input: Prompt the user to enter a string
user_input = input("Enter a string to check if it's a palindrome: ")

#Processing: Check if the string is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
