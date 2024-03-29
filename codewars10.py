class Solution:
    def __init__(self, shape):

        s = shape.splitlines()
        self.double = True
        list_shape = []
        self.width = 0
        for line in s:
            list_line = []
            started = False
            tmp_line = line.rstrip()
            for i in range(len(tmp_line)):

                if tmp_line or started:
                    list_line.append(tmp_line[i])
                    list_line.append(' ')
                    started = True
                else:
                    continue
            if len(list_line) > self.width:
                self.width = len(list_line)
            if tmp_line or started:
                list_shape = list_shape + [list_line] + [[' '] * self.width]
        self.depth = len(list_shape)
        self.list_shape = list_shape
        for i in range(self.depth):
            if len(self.list_shape[i]) < self.width:
                self.list_shape[i] = self.list_shape[i] + [' '] * (self.width - len(self.list_shape[i]))
        i = 0

        while i < self.depth:
            j = 0
            while j < self.width:

                if j > 1 and self.list_shape[i][j] in ['-', '+'] and self.list_shape[i][j - 2] in ['-', '+']:
                    self.list_shape[i][j - 1] = '-'
                if i > 1 and self.list_shape[i][j] in ['|', '+'] and self.list_shape[i - 2][j] in ['|', '+']:
                    self.list_shape[i - 1][j] = '|'
                j += 2
            i += 2

        self.vertices = {}
        self.double_vertices = {}
        self.fake_vertices = []
        self.cut_figures = []

    def figure_mapper_double(self, i, j, num, count):
        self.list_shape[i][j] = self.double_vertices[num][0]

        # checking for holes
        if i == 0 or i == self.depth - 1 or j == 0 or j == self.width - 1:
            # self.list_shape[i][j] = '0'
            self.fake_vertices.append(num)
        if count == 0:
            return

        '''vertical up'''
        # 1) we check if we encounter a new number, add it to the dictionary of currently connected vertices,
        #        if the new number in fake_vertices, we add current ones there
        if i >= 1 and self.list_shape[i - 1][j] not in ['|', '+', '-', ' '] and self.list_shape[i - 1][j] not in \
                self.double_vertices[num]:
            for x in self.double_vertices:
                if self.list_shape[i - 1][j] in self.double_vertices[x]:
                    self.double_vertices[num] += self.double_vertices[x]
                    if x in self.fake_vertices:
                        self.fake_vertices.append(num)
                    del (self.double_vertices[x])
                    break
        # 3) if the next location is empty, we travel there
        elif i >= 1 and self.list_shape[i - 1][j] == ' ':
            self.figure_mapper_double(i - 1, j, num, count - 1)

        '''vertical down'''
        if i < self.depth - 1 and self.list_shape[i + 1][j] not in ['|', '+', '-', ' '] and self.list_shape[i + 1][
            j] not in self.double_vertices[num]:
            for x in self.double_vertices:
                if self.list_shape[i + 1][j] in self.double_vertices[x]:
                    self.double_vertices[num] += self.double_vertices[x]
                    if x in self.fake_vertices:
                        self.fake_vertices.append(num)
                    del (self.double_vertices[x])
                    break
        elif i < self.depth - 1 and self.list_shape[i + 1][j] == ' ':
            self.figure_mapper_double(i + 1, j, num, count - 1)

        '''horizontal left'''
        if j >= 1 and self.list_shape[i][j - 1] not in ['|', '+', '-', ' '] and self.list_shape[i][j - 1] not in \
                self.double_vertices[num]:
            for x in self.double_vertices:
                if self.list_shape[i][j - 1] in self.double_vertices[x]:
                    self.double_vertices[num] += self.double_vertices[x]
                    if x in self.fake_vertices:
                        self.fake_vertices.append(num)
                    del (self.double_vertices[x])
                    break
        elif j >= 1 and self.list_shape[i][j - 1] == ' ':
            self.figure_mapper_double(i, j - 1, num, count - 1)

        '''horizontal right'''
        if j < self.width - 1 and self.list_shape[i][j + 1] not in ['|', '+', '-', ' '] and self.list_shape[i][
            j + 1] not in self.double_vertices[num]:
            for x in self.double_vertices:
                if self.list_shape[i][j + 1] in self.double_vertices[x]:
                    self.double_vertices[num] += self.double_vertices[x]
                    if x in self.fake_vertices:
                        self.fake_vertices.append(num)
                    del (self.double_vertices[x])
                    break
        elif j < self.width - 1 and self.list_shape[i][j + 1] == ' ':
            self.figure_mapper_double(i, j + 1, num, count - 1)

        # store the coordinates of figure in graph

        for n in self.double_vertices[num]:
            if n in self.vertices:
                self.vertices[n][0] = i if i < self.vertices[n][0] else self.vertices[n][0]
                self.vertices[n][1] = i if i > self.vertices[n][1] else self.vertices[n][1]
                self.vertices[n][2] = j if j < self.vertices[n][2] else self.vertices[n][2]
                self.vertices[n][3] = j if j > self.vertices[n][3] else self.vertices[n][3]

        return


    def find_near_num(self, i, j, count):
        if count <= 0:
            return "none"
        result = "none"
        if self.list_shape[i][j] not in ['|', '+', '-', ' ']:
            return self.list_shape[i][j]
        elif self.list_shape[i][j] in ['|', '+', '-']:
            return "none"
        if i > 0:
            tmp = self.find_near_num(i - 1, j, count - 1)
            if tmp != "none":
                return tmp
        if i < self.depth - 1:
            tmp = self.find_near_num(i + 1, j, count - 1)
            if tmp != "none":
                return tmp
        if j < self.width - 1:
            tmp = self.find_near_num(i, j + 1, count - 1)
            if tmp != "none":
                return tmp
        if j > 0:
            tmp = self.find_near_num(i, j - 1, count - 1)
            if tmp != "none":
                return tmp
        return "none"

    def overview_traversal(self):
        dou_count = 1
        num = 1
        for i in range(self.depth):
            for j in range(self.width):
                near_num = self.find_near_num(i, j, 3)
                if self.list_shape[i][j] == ' ':
                    double_num = "none"
                    for x in self.double_vertices:
                        if near_num in self.double_vertices[x]:
                            double_num = x
                            break
                    if near_num == "none":
                        self.vertices[num] = [1000, -1, 1000, -1]
                        near_num = num
                        num += 1
                    if double_num == "none":
                        self.double_vertices[dou_count] = [near_num]
                        double_num = dou_count
                        dou_count += 1
                    self.figure_mapper_double(i, j, double_num, 30)
                if near_num != "none":
                    for x in self.double_vertices:
                        if near_num in self.double_vertices[x]:
                            self.figure_mapper_double(i,j,x,2)
                            break



    def smallify(self, tmp):
        result = []
        depth = len(tmp)
        width = len(tmp[0])
        i = 0
        while i < depth:
            j = 0
            line = []
            while j < width:
                line.append(tmp[i][j])
                j += 2
            result.append(line)
            i += 2
        return result

    def cut_out_figure(self, num):
        num_list = self.double_vertices[num]
        coord = [1000, -1, 1000, -1]
        for ver in num_list:
            self.fake_vertices.append(ver)
            v = self.vertices[ver]
            coord[0] = v[0] if v[0] < coord[0] else coord[0]
            coord[1] = v[1] if v[1] > coord[1] else coord[1]
            coord[2] = v[2] if v[2] < coord[2] else coord[2]
            coord[3] = v[3]+1 if v[3]+1 > coord[3] else coord[3]

        tmp = []
        for i in range(coord[0] - 1, coord[1] + 2):
            tmp.append(self.list_shape[i][coord[2] - 1:coord[3] + 2])

        depth = len(tmp) - 1
        width = len(tmp[0]) - 1
        for i in range(depth + 1):
            for j in range(width + 1):
                if tmp[i][j] not in ['-', '+', '|'] and tmp[i][j] not in num_list:
                    tmp[i][j] = ' '
                elif tmp[i][j] == '-':
                    if (i > 0 and tmp[i - 1][j] in num_list) or (i < depth and tmp[i + 1][j] in num_list):
                        tmp[i][j] = '-'
                    else:
                        tmp[i][j] = ' '
                elif tmp[i][j] == '|':
                    if (j > 0 and tmp[i][j - 1] in num_list) or (j < width and tmp[i][j + 1] in num_list):
                        tmp[i][j] = '|'
                    else:
                        tmp[i][j] = ' '
                elif tmp[i][j] == '+':  # this nefarious plus...
                    touches_num = False
                    if i > 0 and j > 0:
                        touches_num = True if tmp[i - 1][j - 1] in num_list else touches_num
                    if i > 0 and j < width:
                        touches_num = True if tmp[i - 1][j + 1] in num_list else touches_num
                    if i < depth and j > 0:
                        touches_num = True if tmp[i + 1][j - 1] in num_list else touches_num
                    if i < depth and j < width:
                        touches_num = True if tmp[i + 1][j + 1] in num_list else touches_num

                    if i > 0:
                        touches_num = True if tmp[i - 1][j] in num_list else touches_num
                    if i < depth:
                        touches_num = True if tmp[i + 1][j] in num_list else touches_num
                    if j > 0:
                        touches_num = True if tmp[i][j - 1] in num_list else touches_num
                    if j < width:
                        touches_num = True if tmp[i][j + 1] in num_list else touches_num

                    if not touches_num:
                        tmp[i][j] = ' '
        for i in range(depth + 1):
            for j in range(width + 1):
                if tmp[i][j] in num_list:
                    tmp[i][j] = ' '
                elif tmp[i][j] == '+':  # this plus just doesn't give up...

                    if i < depth and i > 0 and tmp[i + 1][j] in ['|', '+'] and tmp[i - 1][j] in ['|', '+']:
                        tmp[i][j] = '|'
                    elif j < width and j > 0 and tmp[i][j + 1] in ['-', '+'] and tmp[i][j - 1] in ['-', '+']:
                        tmp[i][j] = '-'

                    count = 0
                    if i < depth and tmp[i + 1][j] in ['|', '+']:
                        count += 1
                    if i > 0 and tmp[i - 1][j] in ['|', '+']:
                        count += 1
                    if j < width and tmp[i][j + 1] in ['-', '+']:
                        count += 1
                    if j > 0 and tmp[i][j - 1] in ['-', '+']:
                        count += 1
                    if count >= 3:
                        tmp[i][j] = '+'
        if self.double:
            tmp = self.smallify(tmp)
            result = "\n".join([("".join(x)).rstrip() for x in tmp])
            # if result not in self.cut_figures:
            self.cut_figures.append(result)

    def make_figures_list(self):
        self.true_vertices = []  # indeces of self.double_vertices that have correct lists of connected vertices
        used_vertices = []
        for x in self.vertices:
            max_vert = [0, 'none']
            if x not in self.fake_vertices and x not in used_vertices:
                for y in self.double_vertices:
                    if x in self.double_vertices[y]:
                        if len(self.double_vertices[y]) > max_vert[0]:
                            max_vert[0] = len(self.double_vertices[y])
                            max_vert[1] = y
                self.true_vertices.append(max_vert[1])
                for z in self.double_vertices[max_vert[1]]:
                    used_vertices.append(z)

        for num_key in self.double_vertices:
            #print("num_key:", num_key)
            fake = False
            for y in self.double_vertices[num_key]:
                #print("___num:", y)
                if y in self.fake_vertices:
                    fake = True
            if not fake:
                print("num_key:", num_key)
                print("___nums:", self.double_vertices[num_key])
                if len(self.cut_figures) == 2:
                    print("we're here")
                self.cut_out_figure(num_key)
        # for y in self.vertices:
        #    if y not in self.fake_vertices:
        #        self.cut_out_figure(y)
        return

    def print(self):
        for x in self.list_shape:
            line = []
            for y in x:
                if len(str(y)) == 1:
                    line.append("  " + str(y))
                elif len(str(y)) == 2:
                    line.append(" " + str(y))
                else:
                    line.append(y)

            print(line, self.width)
        print("____")
        i = 0
        while i < len(self.cut_figures):
            print(self.cut_figures[i])
            print("///////", i)
            i += 1
        '''
        for z in self.cut_figures:
            print(z)
            print("///////")
        '''
        """
        for y in self.vertices:
            if y not in self.fake_vertices:
                print(y, ": ", self.vertices[y])
        """


