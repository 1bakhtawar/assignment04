def main():
    num1 :int = int(input("Please enter an integer to be divided: "))
    num2 :int = int(input("Please enter an integer to be divided by : "))
    quotient :int = num1 // num2
    reminder :int = num1 % num2
    print(f"The result of this division is {quotient} with the reminder of {reminder}")
     
if __name__ == '__main__':
    main()