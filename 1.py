import numpy as np

x = 0.25 * np.pi
x0 = 11 * np.pi / 45
x1 = 23 * np.pi / 90

def f(x):
    ans = np.tan(x)
    return ans


def newtonSecondOrder(x, x0, x1):
    b0 = f(x0)
    b1 = (f(x1)-f(x0))/(x1-x0)

    order2 = b0 + b1 * (x - x0)

    return order2


def lagrangeSecondOrder(x, x0, x1):
    l0 = (x-x1)/(x0-x1)
    l1 = (x-x0)/(x1-x0)

    p = (l0 * f(x0)) + (l1 * f(x1))

    return p


def relativeError(exact, estimate):
    absError = exact-estimate
    relError = absError/exact

    return relError


exact = np.tan(x)
newton = newtonSecondOrder(x, x0, x1)
lagrange = lagrangeSecondOrder(x, x0, x1)

newtonRelError = relativeError(exact, newton)
lagrangeRelError = relativeError(exact, lagrange)

print("Exact Value: ", exact)
print("\nSecond Order Newton's Interpolation Method: ", newton)
print("Relative Error: ", newtonRelError)
print("\nSecond Order Lagrange's Interpolation Method: ", lagrange)
print("Relative Error: ", lagrangeRelError)