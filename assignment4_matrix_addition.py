"""
Assignment 4
Write a python program to create an array and perform addition of two matrices.
"""

from array import array


def input_matrix(rows, cols, matrix_name):
    """Take matrix elements as input from the user and store each row as an array."""
    matrix = []
    print(f"\nEnter elements for {matrix_name} ({rows}x{cols}):")
    for i in range(rows):
        row = array('i')  # array of integers
        for j in range(cols):
            value = int(input(f"Element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def add_matrices(matrix_a, matrix_b, rows, cols):
    """Add two matrices of the same dimensions and return the result as a list of arrays."""
    result = []
    for i in range(rows):
        row_result = array('i')
        for j in range(cols):
            row_result.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row_result)
    return result


def display_matrix(matrix, matrix_name):
    """Display a matrix in a readable grid format."""
    print(f"\n{matrix_name}:")
    for row in matrix:
        print(" ".join(str(element) for element in row))


def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix_a = input_matrix(rows, cols, "Matrix A")
    matrix_b = input_matrix(rows, cols, "Matrix B")

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")

    result = add_matrices(matrix_a, matrix_b, rows, cols)
    display_matrix(result, "Sum of Matrix A and Matrix B")


if __name__ == "__main__":
    main()
