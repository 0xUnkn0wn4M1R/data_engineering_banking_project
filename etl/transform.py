import pandas as pd

def calculate_net_effect(df):
    """
    Adds a new column 'net_effect' to the DataFrame.
    Deposits are treated as positive, withdrawals as negative.
    """
    if 'txn_type' not in df.columns or 'amount' not in df.columns:
        print("⚠️ DataFrame missing required columns ('txn_type', 'amount').")
        return df

    df['net_effect'] = df.apply(
        lambda row: row['amount'] if row['txn_type'] == 'deposit' else -row['amount'],
        axis=1
    )

    print("✅ Net effect column added successfully.")
    return df
