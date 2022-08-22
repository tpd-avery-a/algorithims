from config.mysqlconnection import connectToMySQL

class SecurityCVE: 
    def __init__(self, data):
        self.id = data['id']
        self.cve_id = data['cve_id']
        self.description = data['description']
        self.links = data['links']
        self.created_at = data["created_at"]
        self.updated_at = data['updated_at']

    @classmethod
    def cve(cls):
        query = "SELECT * FROM cve;"
        results = connectToMySQL('login_training').query_db(query)
        items = []
        for item in results:
            items.append(cls(item))
        return items

class SecurityExchange:
    def __init__(self,data):
        self.id  = data['id']
        self.date = data['date']
        self.title = data['title']
        self.link = data['link']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def securitexchangepressrelease(cls):
        query = "SELECT * FROM secexcprerel;"
        results = connectToMySQL('login_training').query_db(query)
        items = []
        for item in results:
            items.append(cls(item))
        return items

class SecurityExchangeFiling:
    def __init__(self,data):
        self.id  = data['id']
        self.name = data['name']
        self.form = data['form']
        self.description = data['description']
        self.dateAccepted = data['dateAccepted']
        self.filingDate = data['filingDate']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def securitexchangefiling(cls):
        query = "SELECT * FROM secexcfil;"
        results = connectToMySQL('login_training').query_db(query)
        items = []
        for item in results:
            items.append(cls(item))
        return items
        
class Weather: 
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.timethere = data['timethere']
        self.temperature = data['temperature']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def weather(cls):
            query = "SELECT * FROM weather;"
            results = connectToMySQL('login_training').query_db(query)
            items = []
            for item in results:
                items.append(cls(item))
            return items

class WhiteHouse:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.category = data['category']
        self.time = data['time']
        self.link= data['link']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def whitehouse(cls):
            query = "SELECT * FROM white_house;"
            results = connectToMySQL('login_training').query_db(query)
            items = []
            for item in results:
                items.append(cls(item))
            return items

class House:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.time = data['time']
        self.info = data['info']
        self.host = data['host']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def house(cls):
            query = "SELECT * FROM house;"
            results = connectToMySQL('login_training').query_db(query)
            items = []
            for item in results:
                items.append(cls(item))
            return items

class Senate:
    def __init__(self, data):
        self.id = data['id']
        self.identifier = data['identifier']
        self.committee = data['committee']
        self.matter = data['matter']
        self.time = data['time']
        self.day_of_week = data['day_of_week']
        self.updated_at = data['update_at']
        self.created_at = data['created_at']
    
    @classmethod
    def senate(cls):
            query = "SELECT * FROM senate;"
            results = connectToMySQL('login_training').query_db(query)
            items = []
            for item in results:
                items.append(cls(item))
            return items

class Data:
    def __init__( self , data):
        try:
            self.id = data['id']
            self.name = data['name']
            self.price = data['price']
            self.day = data['day']
            self.percent = data['percent']
            self.weekly = data['weekly']
            self.monthly = data['monthly']
            self.yoy = data['yoy']
            self.date = data['date']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
        except:

            pass

        try:
            self.id = data['id']
            self.title = data['title']
            self.link = data['link']
            self.percent = data['created_at']
            self.weekly = data['updated_at']
        except:

            pass


    # Now we use class methods to query our database
    @classmethod
    def get_commodities(cls):
        query = "SELECT * FROM commodities;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_training').query_db(query)
        # Create an empty list to append our instances of friends
        items = []
        # Iterate over the db results and create instances of friends with cls.
        for item in results:
            items.append( cls(item) )
        return items

    @classmethod
    def get_alra(cls):
        query = "SELECT * FROM news WHERE station = \"Al-Arabyia\";"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_training').query_db(query)
        # Create an empty list to append our instances of friends
        items = []
        # Iterate over the db results and create instances of friends with cls.
        for item in results:
            items.append( cls(item) )
        return items

    @classmethod
    def get_alja(cls):
        query = "SELECT * FROM news WHERE station = \"Al-Jazeera\";"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_training').query_db(query)
        # Create an empty list to append our instances of friends
        items = []
        # Iterate over the db results and create instances of friends with cls.
        for item in results:
            items.append( cls(item) )
        return items
    @classmethod
    def get_bbc(cls):
        query = "SELECT * FROM news WHERE station = \"BBC\";"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_training').query_db(query)
        # Create an empty list to append our instances of friends
        items = []
        # Iterate over the db results and create instances of friends with cls.
        for item in results:
            items.append( cls(item) )
        return items

    @classmethod
    def get_cnn(cls):
        query = "SELECT * FROM news WHERE station = \"CNN\";"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_training').query_db(query)
        # Create an empty list to append our instances of friends
        items = []
        # Iterate over the db results and create instances of friends with cls.
        for item in results:
            items.append( cls(item) )
        return items
    
    @classmethod
    def get_sky(cls):
        query = "SELECT * FROM news WHERE station = \"SKY\";"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_training').query_db(query)
        # Create an empty list to append our instances of friends
        items = []
        # Iterate over the db results and create instances of friends with cls.
        for item in results:
            items.append( cls(item) )
        return items

    @classmethod
    def get_all_a_title(cls):
        query = "SELECT * FROM news;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_training').query_db(query)
        # Create an empty list to append our instances of friends
        items = []
        # Iterate over the db results and create instances of friends with cls.
        for item in results:
            items.append( cls(item) )
        return items

