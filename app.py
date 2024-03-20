#from app import create_app

#app = create_app()

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000)

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
mongo_uri = "mongodb+srv://marius:Mongodb2000.@bankappetti.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
client = MongoClient(mongo_uri)
db = client.yourdbname