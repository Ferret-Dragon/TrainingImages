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
    if not os.path.exists(directoryLocationThatContainsImages):
        print("You source path does not exist")

listOfImagesFromDirectory = []

searchDir(directoryLocationThatContainsImages,listOfImagesFromDirectory)
print("\nEnter your destination folder location: ")
#The folder where we want to move the images into
destination = input()

def manuallySortThroughImages(listOfImagesToFilterThrough):
    '''We are expecting to be passed a list of lists formated with features [[a,b,c, imageLocationPathway], ...]'''
    for imageLocation in listOfImagesToFilterThrough:

        if not os.path.exists(imageLocation):
            continue
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

manuallySortThroughImages(listOfImagesFromDirectory)
#cv.imshow("test_image",image)

