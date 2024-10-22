import requests
import json

# 首先获取知识库列表
list_url = "http://localhost:18080/v1/kb/list"
update_url = "http://localhost:18080/v1/kb/update"

headers = {
    'Accept': 'application/json',
    'Authorization': '09a1969a8f7211ef94610242ac130006',
    'Content-Type': 'application/json;charset=UTF-8'
}

# 获取知识库列表
list_response = requests.get(list_url, headers=headers)
list_data = list_response.json()

kb_list = list_data.get('data', {})

# 遍历每个知识库并更新
for kb in kb_list:
    kb_id = kb['id']
    kb_name = kb['name']
    
    # 准备更新的payload
    update_payload = {
        "kb_id": kb_id,
        "name": kb_name,  # 保持原有名称
        "avatar": "",
        "description": None,
        "language": "Chinese",
        "permission": "team",
        "embd_id": "jina-embeddings-v3@Xinference",
        "parser_id": "naive",
        "parser_config": {
            "raptor": {
                "use_raptor": False
            },
            "chunk_token_num": 350,
            "delimiter": "\n!?;。；！？",
            "layout_recognize": False,
            "html4excel": False
        }
    }
    
    # 发送更新请求
    update_response = requests.post(update_url, headers=headers, json=update_payload)
    
    # 打印更新结果
    print(f"Updating KB - Name: {kb_name}, ID: {kb_id}")
    print(f"Update Response: {update_response.text}")
    print("---")

print("All knowledge bases have been updated.")