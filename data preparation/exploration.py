import pandas as pd

df = pd.read_csv("sales_06_FY2020-21.csv/sales_06_FY2020-21.csv")
print(df.head())
# les types de colonnes
print(df.info())
# d'apres cette ligne je vois que je dois regler les types des colonnes 

print(df.describe())
# d'apres cette ligne il y a un nombre de valeurs abberantes qui influencent sur la distribution de dataset

print(df.isnull().sum())
# d'apres cette ligne il y a pas des valeurs manquantes 

