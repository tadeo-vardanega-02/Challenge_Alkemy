import requests as req
from os import path
from os import remove
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


#Eliminar un archivo si ya existe un archivo con el mismo nombre
if path.exists('/Users/Usuario/Desktop/Proyecto Alkemy/museos-2022-enero-museos-23-01-2022.csv'):
    remove('/Users/Usuario/Desktop/Proyecto Alkemy/museos-2022-enero-museos-23-01-2022.csv') 

if path.exists('/Users/Usuario/Desktop/Proyecto Alkemy/cines-2022-enero-cines-23-01-2022.csv'):
    remove('/Users/Usuario/Desktop/Proyecto Alkemy/cines-2022-enero-cines-23-01-2022.csv')

if path.exists('/Users/Usuario/Desktop/Proyecto Alkemy/bibliotecas-2022-enero-bibliotecas-23-01-2022.csv'):
    remove('/Users/Usuario/Desktop/Proyecto Alkemy/bibliotecas-2022-enero-bibliotecas-23-01-2022.csv')



#Descargo el archivo csv de los museos
url_museo = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv'

archivo_museo_csv = 'museos-2022-enero-museos-23-01-2022.csv'

data = req.get(url_museo)

with open(archivo_museo_csv, 'wb')as file:
    file.write(data.content)



#Descargo el archivo csv de los cines

url_cine = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'

archivo_cine_csv = 'cines-2022-enero-cines-23-01-2022.csv'

data = req.get(url_cine)

with open(archivo_cine_csv, 'wb')as file:
    file.write(data.content)



#Descargo el archivo csv de las bibliotecas populares

url_biblioteca = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'

archivo_biblioteca_csv = 'bibliotecas-2022-enero-bibliotecas-23-01-2022.csv'

data = req.get(url_biblioteca)

with open(archivo_biblioteca_csv, 'wb')as file:
    file.write(data.content)



#Procesamiento de datos

#Traigo la informacion de los .csv para poder crear un solo DataFrame con toda la informacion

cines_df = pd.read_csv(r'C:\Users\Usuario\Desktop\Proyecto Alkemy\cines-2022-enero-cines-23-01-2022.csv')

museos_df = pd.read_csv(r'C:\Users\Usuario\Desktop\Proyecto Alkemy\museos-2022-enero-museos-23-01-2022.csv')

bibliotecas_df = pd.read_csv(r'C:\Users\Usuario\Desktop\Proyecto Alkemy\bibliotecas-2022-enero-bibliotecas-23-01-2022.csv')




#Informacion de museos, cines y blibliotecas normalizada en una sola tabla

#Elimino las columnas que no me sirven de cada dataframe

cines_df_filtrado = cines_df.drop([
    'Información adicional' ,'Observaciones', 'Piso', 'Latitud', 'Longitud',
    'TipoLatitudLongitud', 'Fuente', 'tipo_gestion', 'Pantallas', 'Butacas', 
    'espacio_INCAA', 'año_actualizacion'], axis = 1) 

cines_df_filtrado2 = cines_df_filtrado.rename(columns={
    'Categoría':'categoria', 
    'Provincia': 'provincia'})


museos_df_filtrado = museos_df.drop([
    'Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud', 
    'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 
    'año_inauguracion', 'IDSInCA'], axis = 1)

museos_df_filtrado2 = museos_df_filtrado.rename(columns={
    'Categoría':'categoria', 
    'localidad': 'Departamento', 
    'nombre': 'Nombre', 
    'direccion': 'Dirección', 
    'telefono': 'Teléfono'})

