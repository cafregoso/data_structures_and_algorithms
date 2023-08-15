
fibonacci_cache = {  }


def fibonacci(nth_term: int) -> int:

    if type(nth_term) != int:
        raise TypeError("nth term of fibonacci must be a positive int")
    if nth_term < 1:
        raise ValueError("nth term of fibonacci must be a positive int")
    # If we have cached the value, then return it
    if nth_term in fibonacci_cache:
        return fibonacci_cache[nth_term]

    # Calculate the nth term of fibonacci serie
    if nth_term == 1:
        return 1
    elif nth_term == 2:
        return 1
    else:
        value = fibonacci( nth_term - 1 ) + fibonacci( nth_term - 2 )

    # Cache value and return it
    fibonacci_cache[nth_term] = value
    return value


if __name__ == "__main__":
    for i in range(1, 1001):
        print(f"{i}: {fibonacci(i)}")
