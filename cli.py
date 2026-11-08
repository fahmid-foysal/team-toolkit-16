
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculator():
    print("\n===== CLI Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid operation!")
        return

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print("Result:", result)


def unit_converter():
    print("\n===== Unit Converter =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Meters to Feet")
    print("8. Feet to Meters")

    choice = input("Choose a conversion (1-8): ")

    if choice == "1":
        celsius = get_number("Enter temperature in Celsius: ")
        result = (celsius * 9 / 5) + 32
        print("Result:", round(result, 2), "F")

    elif choice == "2":
        fahrenheit = get_number("Enter temperature in Fahrenheit: ")
        result = (fahrenheit - 32) * 5 / 9
        print("Result:", round(result, 2), "C")

    elif choice == "3":
        kilometers = get_number("Enter distance in kilometers: ")
        result = kilometers * 0.621371
        print("Result:", round(result, 2), "miles")

    elif choice == "4":
        miles = get_number("Enter distance in miles: ")
        result = miles * 1.609344
        print("Result:", round(result, 2), "km")

    elif choice == "5":
        kilograms = get_number("Enter weight in kilograms: ")
        result = kilograms * 2.20462
        print("Result:", round(result, 2), "lbs")

    elif choice == "6":
        pounds = get_number("Enter weight in pounds: ")
        result = pounds / 2.20462
        print("Result:", round(result, 2), "kg")

    elif choice == "7":
        meters = get_number("Enter length in meters: ")
        result = meters * 3.28084
        print("Result:", round(result, 2), "ft")

    elif choice == "8":
        feet = get_number("Enter length in feet: ")
        result = feet / 3.28084
        print("Result:", round(result, 2), "m")

    else:
        print("Invalid conversion! Please select 1-8.")


def main():
    while True:
        print("\n===== TEAM TOOLKIT =====")
        print("1. Calculator")
        print("2. Unit Converter")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            unit_converter()

        elif choice == "0":
            print("Exiting Team Toolkit...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
