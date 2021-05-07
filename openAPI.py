import requests
from bs4 import BeautifulSoup
from keys import openAPI

key = openAPI[0]
results = requests.get("http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?bgnde=20140301&endde=20150430&pageNo=1&numOfRows=5&ServiceKey={}".format(key))
soup = BeautifulSoup(results.text, "html.parser")

info = soup.find("items")
infos = info.find_all("item")

def extract_info():
    result = []
    for test in infos:
        tmp = []
        tmp.append(test.select_one("age"))       # 나이
        tmp.append(test.select_one("popfile"))   # 동물 사진(원본)
        tmp.append(test.select("kindcd"))        # 종류
        tmp.append(test.select("carenm"))        # 보호 장소
        tmp.append(test.select("sexcd"))         # 성별
        tmp.append(test.select("caretel"))       # 보호 장소 번호
        tmp.append(test.select("processstate"))  # 상태(보호중, 안락사, 자연사)
        result.append(tmp)
    return result