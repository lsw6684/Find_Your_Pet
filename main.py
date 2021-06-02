#from pymongo import MongoClient
from twitter import extract_tweets
from openAPI import extract_info
from keys import s_MongoDB

# URL로 호스트, 포트 지정
cluster = "mongodb+srv://FYP:{}@cluster0.jzw1i.mongodb.net/test?retryWrites=true&w=majority".format(s_MongoDB)
# collection 지정
#client = MongoClient(cluster)

#print(client.list_database_names())

#db = client.test

#print(db.list_collection_names())

#print(client.list_database_names())

print(extract_tweets())
print("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
print(extract_info()) 
