import os
import shutil
# Goals

# 1. A function that takes in a Current File Path, and a Destination Folder
# 2. If the Destination Folder does not exist, create the Destination Folder
# 3. Move the Current File to the Destination Folder


def sendTo(dest, fileName):
    if os.path.exists(dest):
        if not os.path.exists(dest + "/" + fileName):
            shutil.move(fileName,dest)
    else:
        os.mkdir(dest)
        shutil.move(fileName,dest)

if __name__ == "__main__":
    sendTo("/Users/ferretdragon/Documents/Eye_to_Eye/NewFolder","/Users/ferretdragon/Documents/Eye_to_Eye/Test_Code/filename.txt")