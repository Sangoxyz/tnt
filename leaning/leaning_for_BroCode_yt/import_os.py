# import os
import os
import shutil
""" path = "D:\\leaning python\\leaning\\leaning_for_BroCode_yt\\test"


if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!") """

""" source = "test.txt"
destination = "C:\\Users\\sango\\OneDrive\\Máy tính\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+ " was moved")

except FileNotFoundError:
    print(source+ " was not found") """



path = "D:\\leaning python\\leaning\\leaning_for_BroCode_yt\\empty_folder"
#path = "D:\\leaning python\\leaning\\leaning_for_BroCode_yt\\test.txt"

try:

    #os.remove(path)
    os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")