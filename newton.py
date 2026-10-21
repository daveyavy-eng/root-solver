def evaluate(number):
    return number ** 2 - 9


def derivative(number):
    return 2 * number


def newton_method(guess):

    function = evaluate(guess)
    derivative_value = derivative(guess)

    if derivative_value == 0:
        return None
    else:
        delta = function / derivative_value
        return delta


TOLERANCE = 0.00001
MAX_ITERATIONS = 100


guess = 1
delta = newton_method(guess)

counter = 0
while delta is not None and abs(delta) > TOLERANCE and counter < MAX_ITERATIONS:

    guess = guess - delta
    delta = newton_method(guess)
    counter += 1
    print(guess, delta)

if delta is None:
    print("The derivative is zero. Newton's method cannot proceed.")
elif abs(delta) <= TOLERANCE:
    print(f"The approximate value of the root is {guess}")
else:
    print("Maximum iterations reached without convergence.")

print(f"Number of iterations: {counter}")

