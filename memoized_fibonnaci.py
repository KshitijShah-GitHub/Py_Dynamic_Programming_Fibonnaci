from typing import Dict

def memoized_fib(n: int, seen: Dict[int, int]) -> int:
    if n not in seen:
        if n < 2:
            seen[n] = 1
        else:
            seen[n] = memoized_fib(n - 2, seen) + memoized_fib(n - 1, seen)
    return seen[n]

if __name__ == "__main__":
    n = int(input("What number would you like to find the fibonacci for?: "))
    print(memoized_fib(n, {}))  