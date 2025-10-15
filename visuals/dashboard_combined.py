import pandas as pd
import plotly.express as px
from config.db_config import get_engine
import os

def generate_dashboard():
    """
    Generates an interactive Plotly dashboard showing transaction analysis.
    The resulting dashboard is saved as data/output/banking_dashboard.html
    """
    try:
        # Create database engine
        engine = get_engine()

        # Query sample data
        query = "SELECT * FROM transactions;"
        df = pd.read_sql(query, engine)

        if df.empty:
            print("⚠️ No data found in transactions table. Dashboard not generated.")
            return

        # Basic aggregation: total amount by transaction type
        summary = df.groupby('txn_type')['amount'].sum().reset_index()

        # Create chart
        fig = px.bar(
            summary,
            x='txn_type',
            y='amount',
            title='Total Deposit vs Withdrawal Amounts',
            color='txn_type',
            text='amount'
        )

        # Save dashboard
        output_dir = "data/output"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "banking_dashboard.html")
        fig.write_html(output_path)

        print(f"✅ Dashboard generated successfully at {output_path}")

    except Exception as e:
        print(f"❌ Error while generating dashboard: {e}")
