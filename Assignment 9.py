


#Challenge:Ensure that the user enters only a single character and handle cases where the input is not a letter.
#Input:Ask the user to enter a single character.
#Processing:Determine whether the entered character is a vowel (a,e,i,o,u) or a consonant.
#Output:Display whether the entered character is a vowel or a consonant.



#Function to check if the input is a valid single character and a letter
def get_valid_character():
    while True:
        user_input = input("Enter a single character: ")

        if len(user_input) != 1:
            print("Please enter only one character." )
        elif not user_input.isalpha():
            print("Invalid input. Please enter a letter." )
        else:
            return user_input.lower()

#Fuction to determine if the character is a vowel or consonant
def check_vowel_or_consonant(char):
    vowels = 'aeiou'
    if char in vowels:
        return "vowel"
    else:
        return "consonant"

#Input: Ask the user for a single character
character = get_valid_character()

#Processing: Determine if the character is a vowel or consonant
result = check_vowel_or_consonant(character)

#Output: Display whether the character is a vowel or consonant
print(f"The character '{character}' is a {result}." )