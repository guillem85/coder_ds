import pandas as pd
import os
from CODER_DS import DATA_DIR

FILE_NAME = os.path.join(DATA_DIR, 'processed/data.csv')

# cargamos el df
raw_csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw', 'raw.csv')
data = pd.read_csv(raw_csv_path, sep=';')

# generamos nuevo df solo con las columnas que queremos analizar
columns_keep = ['age', 'job', 'education', 'month', 'campaign', 'previous', 'poutcome', 'y']
data_2 = data[columns_keep]

# eliminamos los outliers de campañas
data_3 = data_2.loc[data_2['campaign'] <= 17]