def break_evil_pieces(shape):
    s ="\n".join([x[0] for x in shape])
    # shape.splitlines()
    result = Solution(s)
    # result.overview_traversal()

    # result.double_init()

    result.overview_traversal()
    result.make_figures_list()
    result.print()


graph = [
["  +-----------------+"],
["  |+--------++-----+|"],
["  ||        ++     ||"],
["  |+--------+|     ||"],
["+++----------+     ||"],
["|++----------------+|"],
["|||+----------------+"],
["||||"],
["|||+------+"],
["||+-------+"],
["|+--------+"],
["+---------+"],
[""],
["+-----------+"],
["|+++------++|"],
["||++      ++|"],
["||        |||"],
["|+--------+||"],
["+----------+|"],
["+-----------+"]
]

graph2 = [
["+++----------+     ||"],
["|++----------------+|"],
["|||+----------------+"],
["||||"],
["|||+------+"],
["||+-------+"],
["|+--------+"],
["+---------+"]

]

graph3 = [
["         +-+"],
["         | |"],
["         | |"],
["    +----+ |"],
["    |+-----+    ++"],
["    ||          ||"],
["    ||  +-------+|"],
["    ||  |     +--+"],
["    ||  |     +---+"],
["    ||  +--------+|"],
["    |+-----------+|"],
["    +----+ +------+"],
["         | |"],
["         | |"],
["         | |"],
["         | |"],
["         | |"],
["       +-+ +-+"],
["       |     |"],
["+------+     +------+"],
["|                   |"],
["+-------------------+"]


]

