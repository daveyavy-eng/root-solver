TOLERANCE = 0.00001

left = 1
right = 2

n = (left + right) / 2
left_value = left ** 2 - 2
value_mid = n ** 2 - 2

while abs(value_mid) > TOLERANCE:
    if left_value * value_mid < 0:
        right = n
    else:
        left = n
        left_value = left ** 2 - 2
    n = (left + right) / 2
    value_mid = n ** 2 - 2
print(n)