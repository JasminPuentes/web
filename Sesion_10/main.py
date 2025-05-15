#importar libreria pandas
import pandas as pd

#define la ruta del archivo csv que contiene los datos
#Si el archivo esta en el mismo directorio que el scrib solo se necesita el nombre del archivo
path = 'Online_Retail.csv'

#leer el archivo csv usando la funcion read_csv de pandas
#se especifica la codificacion latin-1 para manejar caracteres especiales
retail_data = pd.read_csv(path, encoding='latin-1')

#Muestra el tipo de la variable retail_datapara confirmar que es un dataframe de pandas
#Un dataframe es una estructura de datos bidimensional que se asemeja a una tabla
print(type(retail_data))

#imprime todo el contenido del dataframe
print(retail_data)
#imprimir todo el contenido data frame
print(retail_data)
