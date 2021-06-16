from pymongo import MongoClient
from twitter import extract_tweets
from openAPI import extract_info
from keys import s_MongoDB
import schedule

# URL로 호스트, 포트 지정
cluster = 'mongodb+srv://FYP:{}@cluster0.jzw1i.mongodb.net/test?retryWrites=true&w=majority'.format(s_MongoDB)
# collection 지정
client = MongoClient(cluster)

db = client.gettingStarted

infos = db.infos

def store_infos():
    for i in extract_info():
        infos.insert_one(
            {
                "age" : i[0],
                "pic" : i[1],
                "kind" : i[2],
                "care_place" : i[3],
                "sex" : i[4],
                "care_tel" : i[5],
                "state" : i[6]
            }
        )
def test():
    print("test")
schedule.every(1).second.do(test)


#print(extract_tweets())
#print("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
#print(extract_info()) 
