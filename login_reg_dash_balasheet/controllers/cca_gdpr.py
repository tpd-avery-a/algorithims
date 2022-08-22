from controllers.mysqlconnection import connectToMySQL

class California:
    def __init__(self, data):
        self.id = data["id"]
        self.choice = data["choice"]
        self.ip_address = data["ip_address"]
        self.created_at = data["created_at"]
        self.updated_At = data["updated_at"]
    @classmethod
    def send(self, data):
        query = "INSERT INTO cca_consent(choice, ip_address, created_at, updated_at) VALUES(%(cca)s,%(ip_address)s,NOW(),NOW());"
        return connectToMySQL("login_training").query_db(query, data)


class Europe:
    def __init__(self, data):
        self.id = data["id"]
        self.choice = data["choice"]
        self.ip_address = data["ip_address"]
        self.created_at = data["created_at"]
        self.updated_At = data["updated_at"]
    @classmethod
    def send(self, data):
        query = "INSERT INTO gdpr_consent(choice, ip_address, created_at, updated_at) VALUES(%(gdpr)s,%(ip_address)s,NOW(),NOW());"
        return connectToMySQL("login_training").query_db(query, data)


class TopPeaksDevelopment:
    def __init__(self, data):
        self.id = data["id"]
        self.choice = data["choice"]
        self.ip_address = data["ip_address"]
        self.created_at = data["created_at"]
        self.updated_At = data["updated_at"]

    @classmethod
    def send(self, data):
        query = "INSERT INTO tpd_consent(choice, ip_address, created_at, updated_at) VALUES(%(tpd)s,%(ip_address)s,NOW(),NOW());"
        return connectToMySQL("login_training").query_db(query, data)
