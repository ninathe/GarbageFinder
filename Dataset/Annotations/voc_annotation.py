import os,random

# read the filenames from a file
print("START")
dirname = './Annotations'
files = [f[:-4] for f in os.listdir(dirname) if f[-4:].lower() == '.xml']
print("HEI")
print(files)

# random divide  
trainval = random.sample(files, len(files)//2)
test = [f for f in files if f not in trainval]

# random divide 
train = random.sample(trainval, len(trainval)//2)
val = [f for f in trainval if f not in train]

# save to txt file
def list2txt(arr, fname):
    with open(fname+'.txt', 'w') as f:
        for a in arr:
            f.write(a+'\n')

list2txt(trainval, 'trainval')
list2txt(test, 'test')
list2txt(train, 'train')
list2txt(val, 'val')