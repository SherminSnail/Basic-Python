
from marshal import version

input_wide = input("Please specify the width of the rectangle: ")
height = int(input_wide)
input_height = input("Please specify the height of the rectangle: ")
height = int(input_height)

number_of_numbers = int(input_wide) * int(input_height) #How many numbers do we need to draw in total?
counter_current_number = 1 #The counter for the current number
number_lengh = len(str(number_of_numbers))
print(number_lengh)

for i in range(0, int(input_height)):         #Run the entire height of the rectangle
    for j in range(0, int(input_wide)):    #Run a line of the rectangle with the given width
        print(" "*(number_lengh-len(str(counter_current_number))), end="") # Leading Spaces based on max number lengh - current number lengh
        print(counter_current_number, end="")
        print(" ", end="")
        counter_current_number += 1             #Increase the current number after it is output
    print("") #At the end of each line a return