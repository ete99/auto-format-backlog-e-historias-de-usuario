# read an excel that has this columns:

# |Funcionalidades|Descripción|Beneficio|Esfuerzo|Usuario|Observaciones|Necesidad|Propósito|Cómo Probar|Cómo Validar|

# the template for the md list should be like this:
template = """#### 4.{index} Historia de Usuario {index}: {funcionalidad}
YO COMO {yo_como}.
NECESITO {necesito}.
PARA {para}.
CRITERIOS DE ACEPTACION
- COMO PROBAR: {como_probar}.
- COMO VALIDAR: {como_validar}. 

"""

# Path: main.py

import pandas as pd


def read_excel():
    print("reading")
    # Read the excel file, set the column names
    df = pd.read_excel(
        "data.xlsx",
        names=[
            "Funcionalidades",
            "Descripción",
            "Beneficio",
            "Esfuerzo",
            "Usuario",
            "Observaciones",
            "Necesidad",
            "Propósito",
            "Cómo Probar",
            "Cómo Validar",
        ],
    )
    return df


def create_md(df):

    # Create a list to store the md
    md_list = ""

    # Iterate over the dataframe
    for index, row in df.iterrows():
        # Get the values from the row
        funcionalidad = row["Funcionalidades"]
        yo_como = row["Usuario"]
        necesito = row["Necesidad"]
        para = row["Propósito"]
        como_probar = row["Cómo Probar"]
        como_validar = row["Cómo Validar"]

        # Create the md string
        md = template.format(
            index=index + 1,
            funcionalidad=funcionalidad,
            yo_como=yo_como,
            necesito=necesito,
            para=para,
            como_probar=como_probar,
            como_validar=como_validar,
        )

        # Append the md string to the file
        md_list += md

    return md_list


def write_md(md_list):
    # Write the md to a file
    print("printing")
    with open("output.md", "w") as f:
        f.write(md_list)


def main():
    # Read the excel file

    df = read_excel()

    # Create the md
    md_list = create_md(df)

    # Write the md to a file
    write_md(md_list)


if __name__ == "__main__":
    main()
