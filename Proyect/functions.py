import pandas as pd
from unidecode import unidecode
from connection import *


# Clean empty characters
def clean_empty_characters(dataframe, column):
    dataframe[column] = dataframe[column].replace('NINGUNO', 'NULL')
    dataframe[column] = dataframe[column].replace('NO SABE', 'NULL')
    dataframe[column] = dataframe[column].replace('NINGUNO', 'NULL')
    dataframe[column] = dataframe[column].replace('NO APLICA', 'NULL')
    dataframe[column] = dataframe[column].replace('nan', 'NULL')
    dataframe[column] = dataframe[column].replace('', 'NULL')
    dataframe[column].fillna('NULL', inplace=True)
    return dataframe


# Clean Ñ or ñ
def clean_special_characters_enie_and_upper(dataframe, column):
    dataframe[column] = dataframe[column].str.upper()
    dataframe[column] = dataframe[column].str.replace('[Ñ]', 'N', regex=True)
    return dataframe

#Clean Special Characters in Dataset
def clean_accents(dataframe, column):
    dataframe[column] = dataframe[column].astype(str).apply(lambda x: unidecode(x))
    return dataframe

#Clean Special Characters in Dataset
def clean_special_characters_letters(dataframe, column):
    dataframe[column] = dataframe[column].str.replace('[^a-zA-Z ]', '', regex=True)
    return dataframe

#Clean Special Characters in Dataset
def clean_special_characters_letters_numbers(dataframe, column):
    dataframe[column] = dataframe[column].str.replace('[^a-zA-Z0-9. ]', '', regex=True)
    return dataframe


#Clean dates in dataset
def clean_date_format_mmddyyyy(dataframe, column):
    #----Wrong dates----
    dataframe[column] = dataframe[column].str[:10]
    dataframe['Substring'] = dataframe[column].str.slice(6, 10)
    dataframe.loc[dataframe['Substring'].astype(int)<= 1920, 'FECHA_NACIMIENTO'] = '01/01/1900'
    del dataframe['Substring']
    #---Convert dates---
    dataframe[column] = pd.to_datetime(dataframe[column])
    dataframe[column] = dataframe[column].dt.strftime('%d/%m/%Y')
    return dataframe

#Clean letters or other in numbers
def clean_special_numbers(dataframe, column):
    dataframe[column]= dataframe[column].astype(str)
    dataframe[column] = dataframe[column].str.replace('[^0-9.]', '', regex=True)
    return dataframe

