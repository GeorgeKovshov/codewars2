import re

def pig_it1(text):
    pattern = re.compile("(?:^|\s)\w")
    pattern2 = re.compile("\w(?:\s|$)")
    match = pattern.findall(text)
    match2 = pattern2.findall(text)
    print(match)
    print(match2)
    length = len(text)
    match_iter = pattern.finditer(text)
    match_iter2 = pattern2.finditer(text)

    for match in match_iter:
        tmp = match
        tmp1 = match_iter2.__next__()
        if tmp.start()==0:
            white = ""
        else:
            white = " "
        if tmp1.end()==length:
            black = ""
        else:
            black = " "
        text = text[:tmp.start()] + white + tmp1.group().rstrip() + text[tmp.end():]
        text = text[:tmp1.start()] + tmp.group().lstrip() + black + text[tmp1.end():]

    print(text)

def pig_it(text):
    pattern = re.compile("(?:\s|^)\w")
    matches = pattern.finditer(text)
    i=-1
    bar = ""
    for match in matches:
        if i==-1:
            text = text[:match.start()] + bar + text[match.end():]
        else:
            text = text[:match.start()-1 + i*2] + bar + text[match.end()-1 + i*2:]
        print(text)
        bar = match.group().strip() + "ay "
        i+=1
    if text[-1] in ['!', '?', '.']:
        text = text[:-2] + bar + text[-1] + text[-2:-1]
    else:
        text += bar
    return text[:-1]



def pig_it2(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)


def pig_it3(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)



print(pig_it3('Pig latin is cool !'))
print(pig_it3('This is my string ?'))