#break_evil_pieces(graph3)




def cuckoo_clock(initial_time, n):
    print(initial_time, n)
    hour_minute = initial_time.split(':')
    hour = int(hour_minute[0])
    minutes = int(hour_minute[1])
    if minutes == 0:
        n -= hour
        minutes += 1
    while n > 0:
        if minutes == 60:
            hour = hour + 1 if hour < 12 else 1
            minutes = 0
            n -= hour
        elif minutes % 15 == 0:
            n -= 1
        minutes += 1
    hour_minute = [str(hour), str(minutes - 1)]
    for i in range(2):
        hour_minute[i] = hour_minute[i] if len(hour_minute[i]) > 1 else "0" + hour_minute[i]

    return hour_minute[0] + ':' + hour_minute[1]

#print(cuckoo_clock("01:58", 114))
#print(cuckoo_clock("12:22", 2))


def cuckoo_clock_better(initial_time, n):
    print(initial_time, n)
    hour_minute = initial_time.split(':')
    hour = int(hour_minute[0])
    minutes = int(hour_minute[1])
    if minutes != 0:
        n -= (60 - minutes) // 15
        hour = hour + 1 if hour < 12 else 1
        minutes = 0
    print(n)
    while n > 114: # in 12 hours clock chimes 114 times, returning to previous position
        n -= 114
    while n > 0:
        n -= hour + 3
        hour = hour + 1 if hour < 12 else 1
    #hour = hour - 1 if hour > 0 else 12
    if n < 0:
        hour = hour - 1 if hour > 0 else 12
        n += hour + 3
        minutes += abs(n) * 15

    hour_minute = [str(hour), str(minutes)]
    for i in range(2):
        hour_minute[i] = hour_minute[i] if len(hour_minute[i]) > 1 else "0" + hour_minute[i]

    return hour_minute[0] + ':' + hour_minute[1]

