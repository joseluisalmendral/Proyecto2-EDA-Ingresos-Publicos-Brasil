import os
import unicodedata
import pandas as pd

# Definir una función para comprobar que las columnas son iguales
def columnas_son_iguales(file_list):
    """
    Verifica si todas las columnas en los archivos CSV de una lista son iguales.

    Parámetros:
    ----------
    file_list : list
        Lista de rutas de archivos CSV que serán comparados.

    Retorna:
    --------
    bool :
        Retorna `True` si todos los archivos tienen las mismas columnas,
        de lo contrario, retorna `False` y muestra un mensaje de error
        indicando cuál archivo tiene columnas diferentes.
    """

    columnas_ref = pd.read_csv(file_list[0], delimiter=';', encoding='latin-1').columns

    print('hola')

    for file in file_list[1:]:
        columnas_actuales = pd.read_csv(file, delimiter=';', encoding='latin-1').columns
        if not columnas_ref.equals(columnas_actuales):
            print(f"Error: Las columnas no coinciden en el archivo {file}")
            return False
    return True



# Función para combinar los archivos
def combinar_csvs(file_list):
    """
    Combina varios archivos CSV en un solo DataFrame si todos tienen las mismas columnas.

    Parámetros:
    ----------
    file_list : list
        Lista de rutas de archivos CSV que serán combinados.

    Retorna:
    --------
    pd.DataFrame or None:
        Un DataFrame combinado de los archivos si las columnas coinciden. 
        Si no coinciden o hay un error al leer los archivos, retorna `None`.
    """

    #, encoding='latin1'

    try:
        print('hola')
        columnas_ref = pd.read_csv(file_list[0], sep=';').columns

        for file in file_list[1:]:
            columnas_actuales = pd.read_csv(file, sep=';').columns
            if not columnas_ref.equals(columnas_actuales):
                print(f"Error: Las columnas no coinciden en el archivo {file}")
                return False
        return True

    except UnicodeDecodeError as e:
        print(f"Error de codificación en el archivo {file}: {e}")
        return False


# Obtener lista de archivos.
def obtener_lista_archivos_csv(ruta, comienzo_nombre):
    """
    Obtiene una lista de todos los archivos CSV en una ruta especificada.

    Parámetros:
    ----------
    ruta : str
        Ruta al directorio donde se buscarán los archivos CSV.

    comienzo_nombre: str
        Comienzo del nombre de los archivos.

    Retorna:
    --------
    list or None :
        Una lista de rutas de archivos CSV. Si ocurre un error al obtener la lista,
        retorna `None` y muestra un mensaje de error.
    """

    try:
        archivos = [os.path.join(ruta, f) for f in os.listdir(ruta) if ((f.endswith('.csv')) and (f.startswith(comienzo_nombre)))]
        return [os.path.join(ruta, f) for f in archivos if f.endswith('.csv')]
    except:
        print('Hubo un error al obtener la lista de archvivos csv')
        return None


#Exportar nuevo archivo con el nombre que le digamos y a la ruta que le digamos
def exportar_nuevo_csv(df,ruta, nuevo_nombre):
    df.to_csv(f'{ruta}/{nuevo_nombre}.csv', index=False)



import re

def limpiar_lista_palabras(lista_palabras):
    """
    Elimina acentos y caracteres especiales de una lista de palabras y las convierte a minúsculas.
    Reemplaza espacios con guiones bajos.

    Parámetros:
    ----------
    lista_palabras : list
        Lista de palabras que serán limpiadas.

    Retorna:
    --------
    list :
        Lista de palabras limpiadas, sin acentos, en minúsculas, y sin caracteres especiales.
    """
    def eliminar_acentos(palabra):
        # Normalizar la palabra para separar caracteres acentuados
        palabra_sin_acentos = ''.join(c for c in unicodedata.normalize('NFKD', palabra) if unicodedata.category(c) != 'Mn')
        # Eliminar caracteres que no sean letras o números
        palabra_limpia = re.sub(r'[^a-zA-Z0-9]', ' ', palabra_sin_acentos)
        # Convertir a minúsculas, eliminar espacios extra, y reemplazar espacios por guiones bajos
        return palabra_limpia.lower().replace(" ", "_").strip()

    # Aplicar la función de limpieza a cada palabra de la lista
    return [eliminar_acentos(palabra) for palabra in lista_palabras]



def ver_filas_con_nulos(df):
    return df[df.isnull().any(axis=1)] 



def mostrar_porcentaje_nulos(df):
    """
    Muestra un DataFrame con el porcentaje de valores nulos por columna, ordenado de mayor a menor.

    Parámetros:
    ----------
    df : DataFrame
        El DataFrame en el cual se calcularán los porcentajes de valores nulos.

    Retorna:
    --------
    DataFrame :
        Un DataFrame con el nombre de las columnas y su porcentaje de valores nulos, ordenado de mayor a menor.
    """
    porcentaje_nulos = df.isnull().mean() * 100
    
    df_nulos = porcentaje_nulos.reset_index()
    
    df_nulos.columns = ['Columna', 'Porcentaje Nulos']
    
    df_nulos_ordenado = df_nulos.sort_values(by='Porcentaje Nulos', ascending=False)
    
    return df_nulos_ordenado



def describe(df):
    resultado = df.describe()
    mediana = df.median()
    resultado.loc['median'] = mediana

    return resultado