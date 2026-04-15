names = ["Thomas", "Sebastian", "Rudolf", "Henry", "Christian"]

text_input = int(input("Please enter a position from 1 to 5, with 0 output all names: "))

if text_input == 0:
    print(names)
else:
    print(names[text_input-1])