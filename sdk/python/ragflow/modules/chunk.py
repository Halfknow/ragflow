from .base import Base


class Chunk(Base):
    def __init__(self, rag, res_dict):
        self.id = ""
        self.content = ""
        self.important_keywords = []
        self.create_time = ""
        self.create_timestamp = 0.0
        self.knowledgebase_id = None
        self.document_name = ""
        self.document_id = ""
        self.available = 1
        for k in list(res_dict.keys()):
            if k not in self.__dict__:
                res_dict.pop(k)
        super().__init__(rag, res_dict)


    def update(self,update_message:dict):
        res = self.put(f"/dataset/{self.knowledgebase_id}/document/{self.document_id}/chunk/{self.id}",update_message)
        res = res.json()
        if res.get("code") != 0 :
            raise Exception(res["message"])


