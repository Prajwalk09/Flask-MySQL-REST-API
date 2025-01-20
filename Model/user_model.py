import mysql
import mysql.connector
from flask import make_response

class user_model():
    def __init__(self):
        # Connection Establishment Code
        try:
            self.conn = mysql.connector.connect(host = 'localhost', 
                                user = 'root', 
                                password = 'password', 
                                database='flask_tutorial'
                                )
            
            """Create a cursor object using cursor method.
            The argument specifies that the data has to be 
            displayed as a dictionary."""

            self.cur = self.conn.cursor(dictionary=True)
            self.conn.autocommit = True

            print("Connection Successful!")
        
        except Exception as e:
            print(f"Error : {e} occurred!")
    
    def user_getall_model(self):
        # Query Execution Code
        query = 'SELECT * FROM USERS'
        self.cur.execute(query)
        
        result = self.cur.fetchall()
        
        if len(result) == 0:
            res = make_response({"message" : "No Data Found"}, 204)
            res.headers['Acess-Control-Allow-Origin'] = '*'
            return res

        else:
            return make_response({'payload':result} , 200) 
    
    def user_addone_model(self, data):
        try:
            # Query Execution Code
            query = f'''INSERT INTO USERS (NAME, EMAIL, ROLE, PASSWORD)
                   VALUES
                   ('{data.get('name')}', '{data.get('email')}', 
                    '{data.get('role')}', '{data.get('password')}')'''
        
            self.cur.execute(query)
            
            return make_response({'message' : "User Created Successfully!"}, 201)

        except Exception as e:
            return {'Error' : e}
        
    def user_updateone_model(self, data):
        try:
            query = f'''UPDATE USERS SET
                        NAME = '{data.get('name')}', 
                        EMAIL = '{data.get('email')}',
                        ROLE = '{data.get('role')}',
                        PASSWORD = '{data.get('password')}'
                    WHERE ID = {data.get('id')}
                    '''
            self.cur.execute(query)
            
            if self.cur.rowcount > 0:
                # In case of any updates, rowcount is set > 0
                return make_response({'message' : "User Updated Successfully!"}, 201)
            else:
                # If same data (as existing) is sent, rowcount remains 0
                return make_response({'message' : "Nothing to Update!"}, 202)
        
        except Exception as e:
            return {'Error' : e}
        
    def user_delete_model(self, id):
        try:
            query = f'''DELETE FROM USERS
                   WHERE ID =  {id}'''
            self.cur.execute(query)
            if self.cur.rowcount > 0:
                # In case of any updates, rowcount is set > 0
                return make_response({'message' : "Nothing to Delete!"}, 200)

            else:
                # If same data (as existing) is sent, rowcount remains 0
                return make_response({'message' : "User Deleted Successfully!"}, 202)

        except Exception as e:
            return {'Error' : e}
        
    def user_patch_model(self, data, id):
        query = 'UPDATE USERS SET '
        for key in data:
            query = query + f"{key} = '{data.get(key)}',"
        query = query[:-1] + f" WHERE ID = {id}"
        
        self.cur.execute(query)
        
        if self.cur.rowcount > 0:
                # In case of any updates, rowcount is set > 0
                return make_response({'message' : "User Updated Successfully!"}, 201)
        else:
                # If same data (as existing) is sent, rowcount remains 0
            return make_response({'message' : "Nothing to Update!"}, 202)
    
    def user_pagination_model(self, limit, page):
        limit = int(limit)
        page = int(page)

        start = (page-1)*limit
        query = f'''SELECT * FROM USERS 
                    LIMIT {start}, {limit}'''
        
        self.cur.execute(query)
        result = self.cur.fetchall()

        if len(result) == 0:
            res = make_response({"message" : "No Data Found"}, 204)
            return res
        else:
            return make_response({'payload':result,
                                  'page_number': page,
                                  'limit' : limit} , 200) 
        
