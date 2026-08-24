
# ================ FUNCTIONS =====================

# 01. Celsius to Fahrenheit
def celcius_to_fahrenheit(celcius_temp):
    fahrenheit_temp = (celcius_temp * (9/5))+32
    return fahrenheit_temp


# 02. Celsius to Fahrenheit
def fahrenheit_to_celcius(fahrenheit_temp):
    celcius_temp = (fahrenheit_temp - 32) * (5/9)
    return celcius_temp


# 03. Celsius to Kelvin
def celcius_to_kelvin(celcius_temp):
    kelvin_temp = (celcius_temp + 273.15)
    return kelvin_temp


# 04. Kelvin to Celsius
def kelvin_to_celcius(kelvin_temp):
    celcius_temp = (kelvin_temp - 273.15)
    return celcius_temp


# 05. Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit_temp):
    kelvin_temp = ( (fahrenheit_temp - 32) * (5/9) ) + 273.15
    return kelvin_temp


# 06. Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin_temp):
    fahrenheit_temp = ( (kelvin_temp - 273.15) * (9/5) ) + 32
    return fahrenheit_temp 




# ================  FUNCTIONS CALL ===================
options = int(input('''
    Conversion Options:
        1. Celsius to Fahrenheit
        2. Fahrenheit to Celsius
        3. Celsius to Kelvin
        4. Kelvin to Celsius
        5. Fahrenheit to Kelvin
        6. Kelvin to Fahrenheit
    Select any options from above: '''))


# 1. Celsius to Fahrenheit
if options == 1:
    celcius = float(input("\n   Enter celcius temperature:  "))
    print(f"\n  Result: {celcius} Celcius = {celcius_to_fahrenheit(celcius)} Fahrenheit \n")

# 2. Fahrenheit to Celsius
elif options == 2:
    fahrenheit = float(input( "\n   Enter fahrenheit temperature : " ))
    print(f"\n  Result: {fahrenheit} Fahrenheit = {fahrenheit_to_celcius(fahrenheit)} Celcius \n")

# 3. Celsius to Kelvin
elif options == 3:
    celcius = float(input("\n   Enter celcius temperature:  "))
    print(f"\n  Result: {celcius} Celcius = {celcius_to_kelvin(celcius)} Kelvin \n")

# 4. Kelvin to Celsius
elif options == 4:
    kelvin = float(input("\n    Enter kelvin temperature: "))
    print(f"\n  Result: {kelvin} Kelvin = {kelvin_to_celcius(kelvin)} Celcius \n")

# 5. Fahrenheit to Kelvin
elif options == 5:
    fahrenheit = float(input( "\n   Enter fahrenheit temperature : " ))
    print(f"\n  Result: {fahrenheit} Fahrenheit = {fahrenheit_to_kelvin(fahrenheit)} Kelvin \n")

# 6. Kelvin to Fahrenheit
elif options == 6:
    kelvin = float(input("\n    Enter kelvin temperature: "))
    print(f"\n  Result: {kelvin} Kelvin = {kelvin_to_fahrenheit(kelvin)} Fahrenheit \n")


else:
    print("\n   Invalid Input")