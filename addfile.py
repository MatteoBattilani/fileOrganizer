
import shutil
import os
import magic
import time
import csv
import argparse

# I create the file path and a list containing all the files.
source = os.path.join(os.getcwd(), 'files')
files = os.listdir('files')

# List of files to be excluded
exclude = ["Resoconto.csv", "audio", "docs", "images"]
# Lista contenente i soli file da spostare
fileSelection = [file for file in files if file not in exclude]

# Supported extension tuples
audioExtensions = (".mp3")
textExtensions = (".txt", ".odt")
imageExtensions = (".jpeg", ".png", ".jpg")

# I set the parser and configure only one argument
parser = argparse.ArgumentParser(description= "Script to move a single file at a time.")
parser.add_argument("file", type=str, help="Files you can move", choices =fileSelection)
args = parser.parse_args()

# Code branch only entered if the .cvs file does NOT yet exist
if not os.path.exists(os.path.join(source, 'Resoconto.csv')):

    # If it does not yet exist, I create the .csv file and write the column headers in it
    header = ['NAME', 'TYPE', 'SIZE']
    row = []
    with open(os.path.join(source,'Resoconto.csv'), 'w') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(header)

# If the name of the file entered by the user matches one of those in the folder then I move it
if args.file in files:
    # I set the variables to print the name, type and size of each file and then print them out
    fileName = os.path.splitext(args.file)[0]
    fileSize = os.path.getsize(os.path.join(source, args.file))
    fileType = magic.from_file(os.path.join(source, args.file), mime=True)

    # I open the "Report.csv" file and add the file information to it (the .cvs file will NOT be overwritten).
    with open(os.path.join(source, "Resoconto.csv"), 'a', newline='') as myfile:
        row = [fileName, fileType, fileSize]
        wr = csv.writer(myfile)
        wr.writerow(row)
    print("File identified: " + fileName + " type:" + str(fileType) + " size: " + str(fileSize) + "B")
    time.sleep(1)
    print("I am moving the file" + str(args.file) + "...")
    time.sleep(1)

    # I identify if a file is an audio file and move it to the correct folder. If this does not exist, I create it.
    if args.file.endswith(audioExtensions):
        destination = os.path.join(source, 'audio')
        if not os.path.exists(destination):
            os.makedirs(destination)
        new_path = shutil.move(os.path.join(source, args.file), destination)
        print("The file " + str(args.file) + "  has been correctly moved!")

    # I identify if a file is text and move it to the correct folder. If this does not exist, I create it.
    elif args.file.endswith(textExtensions):
        destination = os.path.join(source, 'docs')
        if not os.path.exists(destination):
            os.makedirs(destination)
        new_path = shutil.move(os.path.join(source, args.file), destination)
        print("The file " + str(args.file) + "  has been correctly moved!")

    # I identify whether a file is an image and move it to the correct folder. If this does not exist, I create it.
    elif args.file.endswith(imageExtensions):
        destination = os.path.join(source, 'images')
        if not os.path.exists(destination):
            os.makedirs(destination)
        new_path = shutil.move(os.path.join(source, args.file), destination)
        print("The file " + str(args.file) + " has been correctly moved!")



