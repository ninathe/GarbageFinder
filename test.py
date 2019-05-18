import os
 
wd = os.getcwd()
val_ids = os.listdir()
val = 'COCO_val2018_'
train = 'COCO_train2018_'
i = len(val)

dirtrain = './images'
filesTr = [f[:-4] for f in os.listdir(dirtrain) if f[-4:].lower() == '.jpg']
for tf in filesTr:
    os.rename('%s/images/%s.jpg'%(wd, tf), '%s/coco/images/train2018/%s%s.jpg'%(wd, train, tf))




 