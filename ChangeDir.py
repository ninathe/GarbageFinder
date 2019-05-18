import os
 
wd = os.getcwd()

def lowercase_rename( dir ):
    # renames all subforders of dir, not including dir itself
    def rename_all( root, items):
        for name in items:
            try:
                os.rename( os.path.join(root, name), 
                                    os.path.join(root, name.lower()))
            except OSError:
                pass # can't rename it, so what

    # starts from the bottom so paths further up remain valid after renaming
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all( root, dirs )
        rename_all( root, files)



def changeDirectory(typ, wd):
    dirname = './coco/labels/%s2018'%(typ)
    name = 'COCO_%s2018_'%(typ)
    names = [f[:-4] for f in os.listdir(dirname) if f[-4:].lower() == '.txt']
    files = [f[len(name):] for f in names if f[:len(name)] == name]
    for f in files:
        os.rename('%s/images/%s.jpg'%(wd, f), '%s/coco/images/%s2018/COCO_%s2018_%s.jpg'%(wd, typ, typ, f))



# lowercase_rename(wd+"/images")
# changeDirectory("val", wd)


 