#The program will prompt for a URL, 
#read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1384450.xml (Sum ends with 38)

from urllib import request
import xml.etree.ElementTree as ET

url = input('Enter - ')
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)

counts = tree.findall('comments/comment')

print("count:",len(counts))

summe = 0
for i in counts:
    summe = summe + int(i.find('count').text)

print("Sum:",summe)
