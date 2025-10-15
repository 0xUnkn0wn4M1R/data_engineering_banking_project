import pandas as pd
from config.db_config import get_engine

def extract_transactions():
    """
    Extracts transactions table from PostgreSQL database into a pandas DataFrame.
    """
    try:
        engine = get_engine()
        query = "SELECT * FROM transactions;"
        df = pd.read_sql(query, engine)
        print(f"✅ Extracted {len(df)} rows from transactions table.")
        return df

    except Exception as e:
        print(f"❌ Error while extracting transactions: {e}")
        return pd.DataFrame()  # Return empty DataFrame on failure
