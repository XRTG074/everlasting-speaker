import os

import pandas as pd

def load_data(data_purpose) -> pd.DataFrame:
    """
        Loads data into pandas DataFrame

        :param data_purpose: Main purpose of data (train/val/test)

        :return: Loaded data
        :rtype: DataFrame
    """
    data = pd.read_csv(f"../data/{data_purpose}.csv")

    return data

def merge_with_texts(data, data_purpose) -> pd.DataFrame:
    """
        Loads data into pandas DataFrame

        :param data: Main DataFrame
        :param data_purpose: Main purpose of data (train/val/test)

        :return: Data merged with texts
        :rtype: DataFrame
    """
    file_names = [file for file in os.listdir(f"../data/{data_purpose}") if os.path.isfile(f"../data/{data_purpose}/{file}")]
    files = []

    for file_name in file_names:
        with open(f"../data/{data_purpose}/{file_name}", "r", encoding="utf-8") as file:
            files.append(file.read())

    texts_data = pd.DataFrame({
        "id": file_names,
        "text": files
    })

    texts_data["id"] = texts_data["id"].str[:-4]

    data = data.merge(texts_data, on="id", how="left")

    return data

def prepare_data(data_purpose) -> pd.DataFrame:
    """
        Loads data and megres it with texts

        :param data_purpose: Main purpose of data (train/val/test)

        :return: Loaded data merged with texts
        :rtype: DataFrame 
    """
    data = load_data(data_purpose)
    data = merge_with_texts(data, data_purpose)

    return data