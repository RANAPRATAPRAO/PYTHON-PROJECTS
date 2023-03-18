from urllib.request import urlopen
page=urlopen("https://google.com")
sourcecode=page.read()
print(sourcecode)