from pymongo.mongo_client import MongoClient
import pandas as pd
# !!! pasword change !!!
uri = "mongodb+srv://mert:<password>@deneme.yxpoqn1.mongodb.net/?retryWrites=true&w=majority&appName=Deneme"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



db = client.Deneme
transactions_collection = db.sample_analytics.transactions


results = transactions_collection.find({})  # Empty filter to fetch everything
print(results)
print(db)
print(transactions_collection)

# Belgeleri bulma
results = transactions_collection.find()

all_data = list(results)
df = pd.DataFrame(all_data)
print(df)