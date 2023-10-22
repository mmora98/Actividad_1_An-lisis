import pandas as pd
from functions import *

if __name__ == "__main__":

    # import data csv
    data = pd.read_csv('raw\Saber_11__2019-2_20231019.csv', low_memory=False)
    # clean dataset
    data = clean_dataset(data)
    # create datasets
    create_dataframes_to_tables(data)
    # send df to mysql
    create_dataframes_to_tables(data)


    # export data csv
    # data.to_csv('prestage\dataset_clean.csv', index=False)
    # print("Finalizado")