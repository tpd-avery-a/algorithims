from config.mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data["id"]
        self.fname = data["fname"]
        self.lname = data["lname"]
        self.email = data["email"]
        self.pword = data["pword"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_user(cls, email):
        query = "SELECT * FROM users WHERE email = \""+email+"\";"
        results = connectToMySQL("python_exam").query_db(query)
    #    Didn't find a matching user
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO users(fname,lname,email,pword,created_at,updated_at) VALUES(%(fname)s,%(lname)s,%(email)s,%(pword)s,NOW(),NOW());"
        results = connectToMySQL("python_exam").query_db(query,data)
        return results

class Shows:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.release_date = data["release_date"]
        self.description = data["description"]
        self.created_by = data["created_by"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_shows(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL("python_exam").query_db(query)
        items = []
        for item in results:
            items.append(cls(item))
        return items

    @classmethod
    def get_show(cls, id):
        id = str(id)
        query = "SELECT * FROM shows WHERE id = "+id+";"
        results = connectToMySQL("python_exam").query_db(query)
        items = []
        for item in results:
            items.append(cls(item))
        return items

    @classmethod
    def insert_shows(cls, data):
        query = "INSERT INTO shows(title,network,release_date,description,created_by,created_at,updated_at) VALUES(%(title)s,%(network)s,%(release_date)s,%(description)s,%(created_by)s,NOW(),NOW());"
        result = connectToMySQL("python_exam").query_db(query,data)
        return result

    @classmethod
    def delete_show(self, id):
        query = "DELETE FROM shows WHERE id = "+str(id)+";"
        result = connectToMySQL("python_exam").query_db(query)
        return result