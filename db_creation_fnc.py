import mysql.connector

class DB_Manager:
    def __init__(self,host="localhost",port = "", user="root",password="password"):
        print("DB_Manager started")
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            passwd=password,
            auth_plugin='mysql_native_password'
        )

    def reset(self,db):
        print("Dropping " + db)
        self.drop_db(db)
        print("Restarting " + db)
        self.start_db(db)
        print("Reset of " + db + " completed")

    def drop_db(self,db):
        cursor = self.db.cursor()
        cursor.execute("DROP DATABASE " + db)
        return cursor

    def start_db(self,db):
        cursor = self.db.cursor()
        cursor.execute("CREATE DATABASE " + db)
        cursor.close()

class DB:
    '''
    Connection to the database
    @param host, user, password
    returns database
    '''
    def __init__(self,db="database",host="localhost",port = "",user="root",password="password"):
        self.db = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            database=db,
            auth_plugin='mysql_native_password'
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
        cursor.close()
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
        cursor.close()
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
        sql = "INSERT INTO " + table_name + columns + " VALUES ("

        for i in range(0,len(values_to_insert[0])):
            sql += "%s,"

        sql = sql[0:-1] + ")"
        print(sql)

        if len(values_to_insert) > 1:
            cursor.executemany(sql,values_to_insert)
        elif len(values_to_insert) == 1:
            print(sql,values_to_insert[0])
            cursor.execute(sql, values_to_insert[0])

        self.db.commit()
        cursor.close()

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

    def select_from_table(self,table_name,columns = "*",where_condition = "",like_condition=""):
        cursor=self.db.cursor()
        sql = "SELECT " + columns + " FROM " + table_name
        if where_condition != "":
            sql += " WHERE " + where_condition
        if like_condition != "":
            sql += " LIKE " + like_condition

        print(sql) 
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        
        return result

    '''
    drop table
    '''
    def drop_table(self,table_name):
        cursor = self.db.cursor(buffered=True,dictionary=True)
        sql = "DROP TABLE " + table_name
        cursor.execute(sql)
        cursor.close()
        return cursor

    '''
    update a table

    @table_name name of the table
    @columns list of columns to be updated (e.g. ['name','surname'])
    @values tuple of the values to be put in the before mentioned columns (e.g. ('Chiara','Masci'))
    @where_condition
    '''
    def update_table(self,table_name,columns,val,where_condition):
        cursor = self.db.cursor(buffered=True,dictionary=True)
        sql = "UPDATE " + table_name + " SET "
        for column in columns:
            sql += " " + column + " = %s,"

    
        sql = sql[0:-1] + " WHERE " + where_condition
        print("Na, here: "+ sql)

        cursor.execute(sql,val)
        self.db.commit()
        cursor.close()
        
