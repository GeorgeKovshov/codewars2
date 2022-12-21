import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = "Start a sentence and bring it to an end"

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.come
https://www.nasa.gov
'''

print('\tTab')
print(r'\tTab') #raw string

pattern = re.compile(r'Ha')
pattern2 = re.compile(r'start', re.I) # or re.IGNORECASE returns if all caps or none or between
pattern3 = re.compile(r'sentence')

matchss = pattern.findall((text_to_search))
matches = pattern.finditer(text_to_search)

match_start = pattern2.match(sentence) # matches at the beginning of a string
match_search = pattern3.search(sentence) # finds the FIRST match and returns it
print(match_start)
print(match_search)

urlsss = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
urlsssZ = urlsss.finditer(urls)

for match in matches:
    print(match)

for match in urlsssZ:
    print(match.group(2, 3))

subbed_urls = urlsss.sub(r'\2\3', urls)
print(subbed_urls)
