import pandas as pd

# convertir les types de colonnes  à de stypes corrects
df = pd.read_csv("sales_06_FY2020-21.csv")
print(df.dtypes)
print("4. Nombre de valeurs manquantes par colonne :\n", df.isna().sum())
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=False)
df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True)

# 2. Convertir en float (nombre décimal)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 3. Vérifier les types
print(df['price'].dtype)
# pour colonnees numeric 
numeric_cols = ['order_id','item_id', 'qty_ordered', 'value', 'discount_amount', 
                'total', 'cust_id', 'age', 'Discount_Percent']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


#pour colonnes string
int_cols = ['order_id','item_id', 'qty_ordered', 'cust_id', 'ref_num']
for col in int_cols:
    df[col] = df[col].astype('Int64')

cat_cols = ['status', 'category', 'payment_method', 'bi_st', 'Gender', 'Region',
            'month', 'Name Prefix']
for col in cat_cols:
    df[col] = df[col].astype('category')
string_cols = ['sku', 'full_name', 'E Mail', 'Customer Since', 'SSN','Phone No. ', 'User Name', 'First Name', 'Last Name', 'Middle Initial','City', 'State', 'County', 'Place Name']
for col in string_cols:
    df[col] = df[col].astype('string')
print(df.dtypes)
# supprimer les informations dupliques
# je supprimer la colonne place name car porte les memes infromations que city
df.drop(columns=["Place Name"], inplace=True)
# j'ai pas un information direct sur la colonne value total
df.drop(columns=["value","total"], inplace=True)

# je laisse l'un de id car porte le mmee information de commande 
df = df.drop_duplicates(subset=['order_id', 'item_id'], keep='first')
# je supprime les colonnes year et month car ce sinformations sont toujours dans le colonne order date
df.drop(columns=["year","month"], inplace=True)

# les valeurs negatives dans la colonne price , total et qty orderd
negative_checks = {
    'qty_ordered': (df['qty_ordered'] < 0).sum(),
    'price':       (df['price'] < 0).sum(),
    'discount_amount':(df['discount_amount'] < 0).sum()
}

print("Nombre de valeurs négatives par colonne :")
for col, count in negative_checks.items():
    print(f"{col:12} → {count:5} lignes négatives")

# save
df.to_csv("data preparation/cleaned_sales.csv", index=False)




