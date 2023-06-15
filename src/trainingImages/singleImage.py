import ast
import cv2 as cv
import sys
import os

from src.trainingImages.FileOperationsFunction import sendTo

imageData = "/Users/ferretdragon/Documents/Eye_to_Eye/facelessImageData.txt"
allContent = []

def addContentToList(file_path):
    """Open data file, convert lines to lists, return list"""
    tempFile = open(file_path)
    tempList=[]
    for line in tempFile:
        tempList.append((ast.literal_eval(line)))
    tempFile.close()
    return tempList
allContent = addContentToList(imageData)

def whenFeatureNotFound(e):
    for imageListData in allContent:
        if not os.path.exists(imageListData[3]):
            continue
        img = cv.imread(imageListData[3])
        cv.imshow("image", img)

        while 1:
            key = cv.waitKey(5000)
            if key == -1 or key == ord("q"):
                cv.destroyAllWindows()
                break
            elif key == ord("m"):
                print(imageListData[3])
                print(type(imageListData[3]))
                with open("/Users/ferretdragon/Documents/Eye_to_Eye/notRealImages/NotRealImagesRecord.txt","a+") as filename:
                    filename.write(imageListData[3] + "\n")
                sendTo("/Users/ferretdragon/Documents/Eye_to_Eye/notRealImages",imageListData[3])

# 1=left 2=right
whenFeatureNotFound(2)
#cv.imshow("test_image",image)

