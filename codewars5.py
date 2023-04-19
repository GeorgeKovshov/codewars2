def solution(s, t):
    base = s * t
    summ = base + s
    if summ > base:
        base = summ
    j = 1
    t -= 3
    while t >= 0:
        var = 3*(s - j)
        summ += -2*s + var
        t -= 2
        j += 1
        if summ < base:
            break
        else:
            base = summ
    return base


def solution2(s, t):
    # Sprints are optimally placed at the end of the race
    '''
    It is always beneficial to sprint at the end of the race
    Sprints are optimally placed at the end of the race
    e.g. RRRR...(SR)[n]S
    We take a run without sprints are keep adding sprints at
    the latest possible point until adding a sprint stops
    increasing the total distance travelled

    We can treat the final sprint as an add-on and count the number of
    (SR) units we introduce into the race. Looking at this, each add
    on unit changes the distance from 2*s to (3*s-3*n), so altering
    the distance by (s-3*n). We find the largest n<s for which (s-3*n)>0
    to find the trade-off point. If this is longer than the race in general
    we do as many (SR) as possible.
    '''
    trade_off = s // 3
    best_n_rs = min((t - 1) // 2, trade_off)  # trade off must be less than max available slots
    d = lambda n: s * t + s * (n + 1) - 3 / 2 * n * (n + 1)
    return d(best_n_rs)

def solution3(s, t):
    n = min((t-1)//2, s//3)
    return t*s + (n+1)*s - 3*(n+1)*n//2 if t else 0


print(solution(2,4))