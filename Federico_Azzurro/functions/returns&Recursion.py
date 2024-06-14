def sum_numbers(a: float, b: float) -> float:  # return type hint
    return a + b


s = sum_numbers(10, 20)

print(f"{s}")


def recursive(n: int) -> int :
    print(n)
    if n == 1:
        return
    
    recursive(n-1)
    
    
recursive(5)
