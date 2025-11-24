def find_min_max():
    print("Enter 'done' if you want finish you list")
    maximum_number = None
    minimum_number = None
    while True:
        user_input = input("Enter a number: ")
        if user_input == 'done':
            break
        try:
            number = float(user_input)
            if maximum_number is None:
                maximum_number = number
                minimum_number = number
            if number > maximum_number:
                maximum_number = number
            if number < minimum_number:
                minimum_number = number           
        except ValueError:
            print("Invalid input. Please enter a valid number")
            continue 
    if maximum_number is not None:
        print("Maximum Number entered:", maximum_number)
        print("Minimum Number entered:", minimum_number)
find_min_max()