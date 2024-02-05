# region import
import math
# endregion

#region functions
def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability using Simpson's 1/3 rule.

    Parameters:
    - PDF: callback function for the Gaussian/normal probability density function
    - args: tuple containing μ and σ
    - c: upper limit of integration
    - GT: boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False)

    Returns:
    Probability value based on the specified conditions.
    """
    mu, sigma = args

    if GT:
        # Probability of x being greater than c
        # Using Simpson's 1/3 rule to integrate PDF from μ-5σ to c
        num_intervals = 1000
        dx = (mu - 5 * sigma - c) / num_intervals
        probabilities = [PDF((x, mu, sigma)) for x in reversed([c + i * dx for i in range(num_intervals + 1)])]
        result = sum(probabilities) * dx
    else:
        # Probability of x being less than c
        # Using Simpson's 1/3 rule to integrate PDF from μ-5σ to c
        num_intervals = 1000
        dx = (c - (mu - 5 * sigma)) / num_intervals
        probabilities = [PDF((x, mu, sigma)) for x in [mu - 5 * sigma + i * dx for i in range(num_intervals + 1)]]
        result = sum(probabilities) * dx

    return result


def normal_pdf(args):
    """
    Gaussian/normal probability density function.

    Parameters:
    - args: tuple containing x values, μ, and σ

    Returns:
    Probability density values based on the normal distribution.
    """
    x, mu, sigma = args
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


def main():
    """
    Main function to demonstrate the use of Probability function.

    Examples:
    1. P(x<105|N(100,12.5))
    2. P(x>μ+2σ|N(100, 3))
    """
    # Example 1: P(x<105|N(100,12.5))
    prob_1 = Probability(normal_pdf, (100, 12.5), 105, GT=False)
    print(f'P(x<105|N(100,12.5))={prob_1:.2f}')

    # Example 2: P(x>μ+2σ|N(100, 3))
    prob_2 = Probability(normal_pdf, (100, 3), 100 + 2 * 3, GT=True)
    print(f'P(x>{100 + 2 * 3:.2f}|N(100,3))={prob_2:.2f}')
# endregion

if __name__ == "__main__":
    main()
