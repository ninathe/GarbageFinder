from xml.etree import ElementTree as ET
tree = ET.parse('Annotation/DJI_0180.xml')
root = tree.getroot()
file = open("annotations.txt", "w")

print("./%s" %(root.find('filename').text))
file.write("./"+root.find('filename').text)
for object in root.findall('.//object'):
    bndbox = object.find('bndbox')
    file.write("%s,%s,%s,%s,%s" % (bndbox.find('xmin').text,bndbox.find('ymin').text, bndbox.find('xmax').text, bndbox.find('ymax').text, object.find('name').text))
    file.write(' ') 
    # print("%s,%s,%s,%s,%s" % (bndbox.find('xmin').text,bndbox.find('ymin').text, bndbox.find('xmax').text, bndbox.find('ymax').text, object.find('name').text))

file.close