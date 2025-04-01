def get_last_element(list):
    print(list[-1])

def get_list():
    list = []
    element:str = input("Enter an element to add to the list. ")
    while element != "":
        list.append(element)
        element = input("Enter an element to add to the list.")
    return list

def main():
    list = get_list()
    get_last_element(list)

if __name__ == '__main__':
    main()

