def bouncing_ball(h, bounce, window):
    if h <= 0 or window >= h or bounce >= 1 or bounce <= 0:
        return -1
    else:
        result = 1
        h = h * bounce
        while h > window:
            result += 2
            h = h * bounce
        return result


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))

def add_binary(a,b):
    c = a + b
    result = ""
    while c:
        result = str(c % 2) + result
        c = c // 2
    return result

def add_binary2(a,b):
    return bin(a+b)[2:]

def add_binary3(a,b):
    return '{0:b}'.format(a + b)

print((add_binary(1,1)))

import math
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    """returns a list of numbers that are like this: 89^2 = 8^2 + 9^2 """
    result = []
    for number in range(a, b):
        digits_of_number = [*str(number)]
        sum_of_digits = 0
        for digit_index in range(0, len(str(number))):
            #first_number = int(y[0])
            sum_of_digits += pow(int(digits_of_number[digit_index]), digit_index + 1)
        if number == sum_of_digits:
            result.append(number)
    return result

def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))

def sum_dig_pow2(a, b):
    return [x for x in range(a,b + 1) if x == dig_pow(x)]

def sum_dig_pow3(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]


print(sum_dig_pow(1, 95))

def bar_triang(point_a, point_b, point_c):
    return[round((point_a[0] + point_b[0] + point_c[0])/3, 4), round((point_a[1] + point_b[1] + point_c[1])/3, 4)]


def bar_triang2(a, b, c):
    return [round(sum(x)/3.0, 4) for x in zip(a, b, c)]

print(bar_triang([4, 6], [12, 4], [10, 10]))
















