
inch :int = 12
def foot():
    feet:int = int(input("Please enter feet and i converter it inito inches.."))
    print(f"There are {inch * feet} inches in {feet} feet.")

if __name__ == '__main__':
    foot()