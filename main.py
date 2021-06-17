from pymongo import MongoClient
from twitter import extract_tweets
from openAPI import extract_info
from keys import s_MongoDB
import schedule
import time

# URL로 호스트, 포트 지정
cluster = 'mongodb+srv://FYP:{}@cluster0.jzw1i.mongodb.net/test?retryWrites=true&w=majority'.format(s_MongoDB)
# collection 지정
client = MongoClient(cluster)

db = client.open_data

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
# 00시 01분 : 전날 데이터 업데이트
schedule.every().day.at("0:1").do(store_infos)
while True:                 # 무한 루프로 스케줄 유지
	schedule.run_pending() 
	time.sleep(1) 

#print(extract_tweets())
#print("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
#print(extract_info()) 