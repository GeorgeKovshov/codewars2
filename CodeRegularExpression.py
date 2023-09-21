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



#print(pig_it3('Pig latin is cool !'))
#print(pig_it3('This is my string ?'))


def strip_comments1(strng, markers):
    if markers == []:
        return strng
    patt = ""
    for item in markers:
        if item == '-':
            patt += '\\'
        elif item == '\\':
            patt += '\\'
        patt += str(item)
    pattern = r"(\w*|\d*|\s)+(\s?["
    pattern += patt
    pattern +="])?(.*)?(\n|$)"
    string1= re.sub(pattern, r"\1\4",strng)
    return string1
    #string1 = pattern.finditer(strng)
    #print(string1)
    #for item in string1:
    #    print(item.group(1,2))

def strip_comments2(strng, markers):
    if markers == []:
        return strng
    patt = ""
    for item in markers:
        if item == '-':
            patt += '\\'
        elif item == '\\':
            patt += '\\'
        patt += str(item)
    pattern = r"(([ \t]*[^ \t"
    pattern += patt
    pattern += r"]+)*)([ \t]?["
    pattern += patt
    pattern += r"])?(.*)?(\n|$)"
    string1= re.sub(pattern, r"\1\5",strng)
    return string1

def strip_comments(strng, markers):
    if markers == []:
        return strng
    # patt is a string of markers we add into a regex expression
    patt = "".join(['\\' + str(item) if item in ['-', '\\'] else item for item in markers])
    """ 
        We create groups:
             avocados = @ bananas oranges cherries\n" \
            (avocados =)( @)( bananas oranges cherries)(\n)" 
                 (1+2)  ( 3)         (4)               (5) 
        We just return (1) and (5):
             avocados =\n
    """
    pattern = r"(([ \t]*[^ \t" + patt + r"]+)*)([ \t]?[" + patt + r"])?(.*)?(\n|$)"
    return re.sub(pattern, r"\1\5", strng)


solution1=lambda t,m,r=__import__('re'):r.sub(r'( *[{}].*)'.format(r.escape(''.join(m))),'',t)if m else t


#print('\\')
#print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))

tring= "avocados strawberries bananas '\n" \
        "lemons @ oranges ! ! pears\n" \
        "- @ watermelons avocados @ watermelons\n" \
        "avocados = @ bananas oranges cherries\n" \
        "pears ."
Markers= ['-', "'"]
#print(strip_comments(tring, Markers))

'avocados strawberries bananas\n' \
'lemons @ oranges ! ! pears\n' \
'avocados = @ bananas oranges cherries\n' \
'pears .' #should equal
'avocados strawberries bananas\n' \
'lemons @ oranges ! ! pears\n' \
'\n' \
'avocados = @ bananas oranges cherries\n' \
'pears .'


#regex_new = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]){6,}")
regex_new = re.compile(r"(?=.*[a-z]).{6}")
"""
My password strength criteria is as below :
8 characters length
2 letters in Upper Case
1 Special Character (!@#$&*)
2 numerals (0-9)
3 letters in Lower Case"""
"^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$"

#text_new = "fjd3IR9"
#text_new = "12345"
text_new = "asd3faf"

match_start = regex_new.match(text_new)
#print(match_start)



def validate_password(password):
    # define our regex pattern for validation
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[^A-Za-z0-9]).{8,}$"

    # We use the re.match function to test the password against the pattern
    match = re.match(pattern, password)

    # return True if the password matches the pattern, False otherwise
    return bool(match)

password1 = "StrongP@ssword123"
password2 = "weakpassword"
print(validate_password(password1))
print(validate_password(password2))


"""WORKED THE FOLLOWING:
At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a digit
only contains alphanumeric characters (note that '_' is not alphanumeric)

"""

regex_pass = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[^A-Za-z0-9]).{6,}$"

"""
the lookaheads (?= ____) are checking the presence of letters in string (but don't move the "checking" ahead),
 the .{6,} checks the length - the space after comma is blank means infinity
"""