prod = 0
for i in range(1,13):
    #print(i)
    prod += i + 3

#print(prod)

#print(cuckoo_clock_better("01:58", 11))
#print(cuckoo_clock_better("12:30", 4))
#print(cuckoo_clock_better("07:22", 1))

def convert(x):
    if ord(x) > 97 and ord(x) < 123:
        return chr(ord(x) -1)
    elif ord(x) == 97:
        return 'z'
    elif ord(x) > 65 and ord(x) < 91:
        return chr(ord(x) -1)
    elif ord(x) == 65:
        return 'Z'
    else:
        return x

def one_down(txt):
    return "".join([convert(x) for x in txt]) if isinstance(txt, str) else "Input is not a string"


def domino_reaction(s):
    result = ""
    ss = list(s)
    for i in range(len(ss)):
        if s[i] != '|':
            result += "".join(ss[i:])
            break
        result += '/'
    return result

def good_vs_evil(good, evil):
    g_force = good.split()
    good_sum = int(g_force[0]) + int(g_force[1])*2 + int(g_force[2])*3 + int(g_force[3])*3 + int(g_force[4])*4 + int(g_force[5])*10
    e_force = evil.split()
    evil_sum = int(e_force[0]) + int(e_force[1])*2 + int(e_force[2])*2 + int(e_force[3])*2 + int(e_force[4])*3 + int(e_force[5])*5 + int(e_force[6])*10
    print("good:", good, " evil:", evil, "good_sum:", good_sum,"evil_sum:", evil_sum)
    if good_sum > evil_sum:
        return "Battle Result: Good triumphs over Evil"
    elif evil_sum > good_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"


def goodVsEvil2(good, evil):
    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]

    good = sum([int(x) * y for x, y in zip(good.split(), points_good)])
    evil = sum([int(x) * y for x, y in zip(evil.split(), points_evil)])

    result = 'Battle Result: '

    if good < evil:
        return result + 'Evil eradicates all trace of Good'
    elif good > evil:
        return result + 'Good triumphs over Evil'
    else:
        return result + 'No victor on this battle field'

def check_arr(arr, rng, check):
    dict = {}
    for x in arr:
        if x <= rng[1] and x >= rng[0] and x % 2 == check:
            if x not in dict:
                dict[x] = 0
            dict[x] += 1
    return dict

def find_arr(arrA, arrB, rng, wanted):
    check = 0 if wanted == "even" else 1
    dictA = check_arr(arrA, rng, check)
    dictB = check_arr(arrB, rng, check)
    result = set()
    for x in dictA:
        for y in dictB:
            if x == y and dictA[x]>1 and dictB[y]>1:
                result.add(x)
    res = [x for x in result]
    res.sort()
    return res

