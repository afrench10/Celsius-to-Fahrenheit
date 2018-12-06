#This script is dedicated to converting Celsius to Fahrenheit

#Gathering input from user for degrees Celsius
degree_c = input("How many degrees Celsius? \n")

#Converting the string input to a float output
degree_f = float(degree_c)
#Calculating the conversion from Celsius to Fahrenheit
degree_f = ((degree_f * 9 / 5) + 32)

#Printing the output, plus converting the float (degree_f) back to a string
#format so I can concatinate the 'degrees F.' at the end. I also added
#the initial input (degree_c) to make a more readable output.
print ((degree_c) + (" degrees Celsius is ") + (str(degree_f) + (" degrees Fahrenheit. \n")))

input("Press Enter to Exit.")
