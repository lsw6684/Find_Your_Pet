import requests
from bs4 import BeautifulSoup
from keys import openAPI

key = openAPI[0]
result = requests.get("http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?bgnde=20140301&endde=20150430&pageNo=1&numOfRows=5&ServiceKey={}".format(key))

soup = BeautifulSoup(result.text, "html.parser")

info = soup.find("items")
infos = info.find_all("item")
spans = []
num = 0
for test in infos:
    print(test.select_one("age"))
    print(test.select_one("popfile"))
    print(test.select_one("careAddr"))
    print("--------------")
    num+=1
print(num)