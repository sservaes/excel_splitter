import pandas as pd
import os
import tkinter
from tkinter import filedialog
from sys import exit

directory = "/home/cypher/Desktop/IDIF/"

# root = tkinter.Tk()
# root.withdraw
# root.directory = filedialog.askdirectory()
#
# if root.directory == ():
#     print("\nPlease choose a directory first.")
#     print("Closing program.")
#     exit()
#
# directory = root.directory + "/"

print("\n" + "Working in " + directory + "\n")

if os.path.isdir(directory + "Individuals") == False:
    print("No 'Individuals' folder exists...")
    os.mkdir(directory + "Individuals")
    print("So a folder 'Individuals' has been created in " + directory + "." + "\n")

d = {}
for filename in os.listdir(directory):
    if os.path.isdir(directory + filename) == True:
        continue
    if filename.startswith("s") == False:
        continue
    filename, file_extension = os.path.splitext(filename)
    print("File found: " + filename + file_extension)
    df = pd.read_csv(directory + filename + file_extension, header=0, sep='\t')
    split = filename.split("_")

    if len(df.columns) == 5:
        newfile1 = df.columns[3] + "_" + split[0] + "_" + split[2] + "_" + split[3] + "_" + split[4]
        d[df.columns[3]] = df.loc[0:len(df), ("start[seconds]", "end[kBq/cc]", df.columns[3])]
        df1 = d[df.columns[3]]
        df1.to_csv((directory + "Individuals/" + newfile1 + '.crv'), sep="\t", index=False)
        print(newfile1 + " has been generated in the 'Individuals' folder.")

    newfile2 = df.columns[2] + "_" + split[0] + "_" + split[2] + "_" + split[3] + "_" + split[4]
    d[df.columns[2]] = df.loc[0:len(df), ("start[seconds]", "end[kBq/cc]", df.columns[2])]
    df2 = d[df.columns[2]]
    df2.to_csv((directory + "Individuals/" + newfile2 +'.crv'), sep="\t", index=False)
    print(newfile2 + " has been generated in the 'Individuals' folder.")