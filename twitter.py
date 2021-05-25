import tweepy
from keys import twitter

# API Key.
key = twitter[0]
s_key = twitter[1]
token = twitter[2]
s_token = twitter[3]
# 핸들러 생성, 개인정보 인증 요청
auth = tweepy.OAuthHandler(key, s_key)
# Access 요청
auth.set_access_token(token, s_token)
# twitter API 생성
api = tweepy.API(auth)
keyword = '안락사'
tweets = api.search(keyword, count = 1) # 트윗 개수(RT는 밑 함수에서 제거)
result = []
def extract_tweets():
    
    # RT와 원본 게시글의 형태가 너무 다르다. >> RT를 버리자.
    for num, tweet in enumerate(tweets):                # num 번호. RT포함하면 살릴거임.
        tmp = []
        if "RT" not in tweet.text:
            tmp.append(tweet.created_at)                # 날짜 - 한국 시간 아닌 듯..
            tmp.append(tweet.user.profile_image_url)    # 작성자 프로필 이미지 null
            tmp.append(tweet.user.name)                 # 닉네임
            tmp.append(tweet.user.screen_name)          # 트위터 @id
            tmp.append(tweet.text)                      # 트윗 내용
            result.append(tmp)
    return result

import pandas as pd
from sklearn.model_selection import train_test_split
import re

X = []
for i in tweets:
    X.append(i.text)
print(X)
