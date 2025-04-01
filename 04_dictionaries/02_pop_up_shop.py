def main():
    fruits = {
        'apple': 1.5,
        'durian': 50, 
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
        }
    total_cost = 0

    for fruits,price in fruits.items():
        while True:
            try:
              quantity = int(input(f'\n How many {fruits} do you want?:'))
              if quantity < 0:
                 print("Invalid input. Please rnter a non-negative number.")
                 continue
              total_cost += price * quantity
              break
            except ValueError:
              print("Invalid Input. Please enteer a valid number.")
        print(f"Your total cost is: ${total_cost:.2f}")

if __name__ == '__main__':
   main()