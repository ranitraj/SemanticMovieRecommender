import pymongo


class MongoAtlasClient:
    def __init__(self, uri_template, password):
        self.uri = uri_template.replace('<password>', password)
        self.client = pymongo.MongoClient(self.uri)
