"""
Assignment 2
Write a python program to find the largest of three numbers.
"""


def find_largest(a, b, c):
    """Return the largest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    largest = find_largest(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")


if __name__ == "__main__":
    main()