def find_arr2(arrA, arrB, rng, wanted):
    check = 0 if wanted == "even" else 1
    dictA = {}
    for x in arrA:
        if x <= rng[1] and x >= rng[0] and x % 2 == check:
            if x not in dictA:
                dictA[x] = 0
            dictA[x] -= 1
    result = []
    for x in arrB:
        if x not in dictA or dictA[x] == -1:
            continue
        if dictA[x] < 0:
            dictA[x] = 0
        dictA[x] += 1
        if dictA[x] == 2:
            result.append(x)
    result.sort()
    return result


from collections import Counter

def find_arr3(arrA, arrB, rng, wanted):
    ca, cb = Counter(arrA), Counter(arrB)
    m, n = rng
    m += (m % 2 == 1) == (wanted == 'even')
    r = range(m, n+1, 2)
    return [v for v in r if ca[v] > 1 and cb[v] > 1]


def interpreter_smallfuck(code, string_tape):
    print("code: ", code)
    print("tape: ", string_tape)
    flip = {
        '0': '1',
        '1': '0'
    }
    tape = [*string_tape]
    cell = 0
    length_tape = len(tape)
    i = 0
    length_code = len(code)
    while i < length_code:
        if code[i] == '*':
            tape[cell] = flip[tape[cell]]
        elif code[i] == '<':
            if cell > 0:
                cell -= 1
            else:
                return "".join(tape)
        elif code[i] == '>':
            if cell < length_tape - 1:
                cell += 1
            else:
                return "".join(tape)
        elif code[i] == '[' and tape[cell] == '0':
            stack = 0
            while i < length_code:
                if code[i] == ']':
                    stack -= 1
                elif code[i] == '[':
                    stack += 1
                if stack == 0:
                    break
                i += 1
            if i == length_code:
                i -= 1
        elif code[i] == ']':
            stack = 0
            while i >= 0 and stack != 0:
                if code[i] == ']':
                    stack -= 1
                elif code[i] == '[':
                    stack += 1
                if stack == 0:
                    break
                i -= 1
            if i < 0:
                i += 1
        i += 1
    return "".join(tape)

#print(interpreter_smallfuck("*>[[]*>]<*", "100"))

#rows = [[0] * 10] * 10
#print(rows)

def interpreter_original(code, iterations, width, height):
    graph = []
    for z in range(height):
        row = []
        for y in range(width):
            row.append('0')
        graph.append(row)
    print(graph)
    #graph = [['0'] * width] * height
    flip = {
        '0': '1',
        '1': '0'
    }
    iter = 0
    ind = 0
    i = 0
    j = 0
    while iter < iterations and ind < len(code):
        if code[ind] not in ['n', 'e', 's', 'w', '*', '[', ']']:
            ind += 1
            continue
        if code[ind] == '*':
            graph[i][j] = flip[graph[i][j]]
        if code[ind] == 'n':
            if i == 0:
                return graph
            i -= 1
        if code[ind] == 's':
            if i == height - 1:
                return graph
            i += 1
        if code[ind] == 'w':
            if j == 0:
                return graph
            j -= 1
        if code[ind] == 'e':
            if i == width - 1:
                return graph
            j += 1
        iter += 1
        ind += 1
    result = ""
    for x in graph:
        result += "".join([y for y in x]) + "\r\n"
    return result[:-2]

def interpreter(code, iterations, width, height):
    print("code: ", code)
    graph = []
    for z in range(height):
        row = []
        for y in range(width):
            row.append('0')
        graph.append(row)
    print(graph)
    # graph = [['0'] * width] * height - wrong
    # grid = [[0] * width for _ in range(height)] - right
    flip = {
        '0': '1',
        '1': '0'
    }
    iter = 0
    ind = 0
    i = 0
    j = 0
    while iter < iterations and ind < len(code):
        if code[ind] not in ['n', 'e', 's', 'w', '*', '[', ']']:
            ind += 1
            continue
        if code[ind] == '*':
            graph[i][j] = flip[graph[i][j]]
        elif code[ind] == 'n':
            if i == 0:
                i = height
            i -= 1
        elif code[ind] == 's':
            if i == height - 1:
                i = -1
            i += 1
        elif code[ind] == 'w':
            if j == 0:
                j = width
            j -= 1
        elif code[ind] == 'e':
            if j == width - 1:
                j = -1
            j += 1
        elif code[ind] == '[' and graph[i][j] == '0':
            stack = 0
            while ind < len(code):
                if code[ind] == ']':
                    stack -= 1
                elif code[ind] == '[':
                    stack += 1
                if stack == 0:
                    #ind += 1
                    break
                ind += 1
            if ind == len(code):
                ind -= 1
        elif code[ind] == ']' and graph[i][j] == '1':
            stack = 0
            while ind >= 0:
                if code[ind] == ']':
                    stack -= 1
                elif code[ind] == '[':
                    stack += 1
                if stack == 0:
                    # ind -= 1
                    break
                ind -= 1
            # if ind < 0:
            #    ind += 1
            # ind -= 1
        iter += 1
        ind += 1
    result = ""
    for x in graph:
        result += "".join([y for y in x]) + "\r\n"
    return graph#result[:-2]

