from urllib2 import urlopen
import json
req=[]
import re
def gitscrape(s):
#s="www.github.com/rohitanil"
    if re.findall(r'[\w]+.github.com/(\w+)',s):
        cont=re.findall(r'[\w]+.github.com/(\w+)',s)
        #print(cont)
        str1="".join(cont)
        #print(str1)
        link=["https://api.github.com/users/"]
        link.append(str1)
        x="".join(link)
        req=urlopen(x).read()
        data=json.loads(req)
        return(data['public_repos'],data['followers'])
    else:
            return 0                





#soup=bs4.BeautifulSoup(req,'lxml')
#buffer=soup.find_all()
#print(buffer)

