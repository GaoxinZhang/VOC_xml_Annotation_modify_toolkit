import os


def IsSubString(SubStrList, Str):
    flag = True
    for substr in SubStrList:
        if not (substr in Str):
            flag = False

    return flag


def GetFileList(FindPath, FlagStr=[]):
    FileList = []
    FileNames = os.listdir(FindPath)
    if len(FileNames) > 0:
        for fn in FileNames:
            if len(FlagStr) > 0:
                if IsSubString(FlagStr, fn):
                    fullfilename = os.path.join(FindPath, fn)
                    FileList.append(fullfilename)
            else:
                fullfilename = os.path.join(FindPath, fn)
                FileList.append(fullfilename)

    if len(FileList) > 0:
        FileList.sort()

    return FileList


train_txt = open('train.txt', 'w')
imgfile = GetFileList('scratch/train/high')
for img in imgfile:
    str1 = img + ' ' + '1' + '\n'
    train_txt.writelines(str1)

imgfile = GetFileList('scratch/train/low')
for img in imgfile:
    str2 = img + ' ' + '0' + '\n'
    train_txt.writelines(str2)
train_txt.close()

# val
test_txt = open('val.txt', 'w')
imgfile = GetFileList('scratch/val/high')
for img in imgfile:
    str3 = img + ' ' + '1' + '\n'
    test_txt.writelines(str3)

imgfile = GetFileList('scratch/val/low')
for img in imgfile:
    str4 = img + ' ' + '0' + '\n'
    test_txt.writelines(str4)
test_txt.close()

print("Done")