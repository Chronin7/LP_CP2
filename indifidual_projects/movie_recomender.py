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
#Title,Director,Genre,Rating,Length (min),Notable Actors
def main():
    list_of_movies=make_list()
    if list_of_movies=="0":
        return
    while True:
        user_input=utill_functions.get_valid_type(int,"1 to serch/get recomendations\n2 to print full movie list\n3 to quit\nwhat do you want: ")
        if user_input==1:
            while True:
                user_input=utill_functions.get_valid_type(int,"1 to serche via genre\n2 for director\n3 for Notable Actors\n4 for length (min/max)\n5 for title\n6 for rateing\n7 to return\nwhat do you want: ")
                if user_input==5:
                    break
                match user_input:
                    case 1:
                        type_of_serch="Genre"
                    case 2:
                        type_of_serch="Director"
                    case 3:
                        type_of_serch='Notable Actors'
                    case 4:
                        type_of_serch="Length (min)"
                    case 5:
                        type_of_serch="Title"
                    case 6:
                        type_of_serch="Rating"
                    case 7:
                        break
                    case _:
                        print("that is not valid")
                        type_of_serch=None
                if type_of_serch and not type_of_serch=="Length (min)" :
                    user_input=utill_functions.get_valid_type(str,f"what is the {type_of_serch} you are looking for: ").lower()
                    for dicts in list_of_movies:
                        if user_input in dicts[type_of_serch].lower():
                            for key,value in dicts.items():
                                print(f"{key}:{value}  ",end="")
                            print()
                elif type_of_serch=="Length (min)":
                    user_input=utill_functions.get_valid_type(int,"what is the length of the movie you want\n(negative numbers mean less than while positive numbers mean grater than): ")
                    if user_input<0:
                        for dicts in list_of_movies:
                            if abs(user_input)>dicts["Length (min)"]:
                                for key,value in dicts.items():
                                    print(f"{keys}:{value}",end="  ")
                                print()
        elif user_input==2:
            for dicts in list_of_movies:
                for key,value in dicts.items():
                    print(f"{key}:{value}  ",end="")
                print()
        elif user_input==3:
            return()
if __name__=="__main__":
    main() 
