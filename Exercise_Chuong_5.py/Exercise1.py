def process_numbers():
    total = 0.0
    count = 0
    while True:
        user_input = input("Enter a number: ")
        if user_input == 'done':
            break
        try:
            number = float(user_input)
            total = total + number
            count = count + 1
        except ValueError:
            print("Invalid input")
            continue 
    if count > 0:
        print(int(total), count, total/count)
process_numbers()