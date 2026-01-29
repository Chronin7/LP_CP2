import utill_functions
import importlib.util
import os
import sys
module_names=[]
imported_modules = {}
def import_files(folder_path):
    global module_names
    global imported_modules
    sys.path.insert(0,folder_path)
    for filename in os.listdir(folder_path):
        if filename[-3:]==".py" and filename !="shocase.py" and filename != "utill_functions.py":
            module_name=filename[:-3]
            module_names.append(filename[:-3])
            try:
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(folder_path, filename))
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                imported_modules[module_name] = module
            except Exception as e:
                if filename!="utill_functions":
                    print(f"Error importing {filename}: {e}")
                else:
                    pass
    sys.path.pop(0)
    return imported_modules, module_names
mods,names=import_files('indifidual_projects')
while True:
    prompt="0 to quit\n"
    for x,y in enumerate(names):
        prompt=prompt+f"{x+1} for {y.replace("_"," ")}\n"
    user_input=utill_functions.get_valid_type(int,prompt)
    if user_input==0:
        print("goodbye")
        break
    mods[names[user_input-1]].main()