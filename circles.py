import logging
from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")

    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi*(r**2)

#Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circles with r = {radius} is {area}"

#for r in radii:
#    A = circle_area(r)
#    print(message.format(radius=r, area=A))

import logging
import time

#create logger
logging.basicConfig(filename="problems.log", level=logging.DEBUG)

logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        print(dt)
        logger.info("Time required for {file} = {time}".format(file=path,time=dt))

#data = read_file_timed("N:\Afterlife (1978).avi")
#data = read_file_timed("N:\Afterli (1978).avi")

class Martian:

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, key, value):
        print(f">>> You set {key} = {value}")
        self.__dict__[key] = value

    def __getattr__(self, name):
        print(f">>> Get the '{name}' attribute")
        if name == 'full_name':
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"No attribute named {name}")

    def __lt__(self, other):
        if self.last_name != other.last_name:
            return(self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)

#m1 = Martian()
#m1.first_name = "Owen"
#m1.last_name = "Phelps"
m2 = Martian('Rob', 'Schenk')
m3 = Martian('Bob', 'Spelunky')
m4 = Martian('Alan', 'Asimov')
print(m2.__dict__)
print(f"First name = {m2.first_name}")
print(f"Last name = {m2.last_name}")
print(m2.full_name)
martians = [m2, m3, m4]
martians.sort()
for m in martians:
    print(m.full_name)

