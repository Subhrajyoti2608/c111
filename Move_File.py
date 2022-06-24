import os
import shutil

from_dir="C:/Users/subhr/OneDrive/Documents/Downloaded_Files/Document_Files"
to_dir="C:/Users/subhr/OneDrive/Documents/Downloaded_Files/Image_Files"

listOfFiles=os.listdir(from_dir)
print(listOfFiles)
for files in listOfFiles:
    name,ext=os.path.split(files)
    print(name)
    print(ext)