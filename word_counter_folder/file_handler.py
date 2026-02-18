import csv
class csv_file:
    def __init__(self,path_to_csv):
        self.path_to_csv=path_to_csv
        self.sync()
    def sync(self):
        try:
            with open(self.path_to_csv, mode="r") as file:
                reader=csv.DictReader(file)
                self.headers=[]
                self.headers=reader.fieldnames
                self.rows=[]
                self.rows=list(reader)
        except FileNotFoundError:
            print(f"Error: {self.path_to_csv} dose not exist")
        except Exception as e:
            print(f"An error occurred: {e}")
    def __getitem__(self,index):
        return self.rows[index]
    def __str__(self):
        output=""
        for row in self.rows:
            line=",".join([f"{k}:{v}"for k,v in row.items()])
            output+=line+"\n"
        return output
    def return_list_of_dict(self):
        return self.rows
    def add(self,content):
        if len(content)!=len(self.headers):
            raise IndexError(f"len(content)({len(content)})!=len(hedder)({len(self.headers)})")
        try:
            with open(self.path_to_csv,mode="a",newline='\n') as file:
                writer=csv.writer(file)
                writer.writerow(content)
        except FileNotFoundError:
            print(f"Error: {self.path_to_csv} dose not exist")
        except Exception as e:
            print(f"An error occurred: {e}")
        self.sync()
    def __len__(self):
        return len(self.headers)
    def __delitem__(self,line):
        arow=[]
        with open(self.path_to_csv,"r") as source:
            arow=list(csv.reader(source))
        if 0<=line<len(self.rows):
            del arow[line+1]
            try:
                with open(self.path_to_csv,"w",newline='\n') as file:
                    writer=csv.writer(file)
                    writer.writerows(arow)
            except FileNotFoundError:
                print(f"Error: {self.path_to_csv} dose not exist")
            except Exception as e:
                print(f"An error occurred: {e}")
            self.sync()

class txt_file:
    def __init__(self,path_to_txt):
        self.path_to_txt=path_to_txt
        self.sync()
    def sync(self):
        try:
            with open(self.path_to_txt,'r') as file:
                self.content=file.read()
        except FileNotFoundError:
            print(f"Error: {self.path_to_txt} dose not exist")
        except Exception as e:
            print(f"An error occurred: {e}")
    def __str__(self):
        self.sync()
        return self.content
    def __len__(self):
        self.sync()
        return len(self.content.split())