print("The exact value is: -3")

def f(x):
    ans = x**3 + 7*x**2 - 36
    return ans


def fDerivative(x):
    ans = 3*x**2 + 14*x
    return ans


def bisection(a, b, error):
    if ((f(a) * f(b)) >= 0):
        print("The value of a and b is not valid\n")
        return

    while ((b-a) >= error):
        c = (a + b) / 2

        if (f(a)*f(c)<0):
            b = a
        if (f(c) == 0):
            break
        else:
            a = c

    return "%.4f" % c


print("The root with the Bisection Method: ", bisection(-4, -2, 0.05))


def newtonRhapson(x, error):
    h = f(x)/fDerivative(x)

    while (abs(h) >= error):
        h = f(x) / fDerivative(x)
        x = x-h

    return "%.4f" % x


print("The root with the Newton-Rhapson Method: ", newtonRhapson(-2, 0.05))