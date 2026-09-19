import os 
filename = input("Enter the filename to open: ")
if os.path.exists(filename):
    with open(filename, "r") as file:
        contents = file.read()
        print("File Contents:")
        print(contents)
        
else:
    print("File not found . Please check the filesname.")