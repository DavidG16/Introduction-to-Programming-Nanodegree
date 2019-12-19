

def valid_input(message):
    choice = input(f'{message} \n').lower()
    if choice == '1':
        return choice
    elif choice == '2':
        return choice
    else:
        print("Please enter 1 or 2.")
        return valid_input(message)


c = valid_input("Give me something:\n")
print(type(c))
