import numpy as np
import pandas as pd

# train / test data location
train = "./data/phase2_train.csv"
test = "./data/phase2_test.csv"

# Read the extracted CSVs to pandas dataframes
train_df, test_df = pd.read_csv(train), pd.read_csv(test)

def preprocess(df):
    # change timestamp to pandas datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    # change column name to anomaly
    new_columns = df.columns.values
    new_columns[2] = "anomaly"
    df.columns = new_columns
    # change anomaly to boolean
    df["anomaly"] = df["anomaly"].astype(bool)
    return df

# preprocess the dataframes
train_df = preprocess(train_df)
test_df = preprocess(test_df)  

# get unique KPI IDs
kpi_ids = sorted(train_df["KPI ID"].unique())
for kpi in kpi_ids:
    train = train_df[train_df["KPI ID"] == kpi].drop(columns="KPI ID")
    test = test_df[test_df["KPI ID"] == kpi].drop(columns="KPI ID")

    # save the dataframes to csv
    train.to_csv("./train/"+f"train_aiops2020_ID{kpi}.csv", index=False)
    test.to_csv("./test/"f"test_aiops2020_ID{kpi}.csv", index=False)