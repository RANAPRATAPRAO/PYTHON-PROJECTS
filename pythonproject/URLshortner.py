# install one library called pyshorteners
import pyshorteners
url=input("enter url that you want to short")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)
