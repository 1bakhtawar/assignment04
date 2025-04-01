def double(num):
    """Returns the input number multiplied by 2."""
    return num * 2

def main():
    num = int(input("Enter a number: "))
    doubled = double(num)
    print(f"Double that is {doubled}")

if __name__ == '__main__':
    main()