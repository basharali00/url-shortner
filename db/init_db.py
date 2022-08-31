import sqlite3


def create_connection(db_file):
    """ 
        create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
    except sqlite3.Error as e:
        print(e)

    return conn


def execute_sql_file(sql_file, connection):
    """
        Execute a sql file
        :param sql_file: sql file
        :return: void
    """
    with open(sql_file) as f:
        connection.executescript(f.read())
