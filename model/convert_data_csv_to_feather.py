# %%
import feather
import pandas as pd

# %%


def convert_excel_to_feather(
        input_file: str, output_file: str, sheet_name: str, header: int, index_col=None) -> None:
    df = pd.read_excel(filepath=input_file,
                       sheet_name=sheet_name, header=header, index_col=index_col)
    df = df.astype(str)
    feather.write_dataframe(df, output_file)


def convert_csv_to_feather(input_file: str, output_file: str) -> None:
    df = pd.read_csv(input_file)
    feather.write_dataframe(df, output_file)


# %%
input_file = "../data/BIG_MART_SALES_PREDICTION.csv"
output_file = "../data/BIG_MART_SALES_PREDICTION.feather"
header = 0

convert_csv_to_feather(input_file, output_file)

# %%
df = pd.read_feather(output_file)

# %%
