from pymongo import MongoClient
# import certifi

MONGO_URI = 'mongodb://localhost:27017/'
# ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
