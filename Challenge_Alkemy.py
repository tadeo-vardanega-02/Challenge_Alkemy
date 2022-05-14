from os import path
from os import remove
import logging
from time import strftime
from decouple import config
import requests as req
import pandas as pd
import sqlalchemy

# Configuro los logs

logging.basicConfig(level=logging.DEBUG,
                    datefmt=strftime("%Y-%m-%d"),
                    format='%(asctime)s - %(name)s - %(message)s')

logger = logging.getLogger('Challenge Alkemy')

# Configuracion de las variables de entorno
PATH_MUSEO = config('PATH_MUSEO')
PATH_CINES = config('PATH_CINES')
PATH_BIBLIOTECAS = config('PATH_BIBLIOTECAS')
URL_MUSEO = config('URL_MUSEO')
ARCHIVO_MUSEO = config('ARCHIVO_MUSEO')
URL_CINES = config('URL_CINES')
ARCHIVO_CINES = config('ARCHIVO_CINES')
URL_BIBLIOTECAS = config('URL_BIBLIOTECAS')
ARCHIVO_BIBLIOTECAS = config('ARCHIVO_BIBLIOTECAS')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')
DB_TYPE = config('DB_TYPE')

# Variables de entorno
secret = f'{PATH_MUSEO}'
secret2 = f'{PATH_CINES}'
secret3 = f'{PATH_BIBLIOTECAS}'
url_museo = f'{URL_MUSEO}'
archivo_museo = f'{ARCHIVO_MUSEO}'
url_cines = f'{URL_CINES}'
archivo_cines = f'{ARCHIVO_CINES}'
url_bibliotecas = f'{URL_BIBLIOTECAS}'
archivo_bibliotecas = f'{ARCHIVO_BIBLIOTECAS}'
secret4 = f'{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Eliminar un archivo si ya existe un archivo con el mismo nombre

if path.exists(secret):
    remove(secret)

if path.exists(secret2):
    remove(secret2)

if path.exists(secret3):
    remove(secret3)

# Descargo el archivo csv de los museos

data = req.get(url_museo)

with open(archivo_museo, 'wb')as file:
    file.write(data.content)

# Descargo el archivo csv de los cines

data = req.get(url_cines)

with open(archivo_cines, 'wb')as file:
    file.write(data.content)

# Descargo el archivo csv de las bibliotecas populares

data = req.get(url_bibliotecas)

with open(archivo_bibliotecas, 'wb')as file:
    file.write(data.content)


# Procesamiento de datos

# Traigo la informacion de los .csv para poder crear un solo DataFrame con toda la informacion

museos_df = pd.read_csv(secret)

cines_df = pd.read_csv(secret2)

bibliotecas_df = pd.read_csv(secret3)


# Informacion de museos, cines y blibliotecas normalizada en una sola tabla

# Elimino las columnas que no me sirven de cada dataframe

cines_df_filtrado = cines_df.drop([
    'Información adicional', 'Observaciones', 'Piso', 'Latitud', 'Longitud',
    'TipoLatitudLongitud', 'Fuente', 'tipo_gestion', 'Pantallas', 'Butacas',
    'espacio_INCAA', 'año_actualizacion'], axis=1)

cines_df_filtrado2 = cines_df_filtrado.rename(columns={
    'Categoría': 'categoria',
    'Provincia': 'provincia'})


museos_df_filtrado = museos_df.drop([
    'Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud',
    'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion',
    'año_inauguracion'], axis=1)

museos_df_filtrado2 = museos_df_filtrado.rename(columns={
    'Categoría': 'categoria',
    'localidad': 'Departamento',
    'nombre': 'Nombre',
    'direccion': 'Dirección',
    'telefono': 'Teléfono'})

