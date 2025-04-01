import random 

def my_num():
    secret_num = random.randint(1,100)
    print("I am thinking of a number between 1 and 100...")

    guess = int(input("Enter a guess: ")) 

    while guess != secret_num:
        if guess < secret_num:
            print("Your guess is too low.")
        else:
            print("Your gues is not high")
        guess = int(input("Enter a guess: "))

    print("Congrats! The number was: " + str(secret_num))

if __name__ =='__main__':
    my_num()