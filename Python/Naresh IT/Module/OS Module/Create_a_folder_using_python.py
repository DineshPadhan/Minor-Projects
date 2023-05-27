import os
try:
    # os.mkdir("Dinesh")
    # os.mkdir("C:\\Dinesh\\Python")                  # Creating folder in a location
    # os.makedirs("python\\Padhan")                   # Creating folder hierarchy
    # os.rmdir("Dinesh")                              # Removing Folder
    # os.removedirs("python")                         # Removing Folder hierarchy
    # os.remove("C:\\Dinesh\\Python.data")            # Removing file name
    # os.rename("Dinesh","Dinesh_Padhan")             # Rename file/folder name
    # os.rename("Dinesh","Dinesh_Padhan")             # Removing file name
    filelist = os.listdir("../../")                 # Removing file name
    print(filelist)
    print("Folder Create successfully")
except FileExistsError:
    print("Folder Already Exist.")