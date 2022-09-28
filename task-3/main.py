import json


def get_data_from_db():
    with open('input-task-3.json') as json_file:
        return json.load(json_file)
class Node: 
    def __init__(self, title, id):
        self.title = title
        self.id = id
        self.children = []
    def add(self, child):
        self.children.append(child)
        
def List(tree, head):
    if tree.get(head):
        for node in tree[head]: 
            print(node.id)
            List(tree,node.id)

class Tree: 
    def __init__(self): 
        data = get_data_from_db()
        tree = dict()
        for node in data: 
            if not node["parent_knowledge_id"]: 
                tree["head"] = []
                tree["head"].append(Node(node["title"],node["id"]))
            else: 
                if not tree.get(node["parent_knowledge_id"]): 
                    tree[node["parent_knowledge_id"]] = []
                    tree[node["parent_knowledge_id"]].append(Node(node["title"],node["id"]))
                else: 
                    tree[node["parent_knowledge_id"]].append(Node(node["title"],node["id"]))
        List(tree, "head")
        pass

if __name__ == '__main__':
    ll = Tree()