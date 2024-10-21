import requests

url = "http://halfknow.site:18080/v1/kb/create"

payload = "{\"name\":\"测试10\"}"
headers = {
  'Accept': 'application/json',
  'Authorization': '314435be8f6b11efb8de0242ac130006',
  'Content-Type': 'application/json;charset=UTF-8'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
