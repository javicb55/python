#https://www.uja.es/

import urllib as u
import requests
from lxml import html


link = "https://www.uja.es/"
f = u.request.urlopen(link)
myfile = f.read()
#print(myfile)

page = requests.get(link)
tree = html.fromstring(page.content)

meta = tree.xpath('//div[@class=slide__title]/text()')

print(meta)