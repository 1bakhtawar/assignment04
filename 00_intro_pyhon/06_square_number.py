def main():
    num: float = float(input("\033[1;3mEnter a number for square: \033[0m "))
    square = num * num 
    print(f"\033[1;3mThe square of {num} is : {square} \033[0m ")

if __name__ == '__main__':
    main()