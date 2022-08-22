# %%
import feather
import pandas as pd

# %%
df = pd.read_excel('./data/peruvian_enterprise_list.xlsx',
                   sheet_name='Sheet1', header=2, index_col=None)
df.head()

# %%
df.shape

# %%
# convert first column into integer
df['Unnamed: 0'] = df['Unnamed: 0'].astype(int)

# %%
# watch if there a duplicate value
df[df.duplicated() == True]


# %%
# convert list of columns from object to string
for column in [
    'RAZÓN SOCIAL', 'RUC/DNI', 'SECTOR ECONÓMICO', 'NOMBRE DE ENTIDAD OTORGANTE DEL CRÉDITO',
    'NOMBRE DE 2DA. ENTIDAD OTORGANTE DEL CRÉDITO*', 'MONTO PRÉSTAMO (S/)',
        'MONTO COBERTURADO (S/)', 'DEPARTAMENTO']:
    df[column] = df[column].astype(str)


# %%
df.to_feather('./peruvian_enterprise_list.feather')

# %%
feather.write_dataframe(df, './data/peruvian_enterprise_list.feather')

# %%
df = pd.read_feather('./data/peruvian_enterprise_list.feather')

# %%
df.tail()
