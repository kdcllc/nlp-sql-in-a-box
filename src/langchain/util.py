import os


def get_connection_string():
    
    server_name = os.environ.get("SERVER_NAME")
    database_name = os.environ.get("DATABASE_NAME")
    username = os.environ.get("SQLADMIN_USER")
    password = os.environ.get("SQL_PASSWORD")
    connection_string = f'mssql+pyodbc://{username}:{password}@{server_name}/{database_name}?driver=ODBC+Driver+18+for+SQL+Server'
    return connection_string
