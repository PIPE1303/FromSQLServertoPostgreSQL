##    HERE IS THE MAIN PIPELINE TO EXECUTE THE CONNECTION 
#       TO A POSTGRESQL DB AND SAVE THE QUERY REQUESTED

from sqlalchemy import  create_engine
from pandas import DataFrame
import sys

User = "admin"
Pass = "Pass12345"
Host = "localhost"
Db = "company"

def upload(Data: DataFrame, table: str) -> None:
    """Function to upload a SQL Server query, into a postgres database

    Args:
        Data (DataFrame): Query saved in a pandas DataFrame
        table (str): Name of the table that will be created
    """
    try:
        engine = create_engine(f'postgresql+psycopg2://{User}:{Pass}@{Host}/{Db}')

        Data.to_sql(table, con=engine, if_exists='append')
    except Exception as error:
        print(f"Fatal error")
        print(error.args)
        sys.exit(1)