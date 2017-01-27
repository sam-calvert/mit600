# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # TO DO ... (my code here)
    
    ans = 0
    for i in range(len(poly)):
        # For each index of poly, find x to the power of that index and multiply the
        # result by the float at that index of poly. Add the product to running total 
        # at ans. After the loop, ans will return the value of poly for x.
        ans += x**i * poly[i]
    return ans

# Check that evaluate_poly implementation above correctly executes the example given:
poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
print(evaluate_poly(poly, x))


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ... (my code here)
    
    new_poly = [] # create a mutable list to add each derivative element to
    for i in range(len(poly)):
        if i == 0: # remove the x^0 value
            continue
        deriv = poly[i] * i # add other values such that ax^b is now abx^b-1
        new_poly.append(deriv)
    return tuple(new_poly)

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)  
print(compute_deriv(poly))

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ... 
    
    test = x_0
    tries = 0
    while True:
        if evaluate_poly(poly,test) <= epsilon and evaluate_poly(poly,test) >= -epsilon:
            # print(evaluate_poly(poly,test))
            tries += 1
            return (test, tries)
        else:
            x_1 = test - evaluate_poly(poly, test) / evaluate_poly(compute_deriv(poly), test)
            test = x_1
           # print(test)
            tries += 1

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = .0001
print (compute_root(poly, x_0, epsilon))
