import json


def get_data_from_db():
    with open('input-task-3.json') as json_file:
        return json.load(json_file)
class Node: 
    def __init__(self, title, id, children):
        self.title = title
        self.id = id
        self.children = children

class Tree: 
    def __init__(self): 
        data = get_data_from_db()
        
        for node in data : 
            if not node["parent_knowledge_id"]: 
                self.head = Node(node["title"], node["id"], [])
        depth = 0
        print(self.head)
        x = self.head
        for node in data : 
            if node["parent_knowledge_id"] == self.head.id: 
                print('asd')
                print(self.head)
                x.children.append(Node(node["title"], node["id"], []))
            else: 
                print(depth)
                depth = depth +1 
                x = x.children
        pass 

if __name__ == '__main__':
    ll = Tree()