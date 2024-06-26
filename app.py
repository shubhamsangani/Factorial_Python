# This script calculates the factorial of a given number using recursion.
def factorial(n):
    """Return the factorial of n, an integer >= 0."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Main part of the script
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")