#  pip install pandas && openpyxl

import pandas as pd

carros = {
    'marca':['Fiat', 'Crevolet', 'Ford', 'Hyndai'],
    'modelo':['Marea', 'Crevette', 'Escort', 'Creta'],
    'ano':['1999', '1978', '1995', '2023']
}

dataframe = pd.DataFrame(carros)
dataframe.to_excel('./carros.xlsx')