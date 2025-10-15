from sqlalchemy import create_engine

def get_engine():
    """
    Creates and returns a SQLAlchemy engine to connect to the PostgreSQL database.
    Update your credentials below if needed.
    """
    user = "postgres"
    password = "postgres"   #
    host = "localhost"
    port = 5432
    database = 'banking_db' 
    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine
