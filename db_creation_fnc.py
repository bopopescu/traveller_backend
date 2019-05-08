import mysql.connector


class DB:
    '''
    Connection to the database
    @param host, user, password
    returns database
    '''
    def __init__(self,db="traveller",host="localhost",user="root",password="password"):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=db,
            auth_plugin='caching_sha2_password'
        )


    '''
    List of created databases
    @param none
    returns cursor (list of databases)
    '''

    def db_list(self):
        cursor = self.db.cursor()
        cursor.execute("SHOW DATABASES")
        return cursor


    '''
    Creation of a table in db

    @param db: name of the database
    @param table_name: name of the table to create
    @param columns_list: list of the columns to add in the new table (example: ['name VARCHAR(255','address VARCHAR(255)'])
    '''
    def create_table(self,table_name,columns_list,keys=""):
        cursor = self.db.cursor()

        columns_list_string = ""

        for i,column in enumerate(columns_list):
            columns_list_string += column
            if i != len(columns_list) - 1:
               columns_list_string +=  ", "

        sql = "CREATE TABLE " + table_name + " (" + columns_list_string # cdk

        if keys != "":
            sql +=  ", " + keys + ")"
        else:
            sql += ")"

        print(sql)
        cursor.execute(sql)
        return cursor


    '''
    List of created tables in db
    @param db: name of the database
    returns cursor (list of tables)
    '''
    def tables_list(self):
        cursor=self.db.cursor(buffered=True,dictionary=True)
        cursor.execute("SHOW TABLES")
        cursor.close()
        return cursor

    '''
    Modify a table (Add columns, change names...)
    @param db
    @param table_name
    @param alter_command (example "ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    '''
    def alter_table(self,table_name,alter_command):
        cursor=self.db.cursor()
        cursor.execute("ALTER TABLE"+ table_name + alter_command)
        return cursor

    '''
    insert values in table
    @param db
    @param table_name
    @param columns (example "(name, address)")
    @param values_to_insert (example [('Peter','Lowstreet'),('Amy','Apple')])
    @param return_value: what you want to be returned, either the id of the last row ("lastrowid") or the number of the inserted rows ("rowcount")

    returns number of rows inserted of the id of the last inserted row
    '''
    def insert_in_table(self,table_name, values_to_insert,columns = "",return_value = "lastrowid"):
        cursor=self.db.cursor()
        sql = "INSERT INTO" + table_name + columns + "VALUES (%s,%s)"

        if len(values_to_insert) > 1:
            cursor.executemany(sql,values_to_insert)
        elif len(values_to_insert) == 1:
            mycursor.execute(sql, values_to_insert)

        self.db.commit()

        if return_value == "rowcount":
            return cursor.rowcount
        elif return_value == "lastrowid":
            return cursor.lastrowid
        else:
            print ("invalid return value")

    '''
    Get from table
    @param db
    @param table_name
    @param columns (example "name,surname"). Default value: "*"
    @param where_condition (example "name ='Alessia'")
    @param like_condition (example "'%way%'")

    returns the selected rows
    '''

    def select_from_table(self,table_name,columns = "*",where_condition = "",like_condition = "", order_by = "",return_value = "lastrowid"):
        cursor=self.db.cursor()
        sql = "SELECT" + columns + "FROM " + table_name
        if where_condition != "":
            sql += "WHERE " + where_condition
        if like_condition != "":
            sql += "LIKE " + like_condition
        cursor.execute(sql)
        result = cursor.fetchall()
        
        return result

    def drop_table(self,table_name):
        cursor = self.db.cursor(buffered=True,dictionary=True)
        sql = "DROP TABLE " + table_name
        cursor.execute(sql)
        return cursor

    def drop_all_tables(self):
        tables = self.tables_list()

        for table in tables:
            self.drop_table(table['Tables_in_traveller'])
        
