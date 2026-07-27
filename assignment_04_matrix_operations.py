# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
def read_matrix(name, rows, cols):
    """Reads a rows x cols matrix from the user, row by row."""
    print(f"\nEnter matrix {name} ({rows} x {cols}):")
    matrix = []
    for r in range(rows):
        while True:
            row_input = input(f"Row {r + 1} (enter {cols} numbers separated by spaces): ")
            values = row_input.split()
            if len(values) != cols:
                print(f"Error: expected {cols} numbers, got {len(values)}. Try again.")
                continue
            try:
                row = [float(v) for v in values]
            except ValueError:
                print("Error: all entries must be numbers. Try again.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix):
    """Prints a matrix in a readable grid format."""
    for row in matrix:
        print("  ".join(f"{val:g}" for val in row))


def transpose_matrix(matrix):
    """Returns the transpose of the given matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


def add_matrices(a, b):
    """Returns the element-wise sum of two matrices of the same size."""
    rows = len(a)
    cols = len(a[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(a[r][c] + b[r][c])
        result.append(new_row)
    return result


def multiply_matrices(a, b):
    """Returns the matrix product of A (MxN) and B (NxP), giving an MxP matrix."""
    m = len(a)
    n = len(a[0])
    p = len(b[0])

    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def get_dimensions(prompt):
    """Reads and validates a rows/cols pair, ensuring both are positive integers."""
    while True:
        try:
            rows = int(input(f"{prompt} rows: "))
            cols = int(input(f"{prompt} columns: "))
        except ValueError:
            print("Error: dimensions must be integers. Try again.")
            continue
        if rows <= 0 or cols <= 0:
            print("Error: dimensions must be positive integers. Try again.")
            continue
        return rows, cols


def part_a_transpose():
    print("\n--- PART A: Transpose a Matrix ---")
    rows, cols = get_dimensions("Matrix")
    matrix = read_matrix("", rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed)


def part_b_add():
    print("\n--- PART B: Add Two Matrices ---")
    rows, cols = get_dimensions("Matrix")
    matrix_a = read_matrix("A", rows, cols)
    matrix_b = read_matrix("B", rows, cols)

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)

    result = add_matrices(matrix_a, matrix_b)
    print("\nA + B:")
    print_matrix(result)


def part_c_multiply():
    print("\n--- PART C: Multiply Two Matrices ---")
    m, n = get_dimensions("Matrix A")
    matrix_a = read_matrix("A", m, n)

    while True:
        n2, p = get_dimensions("Matrix B")
        if n2 != n:
            print(f"Error: Matrix B must have {n} rows (columns of A). Try again.")
            continue
        break
    matrix_b = read_matrix("B", n2, p)

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)

    result = multiply_matrices(matrix_a, matrix_b)
    print("\nA x B:")
    print_matrix(result)


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    choice = input("Choose an operation (1/2/3): ").strip()

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    else:
        print("Error: invalid choice.")


if __name__ == "__main__":
    main()
# =============================================================================

