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

def next_bigger1(n):
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

def next_bigger2(n):
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


def next_bigger_rec(n, original):
    min = n
    if n == original:
        min *= 10
    list = [*str(n)][::-1]
    for ind, x in enumerate(list):
        for i in range(ind+1, len(list)):
            list_tmp = list.copy()
            list_tmp[ind], list_tmp[i] = list_tmp[i], list_tmp[ind]
            m = 0
            for y in reversed(list_tmp):
                m = m * 10 + int(y)
            if original < m < min:
                min = m
                break
    if min/10 == n:
        return n
    return min if min == n else next_bigger_rec(min, original)

def next_bigger(n):
    next = next_bigger_rec(n, n)
    return next if next != n else -1

#print(next_bigger(144))
#print(next_bigger(1234567890))
#print(next_bigger(59884848459853))



"""
Incorrect answer for n=
59884848459853: 
59884848489553 should equal 
59884848483559
59884848483559

"""

def duplicate_count(text):
    my_dict = {}
    count = 0
    for s in text:
        c = s.lower()
        if c not in my_dict.keys():
            my_dict[c] = 1
        elif my_dict[c] == 1:
            my_dict[c] += 1
            count += 1
    return count

def duplicate_count2(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


#print(duplicate_count("Indivisibilities"))

from queue import Queue


def swap(q):

    return


def get_in_line(arr):
    ones = 0
    twos = 0
    for x in arr:
        if x == 1:
            ones += 1
        elif x == 2:
            twos += 1

    arr2 = []
    ones2 = ones

    while ones2 > 0:
        arr2.append(1)
        ones2 -= 1
    while twos > 0:
        arr2.append(2)
        twos -= 1
    length = len(arr)
    for x in arr:
        if x not in [1, 2]:
            arr2.append(x)


    j = 0
    while ones > 0:
       ones -= 1
       j+= 1
       i = 0
       while i + ones + j <= (length- 1 - i - ones):
           if arr2[i + ones + j] != 3 and arr2[length - 1 - i - ones] != 3:
               arr2[i + ones + j], arr2[length - 1 - i - ones] = arr2[length - 1 - i - ones], arr2[i + ones + j]
           i += 1


    return arr2.index(0) + 1



#get_in_line([1,1,3,2,0])
#print(get_in_line([0, 8, 2, 1, 4, 2, 12, 3, 2]))
print(get_in_line([2, 3, 1, 4, 5, 2, 1, 0, 8, 5, 6, 1]))
















