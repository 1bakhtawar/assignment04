def count_even(numbers):  
    count = 0 
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print(count)

def get_list_of_ints():
    lst = []  
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)  

if __name__ == '__main__':
    main() 