#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Vicki.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: R


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count = input('Enter count - ')
position = input('Enter position - ')

a = int(count)
b = int(position)


for i in range(a+1):
    links = []
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href', None))
    print(url)
    url = links[b - 1]
