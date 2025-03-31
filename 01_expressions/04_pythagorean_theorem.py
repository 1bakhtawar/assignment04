import math
def main():
    AB : float = float(input("Enter a length of side AB: "))
    AC : float = float(input("Enter a length of side AC: "))

    BC :float = math.sqrt(AB**2 + AC **2)
    print(f"The length of BC (the Hypotenous) is : {BC}")

if __name__ == '__main__':
    main()