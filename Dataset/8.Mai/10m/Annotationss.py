import json
file = open("annotations.txt", "w")
annotation_num = 0

with open('annotations.json') as f:
    data = json.load(f)

for image in data["images"]:
    file.write('\n'+image["file_name"]+ " ")

    for annotation in data["annotations"]:
        
        if(image["id"] == annotation["image_id"]):
            annotation_num += 1
            bbox = annotation["bbox"]
            xmin = bbox[0]
            ymin = bbox[3]
            xmax = bbox[1]
            ymax = bbox[2]
            category = annotation["category_id"]
            file.write("%s,%s,%s,%s,%s" % (xmin, ymin, xmax, ymax, category))
            file.write(' ') 
file.write("Annotations: " + str(annotation_num))
         

file.close()