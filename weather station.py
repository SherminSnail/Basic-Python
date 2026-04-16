ext_input=input("Please enter temperatures for a week in the form \"Mon:23,Tue:-2, ...\": ")
temp_week = dict()
for tuple in text_input.split(","): #Run through all value pairs and divide at the decimal point
    temp_week[tuple.split(":")[0]] = int(tuple.split(":")[1]) #Split the key and the temperature and save it in the dict

while True:
    text_input = input("Please enter a weekday or average for the average temperature or exit to quit: ")
    if text_input == "exit": #Termination by the user
        break
    elif text_input == "average": #Calculation of the arithmetic mean
        average = 0
        for temp in temp_week.values():
            average += temp
        average /= len(temp_week)
        print("The average temperature is:", average)
    else: #Output of a single value
        print("On " + text_input + " the temperature was", temp_week.get(text_input))