result = interpreter("*[s[e]*]", 5, 6, 9)
#result = interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9)

for x in result:
    print(x)

def largest_sum(arr):
    result = 0
    max_val = 0
    for x in arr:
        result = max(0, result + x)
        max_val = max(max_val, result)
    return max_val

def convert(x):
    if ord(x) > 97 and ord(x) < 123:
        return chr(ord(x) -1)
    elif ord(x) == 97:
        return 'z'
    elif ord(x) > 65 and ord(x) < 91:
        return chr(ord(x) -1)
    elif ord(x) == 65:
        return 'Z'
    else:
        return x


def check(x):
    if (ord(x) >= 97 and ord(x) < 123) or (ord(x) >= 65 and ord(x) < 91) or ord(x) == 39:
        return True
    return False


def top_3_words(text):
    length = len(text)
    dict = {}
    i = 0
    top3 = [
        ["", 0],
        ["", 0],
        ["", 0],
        ["", 0]
    ]
    while i < length:
        word = ""
        check_2 = True
        while i < length and check(text[i]):
            if ord(text[i]) != 39:
                check_2 = False
            word += text[i]
            i += 1
        i += 1
        if word == "" or check_2:
            continue
        if word not in dict:
            dict[word] = 0
        dict[word] += 1
        j = 0
        found = False
        while j < 3:
            if top3[j][0] == word:
                found = True
                top3[j][1] += 1
                if j > 0 and top3[j][1] > top3[j-1][1]:
                    tmp = top3[j]
                    top3[j] = top3[j - 1]
                    top3[j - 1] = tmp
                break
            j += 1
        if found:
            continue
        j = 2
        while top3[j][1] < dict[word] and j >= 0:
            top3[j + 1] = top3[j]
            top3[j] = [word, dict[word]]
            j -= 1

    print(dict)
    return [x[0] for x in top3][:3]


print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))


from collections import Counter
import re

def top_3_words2(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]


def count_attacking_rooks(rooks):
    dict_let = {}
    dict_dig = {}
    for r in rooks:
        if r[0] not in dict_let:
            dict_let[r[0]] = 0
        dict_let[r[0]] += 1
        if r[1] not in dict_dig:
            dict_dig[r[1]] = 0
        dict_dig[r[1]] += 1
    result = 0
    for x in dict_let:
        result += dict_let[x] - 1
    for y in dict_dig:
        result += dict_dig[y] - 1
    return result


def id_best_users(*args):
    prev = {}
    for x in args[0]: # making the initial list of clients
        if x not in prev:
            prev[x] = 0
        prev[x] += 1
    for arr in args[1:]: # we remove a client that hasn't reappeared in subsequent month
        new = {}
        for y in arr:
            if y in prev:
                if y not in new:
                    new[y] = prev[y]
                new[y] += 1
        prev = new
    """ prev is the answer, the following code is just making it look like the instructions asked"""
    result = {}
    for z in prev: # make the dictionary multi-valued
        if prev[z] not in result:
            result[prev[z]] = []
        result[prev[z]].append(z)
    result2 = []
    for i in result: # turn dictionary into list (with sorted clients)
        result2.append([i, sorted(result[i])])
    for i in range(len(result2)): # sort the list by top clients
        for j in range(i, len(result2)):
            if result2[j][0] > result2[i][0]:
                tmp = result2[j]
                result2[j] = result2[i]
                result2[i] = tmp
    return result2


import math


def tour(friends, friend_towns, home_to_town_distances):
    current_location = "X1"
    distance = 0
    i = 0
    while i < len(friends):
        for x in friend_towns:
            if x[0] == friends[i]:
                if distance != 0:
                    tmp = math.sqrt(home_to_town_distances[x[1]] ** 2 - home_to_town_distances[current_location] ** 2)
                else:
                    tmp = home_to_town_distances[x[1]]  # first friend

                distance += tmp
                current_location = x[1]
                break
        i += 1
    return math.floor(distance) + home_to_town_distances[current_location]



