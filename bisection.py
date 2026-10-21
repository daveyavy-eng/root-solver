def evaluate(number):
    return number ** 2 - 9


TOLERANCE = 0.00001
MAX_SEARCHES = 100
left = 3
right = -4


left_value = evaluate(left)
right_value = evaluate(right)


finding_interval = True

if left_value == 0:
    print(f"The root is {left}")
    finding_interval = False

elif right_value == 0:
    print(f"The root is {right}")
    finding_interval = False

counter = 0
while left_value * right_value > 0:
    if evaluate(left + 1) == 0:
        print(f"The root is {left + 1}")
        finding_interval = False
    elif evaluate(right + 1) == 0:
        print(f"The root is {right + 1}")
        finding_interval = False

    left += 1
    right += 1
    left_value = evaluate(left)
    right_value = evaluate(right)
    counter += 1
    if counter >= MAX_SEARCHES:
        print("Unable to find a sign change in the interval.")
        finding_interval = False
        break

print(f"Number of searches: {counter}")


n = (left + right) / 2
mid_value = evaluate(n)

bisection_counter = 0

if finding_interval:
    while abs(mid_value) > TOLERANCE:
        if left_value * mid_value < 0:
            right = n
        else:
            left = n
            left_value = evaluate(left)
        n = (left + right) / 2
        mid_value = evaluate(n)

        bisection_counter += 1

    print(f"The approximate value of the root is {n}")

print(f"Number of bisections: {bisection_counter}")
