def print_multiple(message: str, repeats: int) -> None:
 
    for _ in range(repeats):
        print(message, end=' ')
    print()  # Add newline after all repetitions

def main():
    message = input("\033[94m Please type a message: \033[0m")
    repeats = int(input("\033[94mEnter a number of times to repeat your message: \033[0m"))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()