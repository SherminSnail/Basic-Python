quiz_number = int(input("Player 1, please enter the number to guess: "))
for i in range(0,25):
    print("")
number_of_attempts = 1
while True:
    input_number = input("Player 2: What is the number? \"give up\" to finish.")
    if input_number == "give up":
        break
    test_number = int(input_number)
    if test_number < quiz_number:
        print("Player 2: Your number is smaller than the searched number")
        number_of_attempts = number_of_attempts + 1
    elif test_number > quiz_number:
        print("Player 2: Your number is greater than the searched number")
        number_of_attempts += 1
    else:
        print(f"Eurika!!!: {quiz_number} is the number you are looking for. You have {number_of_attempts} Trials needed!")
        break