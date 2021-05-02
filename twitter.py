import tweepy

# API Key. 문자열로 입력.
key = 'sgq60siaDbv9v8g8jiQGlgVFt'
s_key = 'yxaGk3SdvewwOnMFpuGMfEZkpPkLstUPUQXBPLwt4Y7cr9gnqa'
token = '304408446-bRTf10WlHTetwJkr7TjRrEPt4nKL8Lc7qqWdIp5s'
s_token = 'b3PFtLyoRTeMljSjwRGOZui4tjWtEO2aytnApHeSd4uUA'
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