"""
Part 3 — Control Flow
======================
Implement each function below according to its docstring.

Rules:
  - Do NOT rename functions or change their signatures.
  - Do NOT import any third-party libraries (the standard library is fine).
  - Remove the `pass` statement and replace it with your implementation.

Run your tests with:
    pytest tests/test_control_flow.py -v
"""


# ---------------------------------------------------------------------------
# Exercise 1  (5 pts)  — if / elif / else
# ---------------------------------------------------------------------------

def grade_calculator(score: float) -> str:
    """Convert a numeric score (0–100) to a letter grade.

    Grading scale:
        90 – 100  ->  "A"
        80 – 89   ->  "B"
        70 – 79   ->  "C"
        60 – 69   ->  "D"
         0 – 59   ->  "F"

    Raise ValueError with message "Score must be between 0 and 100"
    if score < 0 or score > 100.

    Examples:
        >>> grade_calculator(95)
        'A'
        >>> grade_calculator(72)
        'C'
        >>> grade_calculator(55)
        'F'
    """
    # TODO: implement this function
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------------------------
# Exercise 2  (5 pts)  — for loop / if
# ---------------------------------------------------------------------------

def fizzbuzz(n: int) -> list:
    """Return a list of FizzBuzz results for numbers 1 through n (inclusive).

    Rules:
        - Replace multiples of 3 with "Fizz"
        - Replace multiples of 5 with "Buzz"
        - Replace multiples of both 3 AND 5 with "FizzBuzz"
        - All other numbers appear as integers (not strings)

    Raise ValueError with message "n must be a positive integer" if n < 1.

    Examples:
        >>> fizzbuzz(15)
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
         11, 'Fizz', 13, 14, 'FizzBuzz']
    """
    # TODO: implement this function
    if n < 1:
        raise ValueError("n must be a positive integer")

    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result

# ---------------------------------------------------------------------------
# Exercise 3  (5 pts)  — for loop / list comprehension
# ---------------------------------------------------------------------------

def sum_of_evens(numbers: list) -> int:
    """Return the sum of all even integers in *numbers*.

    Non-integer values in the list are ignored.
    An empty list returns 0.

    Examples:
        >>> sum_of_evens([1, 2, 3, 4, 5, 6])
        12
        >>> sum_of_evens([1, 3, 5])
        0
        >>> sum_of_evens([1, "hello", 4, None, 6])
        10
    """
    # TODO: implement this function
    total = 0

    for x in numbers:
        if isinstance(x, int) and not isinstance(x, bool):  # exclude bool (True/False)
            if x % 2 == 0:
                total += x

    return total


# ---------------------------------------------------------------------------
# Exercise 4  (5 pts)  — while loop / math
# ---------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    """Return True if *n* is a prime number, False otherwise.

    By definition:
        - Numbers less than 2 are NOT prime.
        - 2 is prime.
        - Any number divisible only by 1 and itself is prime.

    Hint: you only need to check divisors up to sqrt(n).

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
        >>> is_prime(15)
        False
    """
    # TODO: implement this function
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


# ---------------------------------------------------------------------------
# Exercise 5  (5 pts)  — for loop + is_prime
# ---------------------------------------------------------------------------

def find_primes(limit: int) -> list:
    """Return a list of all prime numbers up to and including *limit*.

    Use your `is_prime` function from Exercise 4.
    Return an empty list if limit < 2.

    Examples:
        >>> find_primes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
        >>> find_primes(1)
        []
    """
    # TODO: implement this function
    if limit < 2:
        return []

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2

        return True

    primes = []

    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes


# ---------------------------------------------------------------------------
# Exercise 6  (5 pts)  — while loop
# ---------------------------------------------------------------------------

def collatz_length(n: int) -> int:
    """Return the number of steps to reach 1 using the Collatz sequence.

    Collatz rules (applied repeatedly until n == 1):
        If n is even  ->  n = n // 2
        If n is odd   ->  n = 3 * n + 1

    The starting number counts as step 1; reaching 1 is the final step.

    Raise ValueError with message "n must be a positive integer" if n < 1.

    Examples:
        >>> collatz_length(1)
        1
        >>> collatz_length(6)
        9    # sequence: 6, 3, 10, 5, 16, 8, 4, 2, 1
        >>> collatz_length(27)
        112
    """
    # TODO: implement this function
    if n < 1:
        raise ValueError("n must be a positive integer")

    steps = 1  # starting number counts as step 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps