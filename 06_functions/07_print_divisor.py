def print_divisors(num):

    print(f"Here are the divisors of {num}", end=' ')
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')
    print()  

def main():
    num = int(input("\033[94mEnter a number: \033[0m"))
    print_divisors(num)

if __name__ == '__main__':
    main()