import requests
import json

url = "http://localhost:18080/v1/kb/list"

payload = {}
headers = {
    'Accept': 'application/json',
    'Authorization': '09a1969a8f7211ef94610242ac130006',
    'Content-Type': 'application/json;charset=UTF-8'
}

response = requests.request("GET", url, headers=headers, data=payload)

# 解析JSON响应
data = json.loads(response.text)

kb_list = data.get('data', {})

# 打印每个知识库的名称和ID
for kb in kb_list:
    print(f"Name: {kb['name']}, ID: {kb['id']}")