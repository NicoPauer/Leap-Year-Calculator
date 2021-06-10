print("This is a little program that tells you if a year is a Leap year (Año bisiesto)")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
    
            print("The year {year}, is a Leap Year")

        else:
            print("The year {year}, is not a Leap Year")
        

    else:
            print("The year {year}, is a Leap Year")

else:
    print(f"The year {year}, is not a Leap Year")




