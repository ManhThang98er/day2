import xml.etree.ElementTree as ET
import time
#from datetime import datetime
#createAt = calendar.timegm(time.gmtime())

tree = ET.parse('test.xml')

root = tree.getroot()
print ("id      name   age  createAt")
for book in root.findall('people'):
  id = book.get('id')
  name = book.find("name").text
  age = book.find("age").text
  createAt = book.get('createAt')
  #ts = datetime.fromtimestamp(int(createAt))
  ts = time.strftime('%d/%m/%Y', time.localtime(int(createAt)))
  print(id, name, age, ts )

#time_stamp = createAt


