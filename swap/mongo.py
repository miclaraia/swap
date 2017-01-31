################################################################
# Mongo client

from .config import Config

class Mongo:
    """
        Mongo

        The main interaction between the python code and the 
        supporting mongo database. All calls to the database
        should be made from here.
    """

    def __init__(self):
        config = Config()

        # Get database configuration from config file
        c = config.config
        host = c['database']['host']
        db_name = c['database']['name']
        port = c['database']['port']

        self._client = MongoClient('%s:%d' % (host,port))
        self._db = self._client[db_name]

    def test(self):
        print(self._db.collection_names())

