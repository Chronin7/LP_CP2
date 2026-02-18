import file_handler
import time
import utill_functions
import os
def make_new_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            file.write(time.ctime())
        print(f"made new file, go to file {file_path} to edit")
        
def main():
    file_path=f"indifidual_projects/{utill_functions.get_valid_type(str,"what is the name of the filename for your text document (I recommend using your name or something you will remember): ").replace(" ","_").replace("\\","").removesuffix(".txt").lower()}.txt"
    make_new_file(file_path)
    document=file_handler.txt_file(file_path)
    last_counted=time.ctime()
    while True:
        choise=utill_functions.get_valid_type(int,f"last time words where counted: {last_counted}\n0 to return\n1 to change file\n2 to count words\n3 to see curent file\nWhat do you want: ",valid=(0,3))
        if choise==0:  
            return
        elif choise==1:
                file_path=f"indifidual_projects/{utill_functions.get_valid_type(str,"what is the name of the filename for your text document (I recommend using your name or something you will remember): ").replace(" ","_").replace("\\","").removesuffix(".txt").lower()}.txt"
                make_new_file(file_path)
                document=file_handler.txt_file(file_path)
        elif choise==2:
            print(f"the amount of words in your document is {len(document)}")
            last_counted=time.ctime()
        elif choise==3:
            print(document)
if __name__=="__main__":
    main()