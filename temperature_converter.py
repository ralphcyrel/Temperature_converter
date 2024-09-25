#will ask the user to choose temperature C or F
while True:
    temp_choice = input("Type 'C' to convert Celsius to Fahrenheit and Type 'F' to convert Fahrenheit to Celsius: ")
#will ask the user to input temperature for conversion
    if temp_choice == 'C':
        celsius = float(input("Enter the Temperature in Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print("The Temperature in Fahrenheit is:", fahrenheit)
    elif temp_choice == 'F':
        fahrenheit = float(input("Enter the Temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("The Temperature in Celsius is: ", celsius)
#will ask the user to try again