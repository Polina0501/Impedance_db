import os
from datetime import datetime
from tkinter.filedialog import askdirectory
from connection import Session, Material, Experiment, Measure
from processing_dir import find_material, open_file

fold = askdirectory()
with Session() as session:
    for dir_name, dir_list, file_list in os.walk(fold):
        if not dir_list:
            dir_base_name = os.path.basename(dir_name)
            dict_mat = find_material(dir_base_name)
            material = Material(**dict_mat)
            session.add(material)
            session.flush()
            file_list_z = [e for e in file_list if e.endswith('.z')]

            for i, file_name in enumerate(file_list_z):
                path = os.path.join(dir_name, file_name)
                current_time = os.path.getmtime(path)
                creation_datetime = datetime.fromtimestamp(current_time)
                formatted_creation_time = creation_datetime.strftime('%H:%M:%S')
                experiment = Experiment(
                    material_id=material.id,
                    experiment_num=i + 1,
                    experiment_time=formatted_creation_time
                )
                session.add(experiment)

                session.flush()

                file = open_file(path)
                list_measure = []

                for index in file.index:
                    string_measure = Measure(
                        experiment_id=experiment.id,
                        re=float(file['Re, Ом'][index]),
                        im=float(file['Im, Ом'][index]),
                        f=float(file['Частота, Гц'][index]),
                        point_num=index + 1
                    )
                    list_measure.append(string_measure)

                session.add_all(list_measure)

    session.commit()
