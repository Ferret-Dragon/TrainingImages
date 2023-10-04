import ast
import cv2 as cv
import sys
import os

from FileOperationsFunction import sendTo
from testDirectory import searchDir
from enum import Enum

class Mode(Enum):
    SET_NUM_FACES = 1
    FILTER_NO_FACES = 2

mode = 0
while not (mode==1 or mode==2):
    print("Enter 1 to set and compare the number of faces.\nEnter 2 to filter out images with no faces")
    mode = int(input())

if(mode == 1):
    setting = Mode.SET_NUM_FACES
elif(mode == 2):
    setting = Mode.FILTER_NO_FACES
else:
    setting = None

directoryLocationThatContainsImages = ''

while not os.path.exists(directoryLocationThatContainsImages):
    # Data file should be the path to the txt file in which the image locations are stored
    print("Enter the name of your image data directory: ")
    directoryLocationThatContainsImages = input()

    if directoryLocationThatContainsImages == "directory":
        directoryLocationThatContainsImages = "/Users/ferretdragon/Documents/UMaskLFW"
    if not os.path.exists(directoryLocationThatContainsImages):
        print("You source path does not exist")

listOfImagesFromDirectory = []

searchDir(directoryLocationThatContainsImages,listOfImagesFromDirectory)

if(mode == 2):
    print("\nEnter your destination folder location: ")
    #The folder where we want to move the images into
    destination = input()

def manuallySortThroughImages(listOfImagesToFilterThrough, listOfNumberOfFaces):
    '''We are expecting to be passed a list of image pathways in the form of strings [[a,b,c, imageLocationPathway], ...]'''
    for imageLocation in listOfImagesToFilterThrough:
            if not os.path.exists(imageLocation):
                continue
            if setting == Mode.SET_NUM_FACES:
                listOfNumberOfFaces.append((imageLocation, setNumFacesProcess(imageLocation)))
            if setting == Mode.FILTER_NO_FACES:
                filterNoFacesProcess(imageLocation)

def setNumFacesProcess(imageLocation)->int:
    ''' Return an integer value telling how many faces we expect to see in each individual image location input'''
    img = cv.imread(imageLocation)
    cv.imshow(img)
    while (1):
        numOfFacesInImage = cv.waitKey()
        try:
            numOfFacesInImage = int(chr(numOfFacesInImage))
            break
        except:
            print("Must be an integer input.")
    return numOfFacesInImage

def filterNoFacesProcess(imageLocation):
    img = cv.imread(imageLocation)
    cv.imshow("image", img)
    while 1:
        key = cv.waitKey(5000)
        if key == -1 or key == ord("q"):
            cv.destroyAllWindows()
            break
        elif key == ord("m"):
            print(imageLocation)
            print(type(imageLocation))
            with open(destination + "/movedImages.txt","a+") as filename:
                filename.write(imageLocation + "\n")
            sendTo(destination,imageLocation)
            cv.destroyAllWindows()
            break

listOfListsAndNumsOfFaces = []
manuallySortThroughImages(listOfImagesFromDirectory, listOfListsAndNumsOfFaces)
#cv.imshow("test_image",image)

