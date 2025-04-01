def main():
    lst = []
    val = input("Enter a value to add the list : ")
    while val:  
     lst.append(val)
     val = input("Enter a value: ") 

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()