import logging
from datetime import datetime
import os
import pandas as pd

# Import modules from your folders
from config.db_config import get_engine
from etl.extract_load import extract_transactions
from etl.transform import calculate_net_effect
from visuals.dashboard_combined import generate_dashboard

from sqlalchemy import create_engine

def get_engine():
    """
    Creates and returns a SQLAlchemy engine to connect to the PostgreSQL database.
    Update your credentials below if needed.
    """
    user = "postgres"
    password = "postgres"
    host = "localhost"
    port = 5432
    database = "banking_db"  

    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine

# -------------------------
# Setup logging
# -------------------------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_filename = os.path.join(LOG_DIR, f"pipeline_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting Banking Data Engineering Pipeline")

try:
    # -------------------------
    # Step 1: Extract
    # -------------------------
    logging.info("Extracting transactions data...")
    transactions_df = extract_transactions()
    logging.info(f"Extracted {len(transactions_df)} rows successfully.")

    # -------------------------
    # Step 2: Transform
    # -------------------------
    logging.info("Calculating net effect per transaction...")
    transformed_df = calculate_net_effect(transactions_df)
    logging.info("Transformation complete.")

    # Save intermediate data
    transformed_path = "data/output/transactions_transformed.csv"
    transformed_df.to_csv(transformed_path, index=False)
    logging.info(f"Transformed data saved to {transformed_path}")

    # -------------------------
    # Step 3: Generate Dashboard
    # -------------------------
    logging.info("Generating interactive dashboard...")
    generate_dashboard()
    logging.info("Dashboard generation completed successfully.")

    logging.info("✅ Pipeline completed successfully!")

except Exception as e:
    logging.error(f"❌ Pipeline failed: {e}")
    print(f"Error occurred: {e}")

