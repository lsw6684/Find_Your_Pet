import tweepy
from keys import twitter
# API Key. 문자열로 입력.
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

keyword = '안락사'                  # 검색 키워드
result = []                         # 크롤링 텍스트 저장 리스트

for i in range(1,2):                # 1, 2 페이지 크롤링
    tweets = api.search(keyword)    # 검색 결과 담기
    for tweet in tweets:
        result.append(tweet.text)        # 결과 삽입

print(len(result))                  # 트윗 갯수
print(result)