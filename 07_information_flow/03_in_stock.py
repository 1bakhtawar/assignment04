def main():
  
    fruit: str = input("Enter a fruit: ").lower().strip()  # Normalize input
    stock = num_in_stock(fruit)
    
    if stock == 0:
        print(f"Sorry, {fruit} is not in stock.")
    else:
        print(f"{fruit.capitalize()} is in stock! Quantity available: {stock}")

def num_in_stock(fruit: str) -> int:
    
    stock_levels = {
        'apple': 2,
        'durian': 4,
        'pear': 1000,
        # Additional fruits can be easily added here
    }
    
    return stock_levels.get(fruit, 0)

if __name__ == '__main__':
    main()