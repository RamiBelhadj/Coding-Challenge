import json


def get_data_from_db():
    with open('../mock-data.json') as json_file:
        return json.load(json_file)


class Cache:
    def __init__(self):
        self.data = get_data_from_db()
        pass
    def addMail(self, mailAccountId, messageId, dateTime):
        self.data["data"]["data_points"].append({"message_id" : messageId, "account_id" : mailAccountId, "created_at": dateTime, "data_point_type":"EMAIL"})
        with open('../mock-data.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def checkMail(self, messageId):
        for k, v in enumerate(self.data["data"]["data_points"]):
            if v["message_id"] == messageId:
                return True
        return False

    def removeMail(self, dateTime):
        data =[]
        for k, v in enumerate(self.data["data"]["data_points"]):
            if v["created_at"] >= dateTime : 
                data.append(v)
        self.data["data"]["data_points"] = data 
        with open('../mock-data.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
    
    def oldestMail(self): 
        data = sorted(self.data["data"]["data_points"], key=lambda x: x["created_at"])
        return data[0]["created_at"]

if __name__ == '__main__':
    cache = Cache()   
    cache.oldestMail() 