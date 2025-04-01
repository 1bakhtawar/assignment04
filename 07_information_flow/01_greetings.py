def greet(name: str) -> None:
    """Prints a greeting with the given name"""
    print(f"Greetings {name}!")

def main():
    # Get user's name
    name = input("What's your name? ")
    
    # Greet the user
    greet(name)

if __name__ == '__main__':
    main()