run = True
while run:

    print("Python Palindrome Checker. Type 'help' for more information")

    user_input = str(input('Enter a word/sentence:\n')).replace(" ", "")


    try:

        if user_input[::-1] == user_input:
            print("It's a palindrome!")

        elif user_input == 'exit' or user_input == 'quit':
            print("Goodbye")
            run = False

        elif user_input == 'help' or user_input == 'quit':
            print("A palindrome is a word or sentence such that when it is reversed it is the same as the original word or sentence. Example: Do geese see god ")

        else:
            print("Sorry, it is not a palindrome :(")

    except Exception as e:
        print("We are sorry, an error occured :( \n")

        print(e)