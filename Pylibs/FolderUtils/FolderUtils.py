import os
import shutil


def log(x, y = None):
   """  Logs whatever you put in X to the console

        Logs whatever you put in X to the console, as
        long as Y is None. Mostly used inside the library
   """
   if y == None:
    print(x)
   

def WriteToFile(x: str, y: str, z: str) -> str:
    """Writes x to y file using z method
    
      A simple function that writes whatever string you put
      as the first parameter, to a file with the name in the 2nd
      parameter. You can also put an absolute path here.
      Either 'W'riting or 'A'ppending in the 3rd parameter.
    """
    txt_file_path = y
    with open(txt_file_path, z) as file:
      file.write(x)

def CreateDirectory(x: str, y = None):
    """Creates a directory at 'x' absolute path
    
       Simply creates a new folder at the absolute path 'X'
       Throws an error if there's already a folder there.
       Put anything into 'y' to stop logging all actions
    """
    if not os.path.exists(x):
      os.mkdir(x)
      log('folder created', y)
    else:
       print("Error, Directory already exists.")

def RemoveDirectory(x: str, y = "e", z = None):
    """Removes directory X
   
      Put whether the directory is 'e'mpty or has 's'ubfolders
      in 'y'. Will throw an error if there are subfolders and you
      leave 'y' empty or enter 'e'. Enter anything into Z to stop
      logging all actions
    """
    try:
        if y == 'e':
                os.rmdir(x)
                log("Empty folder removed", z)
        elif y == 's':
            shutil.rmtree(x)
            log("folder and subtrees removed", z)
        else:
            print("Invalid parameter")
    except:
        print("Invalid directory")

def GetFilesInDir(x: str, y = None) -> list:
    """ Gets all the filenames in directory 'x'

        Returns all the filenames in a list.
        Logs all of the filenames as long as you leave 'y'
        empty
    """
    files = os.listdir(x)
    log(files, y)
    return files

def GetAllFilesInDir(x = None, y = None) -> list:
    if x == None:
        cwd = os.getcwd()
    else:
        cwd = x
    
    folders = []

    topLayer = os.listdir(cwd)
    log(topLayer, y)

    for file in topLayer:
        i = 0
        if file.__contains__('.') or file == "LICENSE":
            pass
        else:
            folders.insert(0, file)
        i += 1
    
    print(folders)

    for i in folders:
        try:
            nextlayer = os.listdir(f"{cwd}/{i}")
            log(f"{i},")
            log(nextlayer, y)
        except:
            print(f"no file access to folder {cwd}/{i}")