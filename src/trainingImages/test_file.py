import os

source = ''

while not os.path.exists(source):
    print("Enter your source folder: ")
    source = input()
    if not os.path.exists(source):
        print("You source path does not exist")

print("\nEnter your destination location: ")
destination = input()