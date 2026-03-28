from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE
db_path = Path('/Users/anushkashaw/dsnd-dashboard-project/python-package/employee_events/employee_events.db')



# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE
    def pandas_query(self,sql_query):
        conn = connect(db_path)
        try:
            df = pd.read_sql(sql_query, conn)
            return df
        finally:
            conn.close()

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    def query(self,sql_query):
        conn = connect(db_path)
        try:
            cursor = conn.cursor()
            result = cursor.execute(sql_query).fetchall()
            conn.commit()
            return result
        finally:
            conn.close()

        
    

 
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        return result
    
    return run_query
