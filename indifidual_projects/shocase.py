import financhal_caluclator
import password_gen
import personal_librarby
import utill_functions
import importlib
import os
import sys
module_names=[]
imported_modules = {}
def import_files(folder_path):
    global module_names
    global imported_modules
    sys.path.insert(0,folder_path)
    for filename in os.listdir(folder_path):
        if filename[-3:]==".py" and filename !="shocase.py":
            module_name=filename[:-3]
            module_names.append(filename[:-3])
            try:
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(folder_path, filename))
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                imported_modules[module_name] = module
                print(f"Imported module: {module_name}")
            except Exception as e:
                print(f"Error importing {filename}: {e}")
    sys.path.pop(0)
    return imported_modules, module_names
mods,names=import_files('indifidual_projects')
print(names)