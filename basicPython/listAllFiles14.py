import os
from pathlib import Path

path = "C:\\Users\\user\\Desktop\\CFP"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

