from unidecode import unidecode
import pandas as pd

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


