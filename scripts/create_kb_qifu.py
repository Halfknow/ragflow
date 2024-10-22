import requests
import json

url = "http://localhost:18080/v1/kb/create"

# 创建一个包含多个名字的列表
names = ["宁波市本级企业政策知识库", "鄞州区企业政策知识库", "海曙区企业政策知识库", "江北区企业政策知识库", "北仑区企业政策知识库", "镇海区企业政策知识库", "奉化区企业政策知识库", "余姚市企业政策知识库", "慈溪市企业政策知识库", "象山县企业政策知识库", "宁海县企业政策知识库", "高新区企业政策知识库", "前湾新区企业政策知识库", "诉求知识库", "项目服务知识库"]

headers = {
    'Accept': 'application/json',
    'Authorization': '09a1969a8f7211ef94610242ac130006',
    'Content-Type': 'application/json;charset=UTF-8'
}

# 遍历名字列表，为每个名字发送请求
for name in names:
    payload = json.dumps({"name": name})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"创建 '{name}' 的响应：")
    print(response.text)