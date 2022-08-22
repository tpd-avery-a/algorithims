from mysqlconnection import connectToMySQL

class Earnings:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.amount_earned = data["amount_earned"]
        self.payment_type = data["payment_type"]
        self.city_taxes = data["city_taxes"]
        self.state_taxes = data["state_taxes"]
        self.federal_taxes = data["federal_taxes"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        pass
    @classmethod
    def get(cls, data):
        query = "SELECT * FROM WHERE id = %(id)s"
        results = connectToMySQL("login_training").query_db(query,data)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        pass
    @classmethod
    def insert(self, data):
        pass
class Assets:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.name = data["name"]
        self.category = data["payment_type"]
        self.location = data["city_taxes"]
        self.warranty = data["state_taxes"]
        self.unit_value = data["federal_taxes"]
        self.qty = data["user_id"]
        self.value = data["value"]
        self.model = data["model"]
        self.serial_num = data["serial_num"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        pass
    @classmethod
    def get(cls, data):
        query = "SELECT * FROM WHERE id = %(id)s"
        results = connectToMySQL("login_training").query_db(query,data)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        pass
    @classmethod
    def insert(self, data):
        pass
class Reciepts:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.amt_paid = data["amt_paid"]
        self.payment_type = data["payment_type"]
        self.items = data["items"]
        self.city_taxes = data["city_taxes"]
        self.state_taxes = data["state_taxes"]
        self.federal_taxes = data["federal_taxes"]
        self.trans_id = data["trans_id"]
        self.business_name = data["business_name"]
        self.business_poc = data["business_poc"]
        self.business_address = data["business_address"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        pass
    @classmethod
    def get(cls, data):
        query = "SELECT * FROM WHERE id = %(id)s"
        results = connectToMySQL("login_training").query_db(query,data)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        pass
    @classmethod
    def insert(self, data):
        pass
class Liabilties:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.name = data["name"]
        self.category = data["category"]
        self.location = data["location"]
        self.warranty = data["warranty"]
        self.unit_value = data["unit_value"]
        self.qty = data["qty"]
        self.value = data["value"]
        self.model = data["model"]
        self.serial_num = data["serial_num"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    
    @classmethod
    def get(cls, data):
        query = "SELECT * FROM WHERE id = %(id)s"
        results = connectToMySQL("login_training").query_db(query,data)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        pass
    @classmethod
    def insert(self, data):
        pass

class Fixed_Expenses:
    def __init__(self, data):
        self.id = data["id"]
        self.due_Date = data["due_Date"]
        self.payment_amt = data["payment_amt"]
        self.date_start = data["date_start"]
        self.payment_start = data["payment_start"]
        self.city_taxes = data["city_taxes"]
        self.state_taxes = data["state_taxes"]
        self.federal_taxes = data["federal_taxes"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        pass
    @classmethod
    def get(cls, data):
        query = "SELECT * FROM WHERE id = %(id)s"
        results = connectToMySQL("login_training").query_db(query,data)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        pass
    @classmethod
    def insert(self, data):
        pass
class Variable_Expenses:
    def __init__(self, data):
        self.id = data["id"]
        self.due_Date = data["due_Date"]
        self.payment_amt = data["payment_amt"]
        self.date_start = data["date_start"]
        self.payment_type = data["payment_type"]
        self.city_taxes = data["city_taxes"]
        self.state_taxes = data["state_taxes"]
        self.federal_taxes = data["federal_taxes"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        pass
    @classmethod
    def get(cls, data):
        query = "SELECT * FROM WHERE id = %(id)s"
        results = connectToMySQL("login_training").query_db(query,data)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        pass
    @classmethod
    def insert(self, data):
        pass
class Transportation: 
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.vehicle_type = data["vehicle_type"]
        self.depart_date = data["depert_date"]
        self.return_date = data["return_date"]
        self.mile_coverage = data["mile_coverage"]
        self.notes = data["notes"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        pass
    @classmethod
    def get(cls, data):
        query = "SELECT * FROM WHERE id = %(id)s"
        results = connectToMySQL("login_training").query_db(query,data)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        pass
    @classmethod
    def insert(self, data):
        pass