bibliotecas_df_filtrado = bibliotecas_df.drop([
    'Información adicional', 'Subcategoria', 'Observacion', 'Piso',
    'Cod_tel', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente',
    'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)

bibliotecas_df_filtrado2 = bibliotecas_df_filtrado.rename(columns={
    'Categoría': 'categoria',
    'Provincia': 'provincia',
    'Domicilio': 'Dirección'})

todos_los_datos_df = pd.concat([
    cines_df_filtrado2,
    museos_df_filtrado2,
    bibliotecas_df_filtrado2], axis=0)


todos_los_datos_df.reset_index(drop=True, inplace=True)

print(todos_los_datos_df)

# Nueva tabla (cantidad de registros totales por categoria, por fuente y por provincia y categoria)

cines_df_filtrado3 = cines_df.drop([
    'Información adicional', 'Observaciones', 'Piso', 'Latitud',
    'Longitud', 'TipoLatitudLongitud', 'tipo_gestion', 'Pantallas',
    'Butacas', 'espacio_INCAA', 'año_actualizacion'], axis=1)

cines_df_filtrado4 = cines_df_filtrado3.rename(columns={
    'Categoría': 'categoria',
    'Provincia': 'provincia'})


museos_df_filtrado3 = museos_df.drop([
    'Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud',
    'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion',
    'año_inauguracion'], axis=1)


museos_df_filtrado4 = museos_df_filtrado3.rename(columns={
    'Categoría': 'categoria', 'localidad': 'Departamento', 'nombre': 'Nombre',
    'direccion': 'Dirección', 'telefono': 'Teléfono', 'fuente': 'Fuente'})


bibliotecas_df_filtrado3 = bibliotecas_df.drop([
    'Información adicional', 'Subcategoria', 'Observacion', 'Piso',
    'Cod_tel', 'Latitud', 'Longitud', 'TipoLatitudLongitud',
    'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)


bibliotecas_df_filtrado4 = bibliotecas_df_filtrado3.rename(columns={
    'Categoría': 'categoria',
    'Provincia': 'provincia',
    'Domicilio': 'Dirección'})


todos_los_datos_df2 = pd.concat([cines_df_filtrado4, museos_df_filtrado4, bibliotecas_df_filtrado4], axis=0)
todos_los_datos_df2.reset_index(drop=True, inplace=True)


todos_los_datos_df3 = todos_los_datos_df2.drop([
    'Cod_Loc', 'Nombre', 'IdProvincia', 'IdDepartamento',
    'Departamento', 'Localidad', 'Dirección', 'CP',
    'cod_area', 'Teléfono', 'Mail', 'Web'], axis=1)
todos_los_datos_df3.reset_index(drop=True, inplace=True)


todos_los_datos_group_by = todos_los_datos_df3.groupby(['provincia', 'categoria'])[['Fuente']].count()

print(todos_los_datos_group_by)


# tabla de los cines (Provincia, cantidad de pantallas, de butacas, de espacios INCAA)

cines_df_filtrado3 = cines_df.drop([
    'Categoría', 'Teléfono', 'Fuente', 'Web', 'Mail', 'cod_area', 'CP', 'Dirección',
    'Nombre', 'Localidad', 'Departamento', 'IdDepartamento', 'IdProvincia', 'Cod_Loc',
    'Información adicional', 'Observaciones', 'Piso', 'Latitud', 'Longitud',
    'TipoLatitudLongitud', 'tipo_gestion', 'año_actualizacion'], axis=1)

cines_df_filtrado3.reset_index(drop=True, inplace=True)

cines_df_filtrado5 = cines_df_filtrado3.fillna('No')

cines_df_filtrado5.reset_index(drop=True, inplace=True)

cines_df_filtrado5['espacio_INCAA'] = cines_df_filtrado5['espacio_INCAA'].map({'Si': 1})

cines_df_filtrado6 = cines_df_filtrado5.fillna(1)


cines_group_by = cines_df_filtrado6.groupby(['Provincia'])[['Pantallas', 'Butacas', 'espacio_INCAA']].sum()


cines_group_by2 = cines_group_by.rename(columns={
    'Pantallas': 'Cantidad de pantallas',
    'Butacas': 'Cantidad de butacas',
    'espacio_INCAA': 'Cantidad de espacios INCAA'})

print(cines_group_by2)


# Base de datos PostgreSQL

engine1 = sqlalchemy.create_engine(secret4)

# Creamos las bases de datos

# Informacion obtenida del request
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


# Tabla que contiene toda la informacion normalizada
todos_los_datos_df.to_sql(
    "Todos_los_datos",
    con=engine1,
    if_exists="replace")

# Tabla que contiene cantidad de registros totales por categoria, por fuente y por provincia y categoria
todos_los_datos_group_by.to_sql(
    "Cantidad de registros totales por categoria",
    con=engine1, if_exists="replace")

# Tabla de los cines (Provincia, cantidad de pantallas, de butacas, de espacios INCAA)

cines_db = cines_group_by2.to_sql(
    "Cantidad de pantallas, de butacas, de espacios INCAA",
    con=engine1,
    if_exists="replace")
