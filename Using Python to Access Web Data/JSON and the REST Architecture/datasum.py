import urllib.request, urllib.parse, urllib.error
from urllib import request
import json

#prompt for a URL and retrieve data from a URL
url = input('Enter - ')
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()

info = json.loads(data)
print(type(info))

summe = 0
for item in info["comments"]:
    count = int(item["count"])
    summe = summe + count

#wrong vision
#for item in info:
#    count = int(item["comments"]["count"])
#TypeError: string indices must be integers

print(summe)
    