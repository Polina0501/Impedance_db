import pandas as pd

def find_material(dir_name: str):
    list_dir_name = dir_name.split('_')
    dict_name = {
        'date_exp': list_dir_name[0],
        'electrolyte_percentage_2': int(list_dir_name[2]),
        'electrolyte_material_2': list_dir_name[3],
        'electrolyte_percentage_1': 100 - int(list_dir_name[2]),
        'electrolyte_material_1': list_dir_name[1],
        'electrolyte_thickness': float(list_dir_name[4]),

        'electrode_percentage_2': int(list_dir_name[6]),
        'electrode_material_2': list_dir_name[7],
        'electrode_percentage_1': 100 - int(list_dir_name[6]),
        'electrode_material_1': list_dir_name[5],
        'electrode_starch_percentage': float(list_dir_name[8]),
        'electrode_thickness': float(list_dir_name[9])
    }
    return dict_name

def open_file(path: str) -> pd.DataFrame:
    file = pd.read_csv(path, sep=' ' * 14,
                       names=['Частота, Гц', 'Re, Ом', 'Im, Ом'], engine='python') #encoding = 'windows-1251')
    return file

# if __name__ == '__main__':
#     s = askdirectory()
#     dir_name = os.path.basename(s)
#     # path = os.walk(s)
#     # i, f, g = path
#     print(dir_name)
#     print(find_material(dir_name))

