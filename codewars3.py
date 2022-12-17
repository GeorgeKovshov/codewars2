def controller(events):
    current_moment = 0  # index of events
    current_status = 0  # 0 - 5 : 0 - door closed, 5 - door open
    current_change = [0, 0]  # -1: door is closing; 0: door not moving; 1: door is opening [change before halt; change now]
    result = ""
    while current_moment < len(events):
        if events[current_moment] == "P":  # the button is pressed
            current_change = {
                -1: [-1, 0],
                0: [0, -1] if current_status == 5 or current_change[0] == -1 else [0, 1],
                1: [1, 0]
            }[current_change[1]]
        elif events[current_moment] == "O":  # an obstacle is encountered
            current_change = {
                -1: [0, 1],
                0: [0, 0],
                1: [0, -1]
            }[current_change[1]]
        current_status = { # nothing is pressed or encountered
            -1: current_status - 1,
            0: current_status,
            1: current_status + 1
        }[current_change[1]]
        if current_status in (0, 5):
            current_change = [0, 0]
        result = result + str(current_status)
        current_moment += 1
    return result



def current(current_change, ch):
    result = {
        -1: [-1, 0],
        0: [0, 1] if ch == 1 else [0,-1],
        1: [1, 0]
    }[current_change]
    return result


def controller2(events):
    out, state, dir, moving = [], 0, 1, False

    for c in events:
        if c == 'O':
            dir *= -1
        elif c == 'P':
            moving = not moving
        if moving:          state += dir
        if state in [0, 5]:  moving, dir = False, 1 if state == 0 else -1
        out.append(str(state))

    return ''.join(out)

def controller3(events):
    state = 0
    movement = False
    direction = True
    output = ''
    for event in events:
        if event is 'P':
            movement = not movement
        if event is 'O':
            direction = not direction
        state = state + (-1, 1)[direction] * movement
        if state in (0, 5):
            direction = not state
            movement  = False
        output += str(state)
    return output

print(controller('..P...O...'))


#Sorting
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse=True)
print(earth_metals)

#Set
example = set()
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
example.add(42)
print(example)
example.remove("Thorium") #remove raise error, discard doesn't
print(example)

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens))
print(primes.intersection(odds))


def freq_stack(pops, balloons):
    counted_balloons = {}
    for balloon in balloons:
        if balloon not in counted_balloons:
            counted_balloons[balloon] = 1
        else:
            counted_balloons[balloon] += 1
    print(counted_balloons)
    max_balloon = max(counted_balloons.values())
    balloons.reverse()
    result = []
    while pops:
        for ind, x in enumerate(balloons):
            if counted_balloons[x] == max_balloon:
                result.append(x)
                del balloons[ind]
                counted_balloons[x] -= 1
                max_balloon = max(counted_balloons.values())
                break
        print("pop", 5 - pops, balloons)
        pops -= 1
    return result

from collections import Counter
def freq_stack2(pops, balloons):
    lst = []
    cntr = Counter()
    for i, b in enumerate(balloons):
        cntr[b] += 1
        lst.append((-cntr[b], -i, b))
    return [b for _, _, b in sorted(lst)[:pops]]

def freq_stack3(pops, balloons):
    balloons = balloons[::-1]
    popped_balloons = []
    print(balloons)
    for i in range(pops):
        balloon_counts = Counter(balloons)
        # Find the most frequent balloon
        most_frequent_count = max(balloon_counts.values())
        # Find the highest balloon with the most frequent count
        j = 0
        while balloon_counts[balloons[j]] != most_frequent_count:
            j+=1
        highest_frequent_balloon = balloons[j]
        popped_balloons.append(highest_frequent_balloon)
        # Remove the popped balloon from the list
        balloons.remove(highest_frequent_balloon)
    return popped_balloons

print(freq_stack(4, [5, 7, 5, 7, 4, 5]))


## ignoring a value
a, _, b = (1, 2, 3) # a = 1, b = 3
print(a, b)

## ignoring multiple values
## *(variable) used to assign multiple value to a variable as list while unpacking
## it's called "Extended Unpacking", only available in Python 3.x
a, *_, b = (7, 6, 5, 4, 3, 2, 1)

## lopping ten times using _
for _ in range(5):
    print(_)

## iterating over a list using _
## you can use _ same as a variable
languages = ["Python", "JS", "PHP", "Java"]
for _ in languages:
    print(_)

_ = 5
while _ < 10:
    print(_, end = ' ') # default value of 'end' id '\n' in python. we're changing it to space
    _ += 1

















