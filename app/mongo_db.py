from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS


class mongo_db: 

    def getAll(self):
        uri = "mongodb+srv://<dbName>:<password>@cluster0.e9tjso8.mongodb.net/?retryWrites=true&w=majority"

        # return uri

        # uri = "mongodb+srv://appMongo:<password>@cluster0.e9tjso8.mongodb.net/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        Database = client.get_database('notesdb')
        # Table
        notes = Database.notes

        query = notes.find()
        output = {}
        i = 0

        for x in query:
            output[i] = x
            output[i].pop('_id')
            i += 1
        return output