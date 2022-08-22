
from controllers.mysqlconnection import connectToMySQL

class User_info:     
    def __init__(self,data):
            self.id = data["id"],
            self.uname = data["uname"],
            self.email = data["email"],
            self.created_at = data["created_at"],
            self.updated_at = data["updated_at"]

    @classmethod
    def register(self,data):  
        data = {
            "uname" : data["uname"],
            "email" : data["email"]
        }
       
        query = "INSERT INTO user (uname ,email, created_at, updated_at) VALUES( \"%(uname)s\" ,\"%(email)s\",NOW() , NOW());"
        return connectToMySQL("login_training").query_db(query, data)

    def get_user_info(cls,data):
        query = "SELECT email FROM user WHERE email = %(email)s;" 
        result = connectToMySQL("login_training").query_db(query, data)
        items = []
        for item in result:
            items.append(cls(item))
    
        return result

class User_config:
    def __init__(self,data):
            self.id = data["id"],
            self.user_id = data["user_id"],
            self.weather = data["weather"],
            self.salt = data["salt"],
            self.pword = data["pword"],
            self.ip_address = data["ip_address"],
            self.test_pword = data["test_pword"],
            self.created_at = data["created_at"],
            self.updated_at = data["updated_at"]

    @classmethod
    def register_user_config_info(self,data):  
        data = {
            "weather" : data["weather"],
            "pword" : data["pword"],
            "salt" : data["salt"]
        }
       
        query = "INSERT INTO user_config (weather, salt, pword, created_at, updated_at) VALUES( \"%(weather)s\" ,\"%(salt)s\",\"%(pword)s\",NOW(),NOW());"
        return connectToMySQL("login_training").query_db(query, data)
    @classmethod

    def get_user_config_info(cls, data):
        data = {
            "id" : data["id"]
        }
        query = "SELECT pword FROM user_config WHERE user_id = %(id)s;"
        results = connectToMySQL("login_training").query_db(query, data)
        items = []
        for item in results:
            items.append(cls(item))
        return items