CORRECT_AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("👏 WELCOME TO THE WHOLESOME MACHINE 👏")
    while True:
        user_input = input("Please type the following afformation: "+ CORRECT_AFFIRMATION)
        if user_input == CORRECT_AFFIRMATION:
            print("Congratulation!!!🎉🎉    That's right!")
            break
        else:
            print("That was not the affirmation. .. Please type again")

if __name__ == "__main__":
    main()