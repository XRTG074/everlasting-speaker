import pandas as pd

def create_clean_text(data) -> pd.DataFrame:
    """
        Creates a new feature 'clean_text' with texts free of markups

        :param data: Data with texts containing markups

        :return: Data with texts free of markups
        :rtype: DataFrame
    """
    data["clean_text"] = data["text"].str.replace(r"<(.*?)>", "", regex=True)

    return data