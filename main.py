import requests, xmltodict, json

url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
params ={'serviceKey' : 't4v1UeV4c4YSApJN0GdQFuAFM6gl2TQ7oDoptueOxC3fcyXXsvq3kRvmi+Yz4Ml1qzLWpJlO5jRiUSViB8B5vA==',
         'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'itemCode' : 'PM10', 'dataGubun' : 'HOUR', 'searchCondition' : 'MONTH' }

response = requests.get(url, params=params)
data = json.loads(response.content.decode('utf-8'))
print(data['response']['body']['items'])