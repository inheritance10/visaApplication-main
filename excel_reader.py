import pandas as pd


# Excel dosyasından veriyi oku

def read_excel(file):
    dataframe = pd.read_excel(file)
    data = dataframe.to_dict(orient='records')
    return data