bibliotecas_df_filtrado = bibliotecas_df.drop([
    'Información adicional', 'Subcategoria', 'Observacion', 'Piso', 
    'Cod_tel', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 
    'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis = 1)

bibliotecas_df_filtrado2 = bibliotecas_df_filtrado.rename(columns={
    'Categoría':'categoria', 
    'Provincia': 'provincia', 
    'Domicilio': 'Dirección'})

todos_los_datos_df = pd.concat([
    cines_df_filtrado2, 
    museos_df_filtrado2, 
    bibliotecas_df_filtrado2], axis=0)


todos_los_datos_df.reset_index(drop=True, inplace=True)

print(todos_los_datos_df)

#Nueva tabla (cantidad de registros totales por categoria, por fuente y por provincia y categoria)

cines_df_filtrado3 = cines_df.drop([
    'Información adicional' ,'Observaciones', 'Piso', 'Latitud', 
    'Longitud','TipoLatitudLongitud', 'tipo_gestion', 'Pantallas', 
    'Butacas', 'espacio_INCAA', 'año_actualizacion'], axis = 1)

cines_df_filtrado4= cines_df_filtrado3.rename(columns={
    'Categoría':'categoria', 
    'Provincia': 'provincia'})



museos_df_filtrado3 =  museos_df.drop([
    'Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 
    'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 
    'año_inauguracion', 'IDSInCA'], axis = 1)



museos_df_filtrado4 = museos_df_filtrado3.rename(columns={
    'Categoría':'categoria', 'localidad': 'Departamento', 'nombre': 'Nombre', 
    'direccion': 'Dirección', 'telefono': 'Teléfono', 'fuente': 'Fuente'})




bibliotecas_df_filtrado3 = bibliotecas_df.drop([
    'Información adicional', 'Subcategoria', 'Observacion', 'Piso', 
    'Cod_tel', 'Latitud', 'Longitud', 'TipoLatitudLongitud',
    'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis = 1)

bibliotecas_df_filtrado4= bibliotecas_df_filtrado3.rename(columns={
    'Categoría':'categoria', 
    'Provincia': 'provincia',
    'Domicilio': 'Dirección'})



todos_los_datos_df2 = pd.concat([cines_df_filtrado4, museos_df_filtrado4, bibliotecas_df_filtrado4], axis=0)
todos_los_datos_df2.reset_index(drop=True, inplace=True)



todos_los_datos_df3 = todos_los_datos_df2.drop([
    'Cod_Loc', 'Nombre', 'IdProvincia', 'IdDepartamento', 
    'Departamento', 'Localidad', 'Dirección', 'CP', 
    'cod_area', 'Teléfono', 'Mail', 'Web'], axis = 1)
todos_los_datos_df3.reset_index(drop=True, inplace=True)



todos_los_datos_group_by = todos_los_datos_df3.groupby(['provincia', 'categoria'])[['Fuente']].count()

print(todos_los_datos_group_by)



#tabla de los cines (Provincia, cantidad de pantallas, de butacas, de espacios INCAA)

cines_df_filtrado3 = cines_df.drop([
    'Categoría', 'Teléfono', 'Fuente', 'Web', 'Mail', 'cod_area', 'CP', 'Dirección', 
    'Nombre', 'Localidad', 'Departamento', 'IdDepartamento', 'IdProvincia', 'Cod_Loc', 
    'Información adicional' ,'Observaciones', 'Piso', 'Latitud', 'Longitud',
    'TipoLatitudLongitud', 'tipo_gestion', 'año_actualizacion'], axis = 1)

cines_df_filtrado3.reset_index(drop=True, inplace=True)

cines_df_filtrado5 = cines_df_filtrado3.fillna('No')

cines_df_filtrado5.reset_index(drop=True, inplace=True)

cines_df_filtrado5['espacio_INCAA'] = cines_df_filtrado5['espacio_INCAA'].map({'Si': 1})

cines_df_filtrado6 = cines_df_filtrado5.fillna(1)


cines_group_by = cines_df_filtrado6.groupby(['Provincia'])[['Pantallas','Butacas', 'espacio_INCAA']].sum()

cines_group_by2= cines_group_by.rename(columns={
    'Pantallas':'Cantidad de pantallas', 
    'Butacas': 'Cantidad de butacas', 
    'espacio_INCAA':'Cantidad de espacios INCAA'})

print(cines_group_by2)



#Base de datos PostgreSQL

#Creamos las bases de datos

engine1 = create_engine("postgresql://postgres:admin@localhost:5432/db_alkemy")

#Informacion obtenida del request
cines_df.to_sql(
    "Cines_df", 
    con=engine1, 
    if_exists="replace")

museos_df.to_sql(
    "Museos_df", 
    con=engine1, 
    if_exists="replace")

bibliotecas_df.to_sql(
    "Bibliotecas_df", 
    con=engine1, 
    if_exists="replace")


#Tabla que contiene toda la informacion normalizada 
todos_los_datos_df.to_sql(
    "Todos_los_datos", 
    con=engine1, 
    if_exists="replace")

#Tabla que contiene cantidad de registros totales por categoria, por fuente y por provincia y categoria
todos_los_datos_group_by.to_sql(
    "Cantidad de registros totales por categoria", 
    con=engine1, if_exists="replace")

#Tabla de los cines (Provincia, cantidad de pantallas, de butacas, de espacios INCAA)

cines_db = cines_group_by2.to_sql(
    "Cantidad de pantallas, de butacas, de espacios INCAA", 
    con=engine1, 
    if_exists="replace")














