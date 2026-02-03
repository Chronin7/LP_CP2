import utill_functions
import csv
def make_list():
    try:
        with open("Movies_list.csv",mode="r") as csv_file_demo:
            content=csv.reader(csv_file_demo)
            hedders = next(content)
            rows=[]
            for line in content:
                rows.append({hedders[0]:line[0], hedders[1]:line[1],hedders[2]:line[2],hedders[3]:line[3],hedders[4]:line[4],hedders[5]:line[5]})
    except FileNotFoundError:
        print("there is no file")
        return "0"
    except Exception as e:
        print(f'an error orrured: {e}')
        return "0"
    else:
        return rows
def main():
    list_of_movies=make_list()
    if list_of_movies=="0":
        return
    while True:
        user_input=utill_functions.get_valid_type(int,"yes")#work needed