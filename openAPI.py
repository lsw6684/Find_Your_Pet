from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
from keys import openAPI

key = openAPI[0]

today = date.today()
yesterday = date.today() - timedelta(1)
day = yesterday.strftime('%Y%m%d')

results = requests.get(f"http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?bgnde={day}&endde={day}&pageNo=1&numOfRows=500&ServiceKey={key}")
soup = BeautifulSoup(results.text, "html.parser")

info = soup.find("items")
infos = info.find_all("item")

def extract_info():
    result = []
    for test in infos:
        tmp = []
        tmp.append(test.select_one("age").get_text())           # 나이
        tmp.append(test.select_one("popfile").get_text())       # 동물 사진(원본)
        tmp.append(test.select_one("kindcd").get_text())        # 종류
        tmp.append(test.select_one("carenm").get_text())        # 보호 장소
        tmp.append(test.select_one("sexcd").get_text())         # 성별
        tmp.append(test.select_one("caretel").get_text())       # 보호 장소 번호
        tmp.append(test.select_one("processstate").get_text())  # 상태(보호중, 안락사, 자연사)
        result.append(tmp)
    return result