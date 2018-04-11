from typing import Dict

def memoized_fib(n: int, seen: Dict[int, int]) -> int:
    """
    Use hash table structure (Dictionary) to keep track of fibonacci numbers
    to prevent redundant calculation in determining fibonacci number.
    """
    if n not in seen:  # prevent redundant calculations
        if n < 2:
            seen[n] = 1
        else:
            seen[n] = memoized_fib(n - 2, seen) + memoized_fib(n - 1, seen)  # recursive calls
    return seen[n]

if __name__ == "__main__":
    n = int(input("What number would you like to find the fibonacci for?: "))
    print(memoized_fib(n, {}))  
