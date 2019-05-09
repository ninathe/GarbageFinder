from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('Annotation/DJI_0180.xml')

imageFilePath = mydoc.getElementsByTagName('filename')

items = mydoc.getElementsByTagName('object')

# all item attributes
print('\nAll attributes:')  
for elem in items: 
    print(elem.getElementsByTagName('bndbox')) 
    # print(elem.attributes['bndbox'].attributes['xmin'].value)
    # print(elem.bndbox.attributes['ymin'].value)
    # print(elem.bndbox.attributes['xmax'].value)
    # print(elem.bndbox.attributes['ymax'].value)
    # print(elem.bndbox.attributes['name'].value)



# # one specific item's data
# print('\nItem #2 data:')  
# print(items[1].firstChild.data)  
# print(items[1].childNodes[0].data)

# # all items data
# print('\nAll item data:')  
# for elem in items:  
#     print(elem.firstChild.data)

# image_file_path box1 box2 ... boxN
# x_min,y_min,x_max,y_max,class_id