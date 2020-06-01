user_input = str(input('Enter a word:\n')).replace(" ", "")

if user_input[::-1] == user_input:
    print("It's a palindrome!")
else:
    print("Sorry, it is not a palindrome :(")