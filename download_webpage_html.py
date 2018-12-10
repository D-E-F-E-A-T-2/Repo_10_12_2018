import urllib.request
give = input("Give link")
try:
    url = urllib.request.urlopen(give)
    content = url.read()
except urllib.error.HTTPError:
    print("Webpage not found")
    exit()

f = open('reader.html', 'wb')
f.write(content)
f.close()
