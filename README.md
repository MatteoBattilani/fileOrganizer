# fileOrganizer
 
 This is an exercise that allowed me to write a script to help me sort files within a folder.

**STEP 1**

I started by creating, in a notebook, a Python script that would iterate alphabetically over the files in the "**files**" folder and, depending on the type (audio, document, image), move them to the relevant subfolder. If the subfolder does not exist, the script automatically creates it.
During the cycle, the script prints the information about the files: name, type and size in bytes. 


In addition to printing out the information as I move files around, I need to keep track of the files by creating a "**recap.csv**" (called "Resoconto.csv" in my code) document with the same information. 
The final structure of the files folder should be:

- files            
   - audio
      - song1.mp3
      - song2.mp3
    - docs
      - ciao.txt
      - pippo.odt
    - images
      - bw.png
      - daffodil.jpg
      - eclipse.png
      - trump.jpeg    
     - recap.csv

**STEP 2**

I put the script I created into a small executable (called **addfile.py**).
The purpose of the executable is to move a *single* file (located in the files folder) to the appropriate subfolder, updating the recap.

The executable's interface has as its only argument the name of the file to be moved (including format, e.g. 'trump.jpeg'). If the file passed as an argument does not exist, the interface must communicate this to the user.


**STEP 3**

I have added to the Step 1 notebook a script that iterates over the *images* subfolder and builds a summary table.
In addition to the file name, the table shows:

- image height, in pixels
- image width, in pixels
- If the image is greyscale, the *grayscale* column indicates the average of the values of the one colour level.
- if the image is in colour, the other columns indicate the average of the values of each colour level.
