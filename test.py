from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(
    os.getenv("MONGO_DB_URL"),
    tls=True,
    serverSelectionTimeoutMS=10000
)

print(client.list_database_names())


print(client.list_database_names())
