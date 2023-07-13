import os
import shutil

from_dir="C:/Users/LENOVO/Downloads"
to_dir="C:/Users/LENOVO/Desktop/PRO"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for x in list_of_files:
    name,extension = os.path.splitext(x)
    print(extension)
    if extension == "":
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir+"/"+x
        path2 = to_dir+"/"+"Document_files"
        path3 = to_dir+"/"+"Document_files"+"/"+x

        if os.path.exists(path2):
            print("Moving"+x)
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving"+x)
            shutil.move(path1,path3)
        