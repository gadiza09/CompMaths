def f(x):
    ans = x**4 - 3*x**3 + 6*x**2 - 10*x - 9
    return ans

def exactFirstDerivative(x):
    ans = 4*x**3 - 9*x**2 + 12*x - 10
    return ans


def exactSecondDerivative(x):
    ans = 12*x**2 - 18*x + 12
    return ans


def firstDerivative(function, x, h):
    derivative1 = (function(x+h) - function(x-h)) / (2*h)
    return derivative1


def secondDerivative(function, x, h):
    derivative2 = (function(x+h) - 2*function(x) + function(x-h)) / (h**2)
    return derivative2


exactFirstD = exactFirstDerivative(0)
exactSecondD = exactSecondDerivative(0)

firstD1 = firstDerivative(f, 0, 0.5)
firstD2 = firstDerivative(f, 0, 0.25)
firstD3 = firstDerivative(f, 0, 0.125)

secondD1 = secondDerivative(f, 0, 0.5)
secondD2 = secondDerivative(f, 0, 0.25)
secondD3 = secondDerivative(f, 0, 0.125)


def relativeError(exact, estimate):
    absError = exact-estimate
    relError = absError/exact

    return relError


relErrorFD1 = relativeError(exactFirstD, firstD1)
relErrorFD2 = relativeError(exactFirstD, firstD2)
relErrorFD3 = relativeError(exactFirstD, firstD3)

relErrorSD1 = relativeError(exactFirstD, secondD1)
relErrorSD2 = relativeError(exactFirstD, secondD2)
relErrorSD3 = relativeError(exactFirstD, secondD2)

print("--------------------------------------------------------------------------------------------------------------------")
print("|h \t\t|f' exact \t|f' approximation \t|f' relative error \t|f'' exact \t\t|f''approximation \t|f'' relative error|")
print("--------------------------------------------------------------------------------------------------------------------")
print("|0.5 \t|", exactFirstD, '\t\t|', firstD1, "\t\t\t|", relErrorFD1, "\t\t\t|", exactSecondD, "\t\t\t|", secondD1, "\t\t\t\t|", relErrorSD1, "\t\t\t   |")
print("--------------------------------------------------------------------------------------------------------------------")
print("|0.25 \t|", exactFirstD, '\t\t|', firstD2, "\t\t\t|", relErrorFD2, "\t\t\t|", exactSecondD, "\t\t\t|", secondD2, "\t\t\t|", relErrorSD2, "\t\t   |")
print("--------------------------------------------------------------------------------------------------------------------")
print("|0.125 \t|", exactFirstD, '\t\t|', firstD3, "\t\t|", relErrorFD3, "\t\t|", exactSecondD, "\t\t\t|", secondD3, "\t\t\t|", relErrorSD3, "\t\t   |")
print("--------------------------------------------------------------------------------------------------------------------")

