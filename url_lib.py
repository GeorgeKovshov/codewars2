from urllib import request

resp = request.urlopen("https://www.wikipedia.org")

print(type(resp))
print(resp.code)
print(resp.length)
#print(resp.peek())
data = resp.read()
html = data.decode("UTF-8") #wikipedia html code in string
