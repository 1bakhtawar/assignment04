def in_range(n: int, low: int, high: int) -> bool:
    
    return low <= n <= high

if __name__ == '__main__':
    print(in_range(5, 1, 10))    # True
    print(in_range(15, 1, 10))   # False
    print(in_range(10, 1, 10))   # True (inclusive)