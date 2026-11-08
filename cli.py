
def calculator():
    print("\n===== CLI Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

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

    else:
        print("Invalid operation!")


def unit_converter():
    print("\n===== Unit Converter =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")

    choice = input("Choose a conversion (1-4): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = (celsius * 9 / 5) + 32
        print("Result:", result, "F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = (fahrenheit - 32) * 5 / 9
        print("Result:", result, "C")

    elif choice == "3":
        kilometers = float(input("Enter distance in kilometers: "))
        result = kilometers * 0.621371
        print("Result:", result, "miles")

    elif choice == "4":
        miles = float(input("Enter distance in miles: "))
        result = miles * 1.609344
        print("Result:", result, "km")

    else:
        print("Invalid conversion!")


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
