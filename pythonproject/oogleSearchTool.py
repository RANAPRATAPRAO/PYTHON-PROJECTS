# install one library called google
from googlesearch import search
query= "Ranaprataprao"
for i in search(query, start=0, pause=2):
    print(i)