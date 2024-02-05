# region functions
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    - fcn: The function for which we want to find the root.
    - x0, x1: Two x values in the neighborhood of the root.
    - xtol: Exit if |xnewest - xprevious| < xtol.
    - maxiter: Exit if the number of iterations equals this number.

    Returns:
    - The final estimate of the root (most recent new x value).
    """
    iter_count = 0

    while iter_count < maxiter:
        f_x0 = fcn(x0)
        f_x1 = fcn(x1)

        if abs(f_x1 - f_x0) < xtol:
            return x1

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x_new - x1) < xtol:
            return x_new

        x0, x1 = x1, x_new
        iter_count += 1

    return x1

def main():
    """
    Test the Secant method with different cases and print the results.
    """
    # Test cases
    x0_1, x1_1, maxiter_1, xtol_1 = 1, 2, 5, 1e-4
    result_1 = Secant(lambda x: x**2 - 3, x0_1, x1_1, maxiter_1, xtol_1)
    print(f"Solution 1: {result_1}")

    x0_2, x1_2, maxiter_2, xtol_2 = 1, 2, 15, 1e-8
    result_2 = Secant(lambda x: x**2 - 3, x0_2, x1_2, maxiter_2, xtol_2)
    print(f"Solution 2: {result_2}")

    x0_3, x1_3, maxiter_3, xtol_3 = 1, 2, 3, 1e-8
    result_3 = Secant(lambda x: x**2 - 3, x0_3, x1_3, maxiter_3, xtol_3)
    print(f"Solution 3: {result_3}")
# endregion

if __name__ == "__main__":
    main()
