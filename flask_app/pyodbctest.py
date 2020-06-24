import pyodbc



class MSDBconnection():

    # Should establish connection with any DB we have in MSsql
    def __init__(self, database = 'e-books-db',server = 'localhost',username = 'root',password = 'ssss'):
        # 1) DB server connection variables
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = self._establish_connection()
        self.cur = self.conn.cursor()

    # 2) Establishing the connection
    def _establish_connection(self):
        connection = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};'
                                    'SERVER=' + self.server +
                                    ';DATABASE=' + self.database +
                                    ';UID=' + self.username +
                                    ';PWD=' + self.password)
        return connection

    # open to SQL injection - very bad btw
    def sql_query(self, sql_string):
        # Usually, should have a check here to filter our DROP and only allow certain sql queries
        return self.cur.execute(sql_string)

nwind = MSDBconnection()

results = nwind.sql_query("SELECT * FROM books")

# nwind.sql_query(f"""INSERT INTO books
#                     (title, author, published_date)
#                     VALUES
#                     ('Old Man', 'Stefan Okolo', '2010') """)
#
# check = nwind.sql_query("SELECT * FROM books WHERE author='Stefan Okolo' ")
#
# print(check.fetchall())