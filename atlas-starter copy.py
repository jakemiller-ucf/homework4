from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import csv

# Update with your standard connection string
uri = "mongodb+srv://jakedmiller18:Jdm072403@cluster0.5rquymp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Try pinging the server
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Failed to connect to MongoDB:", e)
    exit()

# Set your DB and collection
db = client["military_marathon"]
collection = db["results"]

# Path to your CSV file
csv_path = "/Users/jake/Downloads/wdwM-military.csv"

# Read and insert CSV data
try:
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Optional: convert age to integer
    for row in data:
        if "age" in row:
            try:
                row["age"] = int(row["age"])
            except:
                row["age"] = None

    collection.insert_many(data)
    print("Data upload complete. Inserted", len(data), "documents.")
except Exception as e:
    print("Error reading or uploading data:", e)
