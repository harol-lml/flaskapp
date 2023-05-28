import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime
from bson.objectid import ObjectId


class mongo_db:

    dbname = os.getenv('DB_NAME')
    dbpass = os.getenv('DB_PASSWORD')
    uri = f"mongodb+srv://{dbname}:{dbpass}@cluster0.e9tjso8.mongodb.net/?retryWrites=true&w=majority"

    def getAll(self):

        # Create a new client and connect to the server
        client = MongoClient( self.uri, server_api=ServerApi('1'))
        Database = client.get_database('notesdb')
        # Table
        notes = Database.notes

        query = notes.find()
        output = {}
        i = 0

        for x in query:
            output[i] = x
            output[i]['_id'] = str(output[i]['_id'])
            i += 1
        return output

    def getById(self, id):
        client = MongoClient( self.uri, server_api=ServerApi('1'))
        Database = client.get_database('notesdb')
        # Table
        notes = Database.notes

        query = notes.find_one({"_id":ObjectId(id)})

        query['_id'] = str(query['_id'])
        query['date'] = str(query['date'])
        return query

    def postNote(self, data):
        note = {
            "date": datetime.now(),
            "content": data['content'],
            "name": data['name']
        }
        # return data['data']
        client = MongoClient( self.uri, server_api=ServerApi('1'))
        Database = client.get_database('notesdb')
        notes = Database.notes
        nnote = notes.insert_one(note)
        print(type(nnote.inserted_id))
        new_note = notes.find_one({"_id":nnote.inserted_id})
        new_note['_id'] = str(new_note['_id'])
        new_note['date'] = str(new_note['date'])
        return (new_note)

    def putNote(self, data):
        noteUpdate = {"$set":{
            "date": datetime.now(),
            "content": data['content']
        }}

        client = MongoClient( self.uri, server_api=ServerApi('1'))
        Database = client.get_database('notesdb')
        notes = Database.notes
        myNote = {"_id": ObjectId(data['old'])}

        notes.update_one(myNote,noteUpdate)
        for x in notes.find():
            print(x)

    def deleteNote(self, id):

        client = MongoClient( self.uri, server_api=ServerApi('1'))
        Database = client.get_database('notesdb')
        notes = Database.notes
        notes.delete_one({"_id": ObjectId(id)})
        for x in notes.find():
            print(x)

        return id