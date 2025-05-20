from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://MoisesBermejo:Moises2006*@moisesbermejo.clo8p.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

# definimos el método de conexión

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["MOISES"]
        return db
    except ConnectionError:
        print('Error de conexión con la bdd')
        return None

# if __name__ == "__main__":
#     db = dbConnection()
#     if db is not None:
#         print("✅ Conexión exitosa con la base de datos.")
#     else:
#         print("❌ No se pudo conectar.")



