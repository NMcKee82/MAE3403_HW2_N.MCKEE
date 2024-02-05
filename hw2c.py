# region import
import copy
import math
# endregion

# region functions
def GaussSeidel(Aaug, x, Niter=15):
    """
    Perform Gauss-Seidel method to estimate the solution to a set of linear equations Ax = b.

    Parameters:
    - Aaug: N x (N+1) matrix, augmented matrix [A | b]
    - x: Initial guess vector
    - Niter: Number of iterations

    Returns:
    - Final x vector after Niter iterations
    """
    # Number of equations
    N = len(Aaug)

    for _ in range(Niter):
        # Make a copy of the current x vector
        x_old = copy.deepcopy(x)

        # Iterate through each equation
        for i in range(N):
            sigma = 0.0

            # Calculate the sum of products excluding the diagonal element
            for j in range(N):
                if j != i:
                    sigma += Aaug[i][j] * x[j]

            # Update the value of x[i]
            x[i] = (Aaug[i][-1] - sigma) / Aaug[i][i]

    return x

def isDiagonallyDominant(matrix):
    """
    Check if a matrix is diagonally dominant.

    Parameters:
    - matrix: Square matrix

    Returns:
    - True if the matrix is diagonally dominant, False otherwise
    """
    size = len(matrix)

    for i in range(size):
        diagonal_sum = sum(map(abs, matrix[i])) - abs(matrix[i][i])
        if abs(matrix[i][i]) <= diagonal_sum:
            return False

    return True

def main():
    # Example 1
    A1 = [
        [3, 1, -1, 2],
        [1, 4, 1, 12],
        [2, 1, 2, 10]
    ]
    b1 = [2, 12, 10]
    x1_initial_guess = [0, 0, 0]

    if not isDiagonallyDominant(A1):
        print("Matrix is not diagonally dominant. Gauss-Seidel method may not converge.")

    result1 = GaussSeidel(A1, x1_initial_guess)
    print("Solution for Example 1:", result1)

    # Example 2
    A2 = [
        [1, -10, 2, 4, 2],
        [3, 1, 4, 12, 12],
        [9, 2, 3, 4, 21],
        [-1, 2, 7, 3, 37]
    ]
    b2 = [2, 12, 21, 37]
    x2_initial_guess = [0, 0, 0, 0]

    if not isDiagonallyDominant(A2):
        print("Matrix is not diagonally dominant. Gauss-Seidel method may not converge.")

    result2 = GaussSeidel(A2, x2_initial_guess)
    print("Solution for Example 2:", result2)
# endregion_

if __name__ == "__main__":
    main()