def last_digit(n1, n2):
    n_1 = n1
    count = 1
    while True:
        n_1 = n_1 * n1
        while n_1 >= 10:
            n_1 = n_1 % 10
        count += 1
        if n_1 == n1:
            #count += 1
            break
    print("count", count)
    if count < n2:
        n2 = n2 % count -1
    result = 1
    for i in range(n2 - 1):
        #result *= default
        while result >= 10:
            result = result % 10
    return result

#print(last_digit(4, 2))
'''
#print(last_digit(3, 68819615221552997273737174557165657483427362207517952651))
print(68819615221552997273737174557165657483427362207517952651 % 4)

result = 3
result2 = 2
result3 = 4
for i in range(13):
    print(i, ", ", result, result2, result3)
    result *= 3
    result2 *= 2
    result3 *= 4
print(result)
'''

def last_digit_try(n1, n2):
    print(n1, n2)
    if n2 == 0:
        return 1

    n_1 = n1 if n1 < 10 else n1 % 10
    default = n_1
    count = 0
    while True:
        n_1 = n_1 * default
        n_1 = n_1 if n_1 < 10 else n_1 % 10
        count += 1
        if n_1 == default:
            # count += 1
            break
    print("count", count)
    if count == 0:
        return default
    if count < n2:
        n2 = (n2) % (count)
    print("n2", n2)
    # return (default ** n2) % 10
    result = default
    # result = (default ** 2) % 10
    for i in range(n2 - 1):
        result *= default
        # result = result if result < 10 else result % 10
    return result % 10

def last_digit_true(n1, n2):
    if n2 == 0:
        return 1
    # we count how many self-multplications does it take to get back to original last number
    n_1 = n1 % 10
    default = n_1
    count = 0
    while True:
        n_1 = (n_1 * default) % 10
        count += 1
        if n_1 == default:
            break

    if count == 0:
        return default
    # throwing away all multiplications that aren't meaningful, i.e. which return the last digit back to original
    n2 = (n2-1) % (count)
    if n2 == 0:
        return default
    # we raise the original last digit to meaningful exponent
    result = default
    for i in range(n2):
        result *= default
    return result % 10

def last_digit_slow(n1, n2):
    return pow( n1, n2, 10 )


def getting_mad(arr):
    min = 10000000
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            min = min if min < abs(arr[i] - arr[j]) else abs(arr[i] - arr[j])
    return min


