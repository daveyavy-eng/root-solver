def evaluate(number):
    return number ** 2 - 9


TOLERANCE = 0.00001

left = 1
right = 2


left_value = evaluate(left)
right_value = evaluate(right)


finding_interval = True

while finding_interval:

    if left_value == 0:
        print(f"The root is {left}")
        finding_interval = False
        break
    elif right_value == 0:
        print(f"The root is {right}")
        finding_interval = False
        break

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
    if left_value * right_value < 0:
        break


n = (left + right) / 2
mid_value = evaluate(n)

if finding_interval:
    while abs(mid_value) > TOLERANCE:
        if left_value * mid_value < 0:
            right = n
        else:
            left = n
            left_value = evaluate(left)
        n = (left + right) / 2
        mid_value = evaluate(n)

    print(f"The approximate value of the root is {n}")