#Clean dataset
def clean_dataset(data):
    header = ['TIPO_DOCUMENTO',
            'NACIONALIDAD',
            'GENERO',
            'FECHA_NACIMIENTO',
            'PERIODO',
            'ID_CONSECUTIVO',
            'ESTUDIANTE',
            'TIENE_ETNIA',	
            'PAIS_RESIDENCIA',
            'ETNIA',
            'DEPTO_RESIDE',
            'COD_RESIDE_DEPTO',
            'MUNICIPIO_RESIDE',
            'COD_MUNICIPIO_RESIDE',
            'ESTRATO_VIVIENDA',
            'PERSONAS_HOGAR',
            'CUARTOS_HOGAR',
            'EDUCACION_PADRE',
            'EDUCACION_MADRE',
            'TRABAJO_PADRE',
            'TRABAJO_MADRE',
            'TIENE_SERVICIOINTERNET',	
            'TIENE_SERVICIOTV',
            'TIENE_COMPUTADOR',
            'TIENE_LAVADORA',
            'TIENE_HORNOMICROHONDAS',
            'TIENE_AUTOMOVIL',
            'TIENE_MOTOCICLETA',
            'TIENE_CONSOLAVIDEOJUEGOS',
            'TIENE_NUMLIBROS',
            'COME_LECHEDERIVADOS',
            'COME_COMECARNEPESCADOHUEVO',
            'COME_CEREALFRUTOSLEGUMBRE',
            'SITUACION_ECONOMICA_ULT_ANIO',
            'DEDICACION_LECTURADIARIA',
            'DEDICACION_INTERNET',
            'HORAS_SEMANATRABAJA',
            'TIPO_REMUNERACION',
            'COLEGIO_CODIGO_ICFES',
            'COLEGIO_COD_DANE_ESTABLECIMIENTO',
            'COLEGIO_NOMBRE_ESTABLECIMIENTO',
            'COLEGIO_GENERO',
            'COLEGIO_NATURALEZA',
            'COLEGIO_CALENDARIO',
            'COLEGIO_BILINGUE',
            'COLEGIO_CARACTER',
            'COLEGIO_COD_DANE_SEDE',
            'COLEGIO_NOMBRE_SEDE',
            'COLEGIO_SEDE_PRINCIPAL',
            'COLEGIO_AREA_UBICACION',
            'COLEGIO_JORNADA',
            'COLEGIO_COD_MUNICIPIO_UBICACION',
            'COLEGIO_MUNICIPIO_UBICACION',
            'COLEGIO_COD_DEPARTAMENTO_UBICACION',
            'COLEGIO_DEPARTAMENTO_UBICACION',
            'PRIVADO_LIBERTAD',
            'COD_MUNICIPIO_PRESENTACION',
            'MUNICIPIO_PRESENTACION',
            'DEPARTAMENTO_PRESENTACION',
            'COD_DEPARTAMENTO_PRESENTACION',
            'PUNT_LECTURA_CRITICA',
            'PERCENTIL_LECTURA_CRITICA',
            'DESEMP_LECTURA_CRITICA',
            'PUNT_MATEMATICAS',
            'PERCENTIL_MATEMATICAS',
            'DESEMP_MATEMATICAS',
            'PUNT_CIENCIAS_NATURALES',
            'PERCENTIL_CIENCIAS_NATURALES',
            'DESEMP_CIENCIAS_NATURALES',
            'PUNT_SOCIALES_CIUDADANAS',
            'PERCENTIL_SOCIALES_CIUDADANAS',
            'DESEMP_SOCIALES_CIUDADANAS',
            'PUNT_INGLES',
            'PERCENTIL_INGLES',
            'DESEMP_INGLES',
            'PUNT_GLOBAL',
            'PERCENTIL_GLOBAL',
            'INSE_INDIVIDUAL',
            'NSE_INDIVIDUAL',
            'NSE_ESTABLECIMIENTO',
            'ESTADO_INVESTIGACION',
            'GENERACION-E'
    ]
    #Change the header of dataframe
    data.columns = header

    #-----------------------NACIONALIDAD---------------------------------#
    data = clean_special_characters_enie_and_upper(data, 'NACIONALIDAD')
    data = clean_accents(data, 'NACIONALIDAD')
    data = clean_special_characters_letters(data, 'NACIONALIDAD')
    data = clean_empty_characters(data, 'NACIONALIDAD')

    #-----------------------GENERO---------------------------------#
    data = clean_empty_characters(data, 'GENERO')
    data = clean_special_characters_enie_and_upper(data, 'GENERO')
    data = clean_special_characters_letters(data, 'GENERO')
    data = clean_empty_characters(data, 'GENERO')

    #-----------------------FECHA_NACIMIENTO---------------------------------#
    data = clean_date_format_mmddyyyy(data, 'FECHA_NACIMIENTO')

    #-----------------------PERIODO---------------------------------#
    data = clean_special_numbers(data, 'PERIODO')
    data = clean_empty_characters(data, 'PERIODO')

    #------------------------ID_CONSECUTIVO------------------
    data = clean_special_characters_letters_numbers(data, 'ID_CONSECUTIVO')
    data = clean_empty_characters(data, 'ID_CONSECUTIVO')

    #--------------------------TIENE_ETNIA-------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_ETNIA')
    data = clean_empty_characters(data, 'TIENE_ETNIA')

    #--------------------------PAIS_RESIDENCIA------------------
    data = clean_special_characters_enie_and_upper(data, 'PAIS_RESIDENCIA')
    data = clean_accents(data, 'PAIS_RESIDENCIA')
    data = clean_special_characters_letters(data, 'PAIS_RESIDENCIA')
    data = clean_empty_characters(data, 'PAIS_RESIDENCIA')

    #--------------------------ETNIA----------------------------
    data = clean_special_characters_enie_and_upper(data, 'ETNIA')
    data = clean_accents(data, 'ETNIA')
    data = clean_special_characters_letters(data, 'ETNIA')
    data = clean_empty_characters(data, 'ETNIA')

    #-----------------------DEPTO_RESIDE--------------------------------#
    data = clean_special_characters_enie_and_upper(data, 'DEPTO_RESIDE')
    data = clean_accents(data, 'DEPTO_RESIDE')
    data = clean_special_characters_letters(data, 'DEPTO_RESIDE')
    data = clean_empty_characters(data, 'DEPTO_RESIDE')

    #-----------------------COD_RESIDE_DEPTO---------------------------------#
    data = clean_special_numbers(data, 'COD_RESIDE_DEPTO')
    data = clean_empty_characters(data, 'COD_RESIDE_DEPTO')

    #-----------------------MUNICIPIO_RESIDE--------------------------------#
    data = clean_special_characters_enie_and_upper(data, 'MUNICIPIO_RESIDE')
    data = clean_accents(data, 'MUNICIPIO_RESIDE')
    data = clean_special_characters_letters(data, 'MUNICIPIO_RESIDE')
    data = clean_empty_characters(data, 'MUNICIPIO_RESIDE')

    #-----------------------COD_MUNICIPIO_RESIDE---------------------------------#
    data = clean_special_numbers(data, 'COD_MUNICIPIO_RESIDE')
    data = clean_empty_characters(data, 'COD_MUNICIPIO_RESIDE')

    #-------------------------ESTRATO_VIVIENDA-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'ESTRATO_VIVIENDA')
    data = clean_special_numbers(data, 'ESTRATO_VIVIENDA')
    data = clean_empty_characters(data, 'ESTRATO_VIVIENDA')

    #-------------------------PERSONAS_HOGAR-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'PERSONAS_HOGAR')
    data = clean_accents(data, 'PERSONAS_HOGAR')
    data = clean_special_characters_letters_numbers(data, 'PERSONAS_HOGAR')
    data = clean_empty_characters(data, 'PERSONAS_HOGAR')

    #-------------------------CUARTOS_HOGAR-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'CUARTOS_HOGAR')
    data = clean_accents(data, 'CUARTOS_HOGAR')
    data = clean_special_characters_letters_numbers(data, 'CUARTOS_HOGAR')
    data = clean_empty_characters(data, 'CUARTOS_HOGAR')

    #-------------------------EDUCACION_PADRE-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'EDUCACION_PADRE')
    data = clean_accents(data, 'EDUCACION_PADRE')
    data = clean_special_characters_letters(data, 'EDUCACION_PADRE')
    data = clean_empty_characters(data, 'EDUCACION_PADRE')

    #-------------------------EDUCACION_MADRE-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'EDUCACION_MADRE')
    data = clean_accents(data, 'EDUCACION_MADRE')
    data = clean_special_characters_letters(data, 'EDUCACION_MADRE')
    data = clean_empty_characters(data, 'EDUCACION_MADRE')

    #-------------------------TRABAJO_PADRE-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TRABAJO_PADRE')
    data = clean_accents(data, 'TRABAJO_PADRE')
    data = clean_special_characters_letters(data, 'TRABAJO_PADRE')
    data = clean_empty_characters(data, 'TRABAJO_PADRE')

    #-------------------------TRABAJO_MADRE-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TRABAJO_MADRE')
    data = clean_accents(data, 'TRABAJO_MADRE')
    data = clean_special_characters_letters(data, 'TRABAJO_MADRE')
    data = clean_empty_characters(data, 'TRABAJO_MADRE')

    #-------------------------TIENE_SERVICIOINTERNET-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_SERVICIOINTERNET')
    data = clean_accents(data, 'TIENE_SERVICIOINTERNET')
    data = clean_special_characters_letters(data, 'TIENE_SERVICIOINTERNET')
    data = clean_empty_characters(data, 'TIENE_SERVICIOINTERNET')

    #-------------------------TIENE_SERVICIOINTERNET-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_SERVICIOTV')
    data = clean_accents(data, 'TIENE_SERVICIOTV')
    data = clean_special_characters_letters(data, 'TIENE_SERVICIOTV')
    data = clean_empty_characters(data, 'TIENE_SERVICIOTV')

    #-------------------------TIENE_COMPUTADOR-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_COMPUTADOR')
    data = clean_accents(data, 'TIENE_COMPUTADOR')
    data = clean_special_characters_letters(data, 'TIENE_COMPUTADOR')
    data = clean_empty_characters(data, 'TIENE_COMPUTADOR')

    #-------------------------TIENE_COMPUTADOR-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_LAVADORA')
    data = clean_accents(data, 'TIENE_LAVADORA')
    data = clean_special_characters_letters(data, 'TIENE_LAVADORA')
    data = clean_empty_characters(data, 'TIENE_LAVADORA')

    #-------------------------TIENE_HORNOMICROHONDAS-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_HORNOMICROHONDAS')
    data = clean_accents(data, 'TIENE_HORNOMICROHONDAS')
    data = clean_special_characters_letters(data, 'TIENE_HORNOMICROHONDAS')
    data = clean_empty_characters(data, 'TIENE_HORNOMICROHONDAS')

    #-------------------------TIENE_AUTOMOVIL-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_AUTOMOVIL')
    data = clean_accents(data, 'TIENE_AUTOMOVIL')
    data = clean_special_characters_letters(data, 'TIENE_AUTOMOVIL')
    data = clean_empty_characters(data, 'TIENE_AUTOMOVIL')

    #-------------------------TIENE_MOTOCICLETA-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_MOTOCICLETA')
    data = clean_accents(data, 'TIENE_MOTOCICLETA')
    data = clean_special_characters_letters(data, 'TIENE_MOTOCICLETA')
    data = clean_empty_characters(data, 'TIENE_MOTOCICLETA')

    #-------------------------TIENE_CONSOLAVIDEOJUEGOS-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_CONSOLAVIDEOJUEGOS')
    data = clean_accents(data, 'TIENE_CONSOLAVIDEOJUEGOS')
    data = clean_special_characters_letters(data, 'TIENE_CONSOLAVIDEOJUEGOS')
    data = clean_empty_characters(data, 'TIENE_CONSOLAVIDEOJUEGOS')

    #-------------------------TIENE_NUMLIBROS-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIENE_NUMLIBROS')
    data = clean_accents(data, 'TIENE_NUMLIBROS')
    data = clean_special_characters_letters_numbers(data, 'TIENE_NUMLIBROS')
    data = clean_empty_characters(data, 'TIENE_NUMLIBROS')

    #-------------------------COME_LECHEDERIVADOS-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COME_LECHEDERIVADOS')
    data = clean_accents(data, 'COME_LECHEDERIVADOS')
    data = clean_special_characters_letters_numbers(data, 'COME_LECHEDERIVADOS')
    data = clean_empty_characters(data, 'COME_LECHEDERIVADOS')

    #-------------------------COME_LECHEDERIVADOS-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COME_COMECARNEPESCADOHUEVO')
    data = clean_accents(data, 'COME_COMECARNEPESCADOHUEVO')
    data = clean_special_characters_letters_numbers(data, 'COME_COMECARNEPESCADOHUEVO')
    data = clean_empty_characters(data, 'COME_COMECARNEPESCADOHUEVO')

    #-------------------------COME_CEREALFRUTOSLEGUMBRE-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COME_CEREALFRUTOSLEGUMBRE')
    data = clean_accents(data, 'COME_CEREALFRUTOSLEGUMBRE')
    data = clean_special_characters_letters_numbers(data, 'COME_CEREALFRUTOSLEGUMBRE')
    data = clean_empty_characters(data, 'COME_CEREALFRUTOSLEGUMBRE')

    #-------------------------SITUACION_ECONOMICA_ULT_ANIO-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'SITUACION_ECONOMICA_ULT_ANIO')
    data = clean_accents(data, 'SITUACION_ECONOMICA_ULT_ANIO')
    data = clean_special_characters_letters(data, 'SITUACION_ECONOMICA_ULT_ANIO')
    data = clean_empty_characters(data, 'SITUACION_ECONOMICA_ULT_ANIO')

    #-------------------------DEDICACION_LECTURADIARIA-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'DEDICACION_LECTURADIARIA')
    data = clean_accents(data, 'DEDICACION_LECTURADIARIA')
    data = clean_special_characters_letters_numbers(data, 'DEDICACION_LECTURADIARIA')
    data = clean_empty_characters(data, 'DEDICACION_LECTURADIARIA')

    #-------------------------DEDICACION_INTERNET-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'DEDICACION_INTERNET')
    data = clean_accents(data, 'DEDICACION_INTERNET')
    data = clean_special_characters_letters_numbers(data, 'DEDICACION_INTERNET')
    data = clean_empty_characters(data, 'DEDICACION_INTERNET')

    #-------------------------HORAS_SEMANATRABAJA-----------------------------------
    data = clean_special_characters_enie_and_upper(data, 'HORAS_SEMANATRABAJA')
    data = clean_accents(data, 'HORAS_SEMANATRABAJA')
    data = clean_special_characters_letters_numbers(data, 'HORAS_SEMANATRABAJA')
    data = clean_empty_characters(data, 'HORAS_SEMANATRABAJA')

    #-------------------------TIPO_REMUNERACION--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'TIPO_REMUNERACION')
    data = clean_accents(data, 'TIPO_REMUNERACION')
    data = clean_special_characters_letters_numbers(data, 'TIPO_REMUNERACION')
    data = clean_empty_characters(data, 'TIPO_REMUNERACION')

    #-------------------------COLEGIO_CODIGO_ICFES--------------------------------------
    data = clean_special_numbers(data, 'COLEGIO_CODIGO_ICFES')
    data = clean_empty_characters(data, 'COLEGIO_CODIGO_ICFES')

    #-------------------------COLEGIO_COD_DANE_ESTABLECIMIENTO--------------------------------------
    data = clean_special_numbers(data, 'COLEGIO_COD_DANE_ESTABLECIMIENTO')
    data = clean_empty_characters(data, 'COLEGIO_COD_DANE_ESTABLECIMIENTO')


    #-------------------------COLEGIO_NOMBRE_ESTABLECIMIENTO--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_NOMBRE_ESTABLECIMIENTO')
    data = clean_accents(data, 'COLEGIO_NOMBRE_ESTABLECIMIENTO')
    data = clean_special_characters_letters_numbers(data, 'COLEGIO_NOMBRE_ESTABLECIMIENTO')
    data = clean_empty_characters(data, 'COLEGIO_NOMBRE_ESTABLECIMIENTO')

    #-------------------------COLEGIO_GENERO--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_GENERO')
    data = clean_accents(data, 'COLEGIO_GENERO')
    data = clean_special_characters_letters(data, 'COLEGIO_GENERO')
    data = clean_empty_characters(data, 'COLEGIO_GENERO')

    #-------------------------COLEGIO_CALENDARIO--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_NATURALEZA')
    data = clean_accents(data, 'COLEGIO_NATURALEZA')
    data = clean_special_characters_letters(data, 'COLEGIO_NATURALEZA')
    data = clean_empty_characters(data, 'COLEGIO_NATURALEZA')

    #-------------------------COLEGIO_CALENDARIO--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_CALENDARIO')
    data = clean_accents(data, 'COLEGIO_CALENDARIO')
    data = clean_special_characters_letters(data, 'COLEGIO_CALENDARIO')
    data = clean_empty_characters(data, 'COLEGIO_CALENDARIO')

    #-------------------------COLEGIO_BILINGUE--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_BILINGUE')
    data = clean_accents(data, 'COLEGIO_BILINGUE')
    data = clean_special_characters_letters(data, 'COLEGIO_BILINGUE')
    data = clean_empty_characters(data, 'COLEGIO_BILINGUE')

    #-------------------------COLEGIO_CARACTER--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_CARACTER')
    data = clean_accents(data, 'COLEGIO_CARACTER')
    data = clean_special_characters_letters(data, 'COLEGIO_CARACTER')
    data = clean_empty_characters(data, 'COLEGIO_CARACTER')

    #-------------------------COLEGIO_COD_DANE_SEDE--------------------------------------
    data = clean_special_numbers(data, 'COLEGIO_COD_DANE_SEDE')
    data = clean_empty_characters(data, 'COLEGIO_COD_DANE_SEDE')

    #-------------------------COLEGIO_NOMBRE_SEDE--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_NOMBRE_SEDE')
    data = clean_accents(data, 'COLEGIO_NOMBRE_SEDE')
    data = clean_special_characters_letters_numbers(data, 'COLEGIO_NOMBRE_SEDE')
    data = clean_empty_characters(data, 'COLEGIO_NOMBRE_SEDE')

    #-------------------------COLEGIO_SEDE_PRINCIPAL--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_SEDE_PRINCIPAL')
    data = clean_accents(data, 'COLEGIO_SEDE_PRINCIPAL')
    data = clean_special_characters_letters(data, 'COLEGIO_SEDE_PRINCIPAL')
    data = clean_empty_characters(data, 'COLEGIO_SEDE_PRINCIPAL')

    #-------------------------COLEGIO_AREA_UBICACION--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_AREA_UBICACION')
    data = clean_accents(data, 'COLEGIO_AREA_UBICACION')
    data = clean_special_characters_letters(data, 'COLEGIO_AREA_UBICACION')
    data = clean_empty_characters(data, 'COLEGIO_AREA_UBICACION')

    #-------------------------COLEGIO_JORNADA--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_JORNADA')
    data = clean_accents(data, 'COLEGIO_JORNADA')
    data = clean_special_characters_letters(data, 'COLEGIO_JORNADA')
    data = clean_empty_characters(data, 'COLEGIO_JORNADA')

    #-------------------------COLEGIO_COD_MUNICIPIO_UBICACION--------------------------------------
    data = clean_special_numbers(data, 'COLEGIO_COD_MUNICIPIO_UBICACION')
    data = clean_empty_characters(data, 'COLEGIO_COD_MUNICIPIO_UBICACION')

    #-------------------------COLEGIO_MUNICIPIO_UBICACION--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_MUNICIPIO_UBICACION')
    data = clean_accents(data, 'COLEGIO_MUNICIPIO_UBICACION')
    data = clean_special_characters_letters(data, 'COLEGIO_MUNICIPIO_UBICACION')
    data = clean_empty_characters(data, 'COLEGIO_MUNICIPIO_UBICACION')

    #-------------------------COLEGIO_COD_DEPARTAMENTO_UBICACION--------------------------------------
    data = clean_special_numbers(data, 'COLEGIO_COD_DEPARTAMENTO_UBICACION')
    data = clean_empty_characters(data, 'COLEGIO_COD_DEPARTAMENTO_UBICACION')

    #-------------------------COLEGIO_DEPARTAMENTO_UBICACION--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'COLEGIO_DEPARTAMENTO_UBICACION')
    data = clean_accents(data, 'COLEGIO_DEPARTAMENTO_UBICACION')
    data = clean_special_characters_letters(data, 'COLEGIO_DEPARTAMENTO_UBICACION')
    data = clean_empty_characters(data, 'COLEGIO_DEPARTAMENTO_UBICACION')

    #-------------------------PRIVADO_LIBERTAD--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'PRIVADO_LIBERTAD')
    data = clean_accents(data, 'PRIVADO_LIBERTAD')
    data = clean_special_characters_letters(data, 'PRIVADO_LIBERTAD')
    data = clean_empty_characters(data, 'PRIVADO_LIBERTAD')

    #-------------------------COD_MUNICIPIO_PRESENTACION--------------------------------------
    data = clean_special_numbers(data, 'COD_MUNICIPIO_PRESENTACION')
    data = clean_empty_characters(data, 'COD_MUNICIPIO_PRESENTACION')

    #-------------------------MUNICIPIO_PRESENTACION--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'MUNICIPIO_PRESENTACION')
    data = clean_accents(data, 'MUNICIPIO_PRESENTACION')
    data = clean_special_characters_letters(data, 'MUNICIPIO_PRESENTACION')
    data = clean_empty_characters(data, 'MUNICIPIO_PRESENTACION')

    #-------------------------DEPARTAMENTO_PRESENTACION--------------------------------------
    data = clean_special_characters_enie_and_upper(data, 'DEPARTAMENTO_PRESENTACION')
    data = clean_accents(data, 'DEPARTAMENTO_PRESENTACION')
    data = clean_special_characters_letters(data, 'DEPARTAMENTO_PRESENTACION')
    data = clean_empty_characters(data, 'DEPARTAMENTO_PRESENTACION')

    #-------------------------COD_MUNICIPIO_PRESENTACION--------------------------------------
    data = clean_special_numbers(data, 'COD_DEPARTAMENTO_PRESENTACION')
    data = clean_empty_characters(data, 'COD_DEPARTAMENTO_PRESENTACION')

    #-------------------------PUNT_LECTURA_CRITICA--------------------------------------
    data = clean_special_numbers(data, 'PUNT_LECTURA_CRITICA')
    data = clean_empty_characters(data, 'PUNT_LECTURA_CRITICA')

    #-------------------------PERCENTIL_LECTURA_CRITICA--------------------------------------
    data = clean_special_numbers(data, 'PERCENTIL_LECTURA_CRITICA')
    data = clean_empty_characters(data, 'PERCENTIL_LECTURA_CRITICA')

    #-------------------------DESEMP_LECTURA_CRITICA--------------------------------------
    data = clean_special_numbers(data, 'DESEMP_LECTURA_CRITICA')
    data = clean_empty_characters(data, 'DESEMP_LECTURA_CRITICA')

    #-------------------------PUNT_MATEMATICAS--------------------------------------
    data = clean_special_numbers(data, 'PUNT_MATEMATICAS')
    data = clean_empty_characters(data, 'PUNT_MATEMATICAS')

    #-------------------------PERCENTIL_MATEMATICAS--------------------------------------
    data = clean_special_numbers(data, 'PERCENTIL_MATEMATICAS')
    data = clean_empty_characters(data, 'PERCENTIL_MATEMATICAS')

    #-------------------------DESEMP_MATEMATICAS--------------------------------------
    data = clean_special_numbers(data, 'DESEMP_MATEMATICAS')
    data = clean_empty_characters(data, 'DESEMP_MATEMATICAS')

    #-------------------------PUNT_CIENCIAS_NATURALES--------------------------------------
    data = clean_special_numbers(data, 'PUNT_CIENCIAS_NATURALES')
    data = clean_empty_characters(data, 'PUNT_CIENCIAS_NATURALES')

    #-------------------------PERCENTIL_CIENCIAS_NATURALES--------------------------------------
    data = clean_special_numbers(data, 'PERCENTIL_CIENCIAS_NATURALES')
    data = clean_empty_characters(data, 'PERCENTIL_CIENCIAS_NATURALES')

    #-------------------------DESEMP_CIENCIAS_NATURALES--------------------------------------
    data = clean_special_numbers(data, 'DESEMP_CIENCIAS_NATURALES')
    data = clean_empty_characters(data, 'DESEMP_CIENCIAS_NATURALES')

    #-------------------------PUNT_SOCIALES_CIUDADANAS--------------------------------------
    data = clean_special_numbers(data, 'PUNT_SOCIALES_CIUDADANAS')
    data = clean_empty_characters(data, 'PUNT_SOCIALES_CIUDADANAS')

    #-------------------------PERCENTIL_SOCIALES_CIUDADANAS--------------------------------------
    data = clean_special_numbers(data, 'PERCENTIL_SOCIALES_CIUDADANAS')
    data = clean_empty_characters(data, 'PERCENTIL_SOCIALES_CIUDADANAS')

    #-------------------------DESEMP_SOCIALES_CIUDADANAS--------------------------------------
    data = clean_special_numbers(data, 'DESEMP_SOCIALES_CIUDADANAS')
    data = clean_empty_characters(data, 'DESEMP_SOCIALES_CIUDADANAS')

    #-------------------------PUNT_INGLES--------------------------------------
    data = clean_special_numbers(data, 'PUNT_INGLES')
    data = clean_empty_characters(data, 'PUNT_INGLES')

    #-------------------------PERCENTIL_INGLES--------------------------------------
    data = clean_special_numbers(data, 'PERCENTIL_INGLES')
    data = clean_empty_characters(data, 'PERCENTIL_INGLES')

    #-------------------------DESEMP_INGLES--------------------------------------
    data = clean_empty_characters(data, 'DESEMP_INGLES')
    #Clean data except +, -, letters
    data['DESEMP_INGLES'] = data['DESEMP_INGLES'].str.replace('[^ a-zA-Z0-9+-]', '', regex=True) 

    #-------------------------PUNT_GLOBAL--------------------------------------
    data = clean_special_numbers(data, 'PUNT_GLOBAL')
    data = clean_empty_characters(data, 'PUNT_GLOBAL')

    #-------------------------PERCENTIL_GLOBAL--------------------------------------
    data = clean_special_numbers(data, 'PERCENTIL_GLOBAL')
    data = clean_empty_characters(data, 'PERCENTIL_GLOBAL')

    #-------------------------INSE_INDIVIDUAL--------------------------------------
    data = clean_special_numbers(data, 'INSE_INDIVIDUAL')
    data = clean_empty_characters(data, 'INSE_INDIVIDUAL')

    #-------------------------NSE_INDIVIDUAL--------------------------------------
    data = clean_special_numbers(data, 'NSE_INDIVIDUAL')
    data = clean_empty_characters(data, 'NSE_INDIVIDUAL')

    #-------------------------NSE_ESTABLECIMIENTO'--------------------------------------
    data = clean_special_numbers(data, 'NSE_ESTABLECIMIENTO')
    data = clean_empty_characters(data, 'NSE_ESTABLECIMIENTO')

    #-------------------------ESTADO_INVESTIGACION---------------------
    data = clean_special_characters_enie_and_upper(data, 'ESTADO_INVESTIGACION')
    data = clean_accents(data, 'ESTADO_INVESTIGACION')
    data = clean_special_characters_letters(data, 'ESTADO_INVESTIGACION')
    data = clean_empty_characters(data, 'ESTADO_INVESTIGACION')

    #-------------------------GENERACION-E---------------------
    data = clean_special_characters_enie_and_upper(data, 'GENERACION-E')
    data = clean_accents(data, 'GENERACION-E')
    data = clean_special_characters_letters(data, 'GENERACION-E')
    data = clean_empty_characters(data, 'GENERACION-E')
    
    #-----------------------------RETURN DATASET----------------------
    return data


