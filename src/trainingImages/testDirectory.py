import os
import imghdr


def searchDir(pathBeforeVariable, fileList):
    '''Input file path, and operated list of files'''

    if os.path.isdir(pathBeforeVariable) is True:
        for itemName in os.listdir(pathBeforeVariable):
            newPath = pathBeforeVariable + "/" + itemName
            searchDir(newPath, fileList)
    elif imghdr.what(pathBeforeVariable) == "jpeg":
        fileList.append(pathBeforeVariable)

if __name__ == "__main__":

    pathway = "/Users/ferretdragon/Documents/UMaskLFW"
    list = []

    searchDir(pathway, list)


    print(len(list))

    for i in range(0,10):
        print(list[i])

    print("..." + list[-1])