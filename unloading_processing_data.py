import pandas as pd

from connection import Material, Session, engine

with Session() as session:
    materials = session.query(Material).all()
    list_materials = []
    for material in materials:
        for exp in material.experiments:
            n=False
            for meausure in exp.measures:
                if meausure.re < 0.5:
                    list_materials.append(material)
                    n=True
                    break
            if n:
                break

    df_dict = [dict_m.__dict__ for dict_m in list_materials]
    df = pd.DataFrame(df_dict)
    print(df)




# material_table = pd.read_sql_table('material', con=engine)
#
# query = "SELECT * FROM experiment WHERE material.electrolyte_thickness > 1"
# experiment_table = pd.read_sql_query(query, con=engine)

# print(material_table.info())