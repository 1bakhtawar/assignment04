def average(a , b):

    sum = a + b
    return sum / 2

def main():
    num1 = average(0,10)
    num2 = average(8,10)

    final = average(num1 , num2)
    print("average1 = ", num1)
    print("average2 = ", num2)
    print("final = " , final)
if __name__ == '__main__':
    main()