#Create dataframes
def create_dataframes_to_tables(dataframe):

    #create dataframe to tbl estudiantes
    df_estudiante = dataframe.loc[:,['ID_CONSECUTIVO',
                                      'FECHA_NACIMIENTO',
                                      'TIENE_ETNIA',
                                      'ETNIA',
                                      'DEDICACION_LECTURADIARIA',
                                      'COLEGIO_COD_DANE_ESTABLECIMIENTO',
                                      'GENERO',
                                      'NACIONALIDAD',
                                      'TIENE_NUMLIBROS',
                                      'DEDICACION_INTERNET',
                                      'HORAS_SEMANATRABAJA']
                                    ]
    #Drop duplicates
    df_estudiante = df_estudiante.drop_duplicates()
    connection_mysql_to_tbl(df_estudiante, 'estudiante')

    #create dataframe to tbl puntaje
    df_puntaje = dataframe.loc[:,['ID_CONSECUTIVO',
                                  'PUNT_GLOBAL',
                                  'PUNT_LECTURA_CRITICA',
                                  'PUNT_MATEMATICAS',
                                  'PUNT_CIENCIAS_NATURALES',
                                  'PUNT_SOCIALES_CIUDADANAS',
                                  'PUNT_INGLES',
                                  'DESEMP_INGLES']
                                ]
    #Drop duplicates
    df_puntaje = df_puntaje.drop_duplicates()
    connection_mysql_to_tbl(df_puntaje, 'puntaje')

    #create dataframe to residencia estudiante
    df_residencia_estudiante = dataframe.loc[:,['ID_CONSECUTIVO',
                                                'COD_RESIDE_DEPTO',
                                                'DEPTO_RESIDE',
                                                'COD_MUNICIPIO_RESIDE',
                                                'MUNICIPIO_RESIDE',
                                                'PAIS_RESIDENCIA',
                                                'ESTRATO_VIVIENDA',
                                                'PERSONAS_HOGAR',
                                                'CUARTOS_HOGAR']
                                            ]
    #Drop duplicates
    df_residencia_estudiante = df_residencia_estudiante.drop_duplicates()
    connection_mysql_to_tbl(df_residencia_estudiante, 'residencia_estudiante')

    #create dataframe to tecnologia_hogar
    df_tecnologia_hogar = dataframe.loc[:,['ID_CONSECUTIVO',
                                           'TIENE_SERVICIOINTERNET',
                                           'TIENE_COMPUTADOR',
                                           'TIENE_CONSOLAVIDEOJUEGOS']
                                        ]
    #Drop duplicates
    df_tecnologia_hogar = df_tecnologia_hogar.drop_duplicates()
    connection_mysql_to_tbl(df_tecnologia_hogar, 'tecnologia_hogar')

    #create dataframe to tecnologia_hogar
    df_colegio = dataframe.loc[:,['COLEGIO_COD_DANE_ESTABLECIMIENTO', 
                                  'COLEGIO_NOMBRE_ESTABLECIMIENTO',
                                  'COLEGIO_BILINGUE',
                                  'COLEGIO_NATURALEZA',
                                  'COLEGIO_CARACTER',
                                  'COLEGIO_COD_DEPARTAMENTO_UBICACION',
                                  'COLEGIO_DEPARTAMENTO_UBICACION',
                                  'COLEGIO_COD_MUNICIPIO_UBICACION',
                                  'COLEGIO_MUNICIPIO_UBICACION']
                                ]
    #Drop duplicates
    df_colegio = df_colegio.drop_duplicates()
    connection_mysql_to_tbl(df_colegio, 'colegio')