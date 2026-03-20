import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    df.rename(columns={
        "Price_(Rs.)": "Price",
        "Final_Price(Rs.)": "Final_Price"
    }, inplace=True)

    df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"], dayfirst=True)

    df["Revenue"] = df["Final_Price"]
    return df
