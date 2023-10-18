import csv
with open('/Users/ferretdragon/Documents/TrainingImages/ImageLocationsAndNumberOfFaces.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        print("The image is located at " + row["Image Location"] + " and the number of faces expected is " + row["Number of Faces"])

    print(dir(dict))
    #print(help(dict.values))