from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://678ho:rhkdgh14@cluster0.pfo6l.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["<dbname>"]
collection = db["products"]
products = db.products
def count():
    len = products.count_documents({})
    return len

db.products.delete_many({})