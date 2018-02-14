#read xml using lxml

from lxml import etree as et

str1 = '1234 test'
print (str1.split(' ')[0])
#doc = et.parse('simple.xml')
doc = et.parse('bank.xml')
#node1 = et.Element()
nodes = doc.findall('items')
for tmpnode in nodes:
    print (tmpnode.tag)
    print (tmpnode.get('busin_flag'))