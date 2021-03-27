import requests
from bs4 import BeautifulSoup

key = "wqljfYC29Uciln9CQMhGvnFSG2vMdnKmmPjjzEjLu2ddCpDuH7cxed7Z2DxvlbwriHyVFJ%2BzJQIMym8V28thWg%3D%3D"
result = requests.get("http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?bgnde=20140301&endde=20140430&pageNo=1&numOfRows=5&ServiceKey={}".format(key))

soup = BeautifulSoup(result.text, "html.parser")

info = soup.find("item")

print(info)
