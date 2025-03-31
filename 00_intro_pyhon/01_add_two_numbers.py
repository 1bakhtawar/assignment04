#Prompt the user to enter the first number.

def main():
    num1 = input("Enter the first number: ")
    num1 = int(num1)

    num2 = input("Enter the second number: ")
    num2 = int(num2)

    total_number = num1 + num2

    print(f"the sum of the two numbers is: {total_number}")

if __name__ == '__main__':
    main()