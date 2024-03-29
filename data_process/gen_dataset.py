import pandas as pd

import pandas as pd
import os

# Leer el archivo CSV
df = pd.read_csv('tweets_politica_kaggle.csv', sep='\t')

# Crear una carpeta para cada partido y guardar los datos
for partido in df['partido'].unique():
    # Crear la carpeta si no existe
    carpeta_partido = os.path.join('partidos', partido)
    os.makedirs(carpeta_partido, exist_ok=True)
    
    # Filtrar los tweets del partido actual
    tweets_partido = df[df['partido'] == partido]
    
    # Guardar los tweets del partido en un archivo CSV
    tweets_partido.to_csv(os.path.join(carpeta_partido, f'{partido}_tweets.csv'), index=False)
    
    # Guardar los tweets del partido en un archivo de texto
    with open(os.path.join(carpeta_partido, f'orig_{partido}_tweets.txt'), 'w') as f:
        for tweet in tweets_partido['tweet']:
            f.write(tweet + '\n')
