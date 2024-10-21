import requests

url = "http://halfknow.site:18080/v1/kb/create"

payload = "{\"name\":\"测试10\"}"
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Authorization': 'e3f1440a89ef11ef9f520242ac130006',
  'Content-Type': 'application/json;charset=UTF-8',
  'Origin': 'http://halfknow.site:18080',
  'Proxy-Connection': 'keep-alive',
  'Referer': 'http://halfknow.site:18080/knowledge',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
  'Cookie': 'session=lg2w-pJhmApS6A4AV9ntCVrFNI_VpAoDOMj1W-FA8ZE'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
