"""
Assignment 3
Write a python program that accepts the length of three sides of a triangle as inputs.
The program should indicate whether or not the triangle is a right-angled triangle
using a function.
"""


def is_right_angled(side1, side2, side3):
    """
    Check whether the triangle with the given three sides is right-angled.
    Uses the Pythagorean theorem: the square of the largest side must equal
    the sum of squares of the other two sides.
    """
    sides = sorted([side1, side2, side3])
    a, b, c = sides  # c is the largest side after sorting

    # Use a small tolerance to safely compare floating point values
    return abs((a ** 2 + b ** 2) - c ** 2) < 1e-9


def main():
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    if is_right_angled(side1, side2, side3):
        print("The triangle IS a right-angled triangle.")
    else:
        print("The triangle is NOT a right-angled triangle.")


if __name__ == "__main__":
    main()
