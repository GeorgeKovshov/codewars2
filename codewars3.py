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