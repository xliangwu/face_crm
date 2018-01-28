import os
import xml.etree.ElementTree as ET

data = b'''<?xml version="1.0" encoding="UTF-8"?>
<Event>
   <ID>7</ID>
   <BlackList>BlackList</BlackList>
   <RealList>RealList</RealList>
   <CollectTime>2017-12-04 06:35:47</CollectTime>
   <Confidence>0.669651</Confidence>
</Event>
'''

print(len(data))
root = ET.fromstring(data)
print(root)

for child in root:
    print(child.tag, child.attrib, child.text)

blackTag = root.find('BlackList')
print(blackTag, blackTag.text)

realTag = root.find('RealList')
print(realTag, realTag.text)

confidenceTag = root.find('Confidence')
print(confidenceTag, confidenceTag.text)
