import mongoengine as mongo


class Database:
    def __init__(self, config):
        self.config = config
        self.connect()

    def connect(self):
        mongo.connect(
            db=self.config.DATABASE,
            host=self.config.DATABASE_HOST,
            port=self.config.DATABASE_PORT,
            username=self.config.DATABASE_USERNAME,
            password=self.config.DATABASE_PASSWORD
        )

