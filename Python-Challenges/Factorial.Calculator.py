def FactorialCalculator(n):
    """
    Calculate the factorial of the number n.
    
    Args:
    n (int): The number to check.
    
    Returns:
    int: Calculated factorial value.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result