from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient("mongodb+srv://yubik:12345@cluster0.cklcq.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["database"]#acess of current databaser
collist = db.list_collection_names()#finding collection list
login = bool()

def main(username, password):
    pass

