import pandas as pd

def crearOnniRunLink(csv_file, archivo_salida):
    df = pd.read_csv(csv_file)
    df = df[df['input'].str.lower() != 'input']
    df_sin_repetidos = df.drop_duplicates(subset='input', keep='first')
    df_sin_repetidos[['input']].to_csv(archivo_salida, index=False)

    print(f"Archivo {csv_file} procesado y guardado como {archivo_salida}")