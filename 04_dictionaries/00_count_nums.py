def count_numbers():
    count_dic = {}
    while True:
        num = input("Enter a number(or 'Exit' to quit): ")
        if num.title() == 'Exit':
            break
        if num.isdigit():
            num = int(num)
            count_dic[num] = count_dic.get(num,0) + 1
        else:
            print("Invalid Input. Please enter anumber or 'Exit'.")

    return count_dic
    
def display_counts(count_dict):
    print("\n Number Counts: ")
    for key,value in count_dict.items():
        print(f'{key} appears {value} times')

if __name__ == '__main__':
    counts = count_numbers()
    display_counts(counts)