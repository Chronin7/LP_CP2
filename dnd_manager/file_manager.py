#use later
class FileManager:
    def __init__(self,file_name,starting_data):
        self.file_name=file_name
        with open(self.file_name, "w") as f:
            f.write(starting_data)
            return f
    def read(self,file,pointer):
        file.seek(pointer)
        return file.read()
    def write(self,data, file):
        file.write(data)
    def remove_data(self)
            