#notes
#basic file reader
try:
    with open("notes/file_demo.txt","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    print()
file.close()



#basic file writer
try:
    with open("notes/file_demo.txt","w") as file:
        file.write("as you can see all of it is deleted and replaced with this")
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    print()
#show it changed
file.close()
try:
    with open("notes/file_demo.txt","r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    print()
try:
    #                               vvv w is for write r is for read a is for append x is fore creation and writing to a file
    with open("notes/file_demo.txt","a") as file:
        file.write("\nthis is added")
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    print()
#show it changed
file.close()
try:
    with open("notes/file_demo.txt","r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    print()

#how to make a new file if the file doesnt exest it just makes one for you


#r+

try:
    with open("notes/file_demo.txt","r+") as file:
        content=file.read()
        content+="\nthis is added via r+"
        file.write(content)
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    print()

#show it changed
file.close()
try:
    with open("notes/file_demo.txt","r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    print()

















#reading a csv
import csv
try:
    with open("notes/sample.csv",mode="r") as csv_file_demo:
        content=csv.reader(csv_file_demo)
        hedders = next(content)
        rows=[]
        for line in content:
            rows.append({hedders[0]:line[0], hedders[1]:line[1]})
except FileNotFoundError:
    print("there is no file")
except Exception as e:
    print(f'an error orrured: {e}')
else:
    for line in rows:
        print(line)
    



import os
#import csv


class FileManager:
    def __init__(self,file_name,file_type,folder_path):
        self.full_pathfull_path=os.path.join(folder_path,file_name)
        if os.path.exists(self.full_path):
            pass
        else:
            raise FileNotFoundError
        self.file_name=file_name
        self.folder_path=folder_path
        self.file_type=file_type
    def read(self):
        pass


#csv stuff
#import csv
#same methud as writing to a txt for a,w and r and r+ but a+ and w+
with open("notes/sample.csv","a",newline="")as csvfile:
    #                         this seperates each item
    writer=csv.writer(csvfile,delimiter=",")
    writer.writerow(["We are the nights who say","NI!"])
csvfile.close()
with open("notes/sample.csv","w",newline="")as csvfile:
    #                         this seperates each item
    
    pass
csvfile.close()
with open("notes/sample.csv","a",newline="")as csvfile:
    fieldnames=["username","color"]
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writerow({"username":"bob","color":"puse"})