def make_primes():
    primes = []
    for i in range(2, 100000):
        check = True
        for j in range(2, i//2):
            if i % j == 0:
                check = False
                break
        if check:
            primes.append(i)
    return primes


def count_Kprimes(k, start, end):
    primes = make_primes()
    result = []
    for x in range(start, end + 1):
        number = x
        count = k
        i = 0
        while x > 1 and count > 0 and i < len(primes):
            if x % primes[i] == 0:
                x = x / primes[i]
                count -= 1
            else:
                i += 1
        if count == 0 and x == 1:
            result.append(number)
    return result


def puzzle(s):
    primes1 = make_primes()
    primes3 = count_Kprimes(3, 0, 1000)
    primes7 = count_Kprimes(7, 0, 1000)
    result = []
    for x in primes7:
        if x > s:
            break
        for y in primes3:
            if x + y > s:
                break
            for z in primes1:
                if x + y + z == s:
                    if [x, y, z] not in result:
                        result.append([x, y, z])
                elif x + y + z > s:
                    break
    return len(result)

#print(puzzle(143))

#print(make_primes())

class Kprimes:
    primes = []

    def __init__(self):
        if self.primes:
            return
        for i in range(2, 100000):
            check = True
            for j in range(2, i):
                if i % j == 0:
                    check = False
            if check:
                self.primes.append(i)
        return

    def count_Kprimes(self, k, start, end):
        result = []
        for x in range(start, end + 1):
            number = x
            count = k
            i = 0
            while x > 1 and count > 0 and i < len(self.primes):
                if x % self.primes[i] == 0:
                    x = x / self.primes[i]
                    count -= 1
                else:
                    i += 1
            if count == 0 and x == 1:
                result.append(number)
        return result

    def puzzle(self, s):
        primes3 = self.count_Kprimes(3, 0, 1000)
        primes7 = self.count_Kprimes(7, 0, 1000)
        result = []
        for x in primes7:
            if x > s:
                break
            for y in primes3:
                if x + y > s:
                    break
                for z in self.primes:
                    if x + y + z == s:
                        if [x, y, z] not in result:
                            result.append([x, y, z])
                    elif x + y + z > s:
                        break
        return len(result)


def scramble(s1, s2):
    dict = {}
    for x in s2:
        if x not in dict:
            dict[x] = 0
        dict[x] += 1
    for y in s1:
        if y in dict:
            dict[y] -= 1
    for z in dict:
        if dict[z] > 0:
            return False
    return True


def scramble2(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

def largest_rect_1(histogram):
    if not histogram:
        return 0
    length = max(histogram)
    depth = len(histogram)
    maximum = 0
    for i in range(length):
        maxi = 0
        count = 0
        for j in range(depth):
            if histogram[j] >= i:
                count += i
                maxi = max(maxi, count)
            else:
                count = 0
        maximum = max(maxi,maximum)
    return maximum

def largest_rect_2(histogram):
    if not histogram:
        return 0
    maxi = 0
    for i in range(len(histogram)):
        j = i
        z = i
        count = histogram[i]
        current = histogram[i]
        while j > 0 and histogram[j-1] >= current:
            count += current
            j -= 1
        while z < len(histogram)-1 and histogram[z+1] >= current:
            count += current
            z += 1
        maxi = max(maxi, count)
    return maxi

#print(largest_rect([1, 1, 1]))


def king_is_in_check(chessboard) -> bool:
    depth = len(chessboard)
    length = len(chessboard[0])
    i = 0
    while i < depth:
        j = 0
        found = False
        while j < length:
            if chessboard[i][j] == '♔':
                found = True
                break
            j += 1
        if found:
            break
        i += 1
    print(i, j)
    ver = i
    hor = j
    if ver - 1 >= 0 and hor - 1 >= 0 and chessboard[ver - 1][hor - 1] == '♟':
        return True
    if ver - 1 >= 0 and hor + 1 < length and chessboard[ver - 1][hor + 1] == '♟':
        return True
    """Checking Rooks"""
    while i + 1 < depth:
        if chessboard[i + 1][hor] in ['♜', '♛']:
            return True
        if chessboard[i + 1][hor] != ' ':
            break
        i += 1
    i = ver
    while i - 1 >= 0:
        if chessboard[i - 1][hor] in ['♜', '♛']:
            return True
        if chessboard[i - 1][hor] != ' ':
            break
        i -= 1
    i = ver
    while j + 1 < length:
        if chessboard[ver][j + 1] in ['♜', '♛']:
            return True
        if chessboard[ver][j + 1] != ' ':
            break
        j += 1
    j = hor
    while j - 1 >= 0:
        if chessboard[ver][j - 1] in ['♜', '♛']:
            return True
        if chessboard[ver][j - 1] != ' ':
            break
        j -= 1
    j = hor
    """checking Bishops"""
    while i + 1 < depth and j + 1 < length:
        if chessboard[i + 1][j + 1] in ['♝', '♛']:
            return True
        if chessboard[i + 1][j + 1] != ' ':
            break
        i+=1
        j+=1
    j = hor
    i = ver
    while i - 1 >= 0 and j - 1 >= 0:
        if chessboard[i - 1][j - 1] in ['♝', '♛']:
            return True
        if chessboard[i - 1][j - 1] != ' ':
            break
        i-=1
        j-=1
    j = hor
    i = ver
    while i + 1 < depth and j - 1 >= 0:
        if chessboard[i + 1][j - 1] in ['♝', '♛']:
            return True
        if chessboard[i + 1][j - 1] != ' ':
            break
        i+=1
        j-=1
    j = hor
    i = ver
    while i - 1 >=0 and j + 1 < length:
        if chessboard[i - 1][j + 1] in ['♝', '♛']:
            return True
        if chessboard[i - 1][j + 1] != ' ':
            break
        i-=1
        j+=1
    j = hor
    i = ver
    """Checking for Knights"""
    if i - 2 >= 0 and j - 1 >= 0 and chessboard[i - 2][j - 1] == '♞':
        return True
    if i - 2 >= 0 and j + 1 < length and chessboard[i - 2][j + 1] == '♞':
        return True
    if i + 2 < depth and j - 1 >= 0 and chessboard[i + 2][j - 1] == '♞':
        return True
    if i + 2 < depth and j + 1 < length and chessboard[i + 2][j + 1] == '♞':
        return True
    if i - 1 >= 0 and j - 2 >= 0 and chessboard[i - 1][j - 2] == '♞':
        return True
    if i + 1 < depth and j - 2 >= 0 and chessboard[i + 1][j - 2] == '♞':
        return True
    if i - 1 >= 0 and j + 2 < length and chessboard[i - 1][j + 2] == '♞':
        return True
    if i + 1 < depth and j + 2 < length and chessboard[i + 1][j + 2] == '♞':
        return True
    return False









