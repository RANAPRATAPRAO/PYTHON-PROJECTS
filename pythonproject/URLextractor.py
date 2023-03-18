# NO need to install anything here
# just we have to o import urlopen and called urlopen function
from urllib.request import urlopen
page=urlopen("https://google.com")
print(page.headers)