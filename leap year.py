print("This is a little program that tells you if a year is a Leap year (Año bisiesto)")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    # It doesn't need check if year is 400 and 100 multiply because both are 4 multilply (4 * 100, 4 * 25)
    print("The year {year}, is a Leap Year")
else:
    print(f"The year {year}, is not a Leap Year")




