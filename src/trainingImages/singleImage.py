import ast
import cv2 as cv
import sys
import os

"""from src.trainingImages.FileOperationsFunction import sendTo"""
from FileOperationsFunction import sendTo

fileLocationThatContainsImageData = ''

while not os.path.exists(fileLocationThatContainsImageData):
    # Data file should be the path to the txt file in which the image locations are stored
    print("Enter the name of your image data file: ")
    fileLocationThatContainsImageData = input()
    if not os.path.exists(fileLocationThatContainsImageData):
        print("You source path does not exist")

print("\nEnter your destination folder location: ")
#The folder where we want to move the images into
destination = input()

allContent = []

def addContentToList(file_path):
    """Open data file, convert lines to lists, return list"""
    tempFile = open(file_path)
    tempList=[]
    for line in tempFile:
        tempList.append((ast.literal_eval(line)))
    tempFile.close()
    return tempList

allContent = addContentToList(fileLocationThatContainsImageData)

def manuallySortThroughImages(listOfImagesToFilterThrough):
    '''We are expecting to be passed a list of lists formated with features [[a,b,c, imageLocationPathway], ...]'''
    for imageListData in allContent:

        currentImagePathway = imageListData[3]
        if not os.path.exists(currentImagePathway):
            continue
        img = cv.imread(currentImagePathway)
        cv.imshow("image", img)

        while 1:
            key = cv.waitKey(5000)
            if key == -1 or key == ord("q"):
                cv.destroyAllWindows()
                break
            elif key == ord("m"):
                print(currentImagePathway)
                print(type(currentImagePathway))
                with open(destination + "/movedImages.txt","a+") as filename:
                    filename.write(currentImagePathway + "\n")
                sendTo(destination,currentImagePathway)
                cv.destroyAllWindows()
                break

manuallySortThroughImages(allContent)
#cv.imshow("test_image",image)

