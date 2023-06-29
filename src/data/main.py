# -*- coding: utf-8 -*-
""" esto no es necesario porque nosotros ya tenemos la data en .csv, este archivo main.py de src.data es para
la obtencion de los datos, nosotros ya los tenemos, sería más bien para cuando recolectas datos de una api o fuente externa
hay un ejemplo en la clase 38
import pandas as pd

from ..config import DATA_DIR


if __name__ == '__main__':
    data = pd.read_csv('data/raw/raw.csv',sep=';')

    print(data.head())
"""

""" otra forma de resolverlo es crenado una ruta absoluta
import os
import pandas as pd

raw_csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw', 'raw.csv')
data = pd.read_csv(raw_csv_path, sep=';')

"""