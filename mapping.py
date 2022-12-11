import math, statistics

g = lambda x: 3*x + 1

print(g(2))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("  leonhard", "EULER"))

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein",
                 "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card",
                 "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

print(build_quadratic_function(3, 0, 1)(2)) # 3x^2 + 1 evaluated for x = 2

f = build_quadratic_function(2, 3, -5)
print(f(0))

def area(r):
    """area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]
print(list(map(area, radii)))

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
         ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28),
         ("London", 22), ("Beijing", 32), ]

c_to_f = lambda data: (data[0], round((9/5)*data[1] +32))


print(list(map(c_to_f, temps)))

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

filtered_list = list(filter(lambda x: x > avg, data))
print(filtered_list)

countries = ["", "Argentina", "", "Brazil", "Chile", ""]
print(list(filter(None, countries)))

from functools import reduce

#multiply all numbers in a list
data = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))