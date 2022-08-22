from controllers.mysqlconnection import connectToMySQL

class Query:

    def __init__(self , data ):
        try:
            self.id = data['id'],
            self.username = data['username'],
            self.message = data['message']
        except KeyError:
            pass

        try:
            self.id = data['project_id'],
            self.project_name = data['project_name'],
            self.preview_link = data['preview_link'],
            self.next_meeting = data['next_meeting'],
            self.next_update = data['next_update'],
            self.last_update = data['last_update'],
            self.current_feature = data['current_feature'],
            self.client_id = data['client_id']
        except KeyError:
            pass

        
    @classmethod
    def SelectExample(cls):
        query = "SELECT * FROM tablename;"
        results = connectToMySQL('databaseName').query_db(query)
        items = []
        for item in results:
            items.append(cls(item))
            item = "\""
        return items
    pass

    @classmethod
    def InsertExamples(cls, data):
        query = "INSERT INTO tablename (catName, CatName) VALUES(%(valueName)s,%(valueName)s,NOW(),NOW());"
        return connectToMySQL('databasename').query_db(query,data)
    pass
#
#
#
    @classmethod
    def retrieve_project(cls):
        query = "SELECT * FROM client_project;"
        results = connectToMySQL('chat_room_test').query_db(query)
        items = []
        for item in results:
            items.append(item)
        return items
    pass

    @classmethod
    def send_message(cls, data):
        query = "INSERT INTO chatroom (username, message) VALUES(%(username)s,%(message)s);"
        return connectToMySQL('chat_room_test').query_db(query, data)
    pass

    @classmethod
    def retrieve_messages(cls):
        query = "SELECT * FROM chatroom;"
        results = connectToMySQL('chat_room_test').query_db(query)
        items = []
        for item in results:
            items.append(cls(item))
        return items
    pass