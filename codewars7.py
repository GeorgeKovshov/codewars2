def solution1(args):
    previous = -10000
    string = ""
    in_range = False
    for x in args:
        if x - previous == 1:
            if not in_range:
                in_range = True
        else:
            if in_range:
                string += "-" + str(previous) + "," + str(x)
                in_range = False
            else:
                string += "," + str(x)
        previous = x
    if in_range:
        string += "-" + str(previous)
    return string[1:]


def check(previous, length):
    """if a span of consequetive numbers is more than 2 numbers long, then we do a range, otherwise a comma"""
    if length >= 1:
        string = "-" + str(previous)
    else:
        string = "," + str(previous)
    return string

def solution(args):
    previous = -10000
    string = ""
    in_range = False
    length = 0
    for x in args:
        if x - previous == 1:
            if not in_range:
                in_range = True
            else:
                length += 1
        else:
            if in_range:
                string += check(previous, length)
                in_range = False
                length = 0
            string += "," + str(x)
        previous = x
    if in_range:
        string += check(previous, length)
    return string[1:]


def solution2(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)
"""
-6,-3-1,3-5,7-11,14-15,17-20'
 should equal 
'-6,-3-1,3-5,7-11,14,15,17-20'

'-83,-81,-80,-78,-77,-75,-73--71,-69,-66,-65,-63,-60,-58,-56--55' should equal 
'-83,-81,-80,-78,-77,-75,-73--71,-69,-66,-65,-63,-60,-58,-56,-55'

"""
#print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 22]))
#print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

def adding_time(result, time, bar):
    if time > 1:
        return bar + "s" + result
    elif time == 1:
        return bar + result
    return result


def format_duration(seconds):
    if seconds == 0:
        return "now"
    elif seconds < 0:
        return None
    elif 1 < seconds < 60:
        return str(seconds) + " seconds"
    elif seconds == 1:
        return "1 second"
    time = [seconds, 0, 0, 0, 0]
    denominators = [60, 60, 24, 365]
    words = ["second", "minute", "hour", "day", "year"]
    ind = 0
    result = ""
    while ind < 4:
        time[ind+1], time[ind] = divmod(time[ind], denominators[ind])
        bar = str(time[ind]) + " " + words[ind]
        result = adding_time(result, time[ind], bar)
        if time[ind + 1] > 0 and result in [bar, bar + "s"]:
            result = " and " + result
        elif time[ind + 1] > 0 and time[ind] != 0:
            result = ", " + result
        ind += 1
    bar = str(time[4]) + " " + words[4]
    return adding_time(result, time[4], bar)

"""
time[1], time[0] = divmod(time[0],60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)
years, days = divmod(days, 365)
print("seconds:", seconds)
print("minutes:", minutes)
print("hours:", hours)
print("days:", days)
print("years:", years)
"""



#print(format_duration(3662))


def next_bigger_bad(n):
    min = n*10
    list = [*str(n)][::-1]
    for ind, x in enumerate(list):
        for i in range(ind+1, len(list)):
            list_tmp = list   # here's the mistake - list and list_tmp are pointers to the same data
            list_tmp[ind], list_tmp[i] = list_tmp[i], list_tmp[ind]
            m = 0
            for y in reversed(list_tmp):
                m = m * 10 + int(y)
            if n < m < min:
                min = m
    return min if min/10 != n else "-1"
            #print("main: ", x, "second:",  list[i], end=" | ")

def next_bigger(n):
    min = n*10
    list = [*str(n)][::-1]
    for ind, x in enumerate(list):
        for i in range(ind+1, len(list)):
            list_tmp = list.copy()
            list_tmp[ind], list_tmp[i] = list_tmp[i], list_tmp[ind]
            m = 0
            for y in reversed(list_tmp):
                m = m * 10 + int(y)
            if n < m < min:
                min = m
    return min if min/10 != n else -1





print(next_bigger(144))

















