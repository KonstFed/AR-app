import json
f = open("C:\Projects\GitHub\Hakaton\AR-app\AR\graph.json","r")
content=json.load(f)

#content={"width": 10, "nodes": [{"y": 3, "name": "church", "cost": 1.3, "id": 13, "x": 1}, {"y": 5, "name": "theater", "cost": 2.3, "id": 65, "x": 6}, {"y": 6, "name": "fontain", "cost": 0.3, "id": 76, "x": 7}, {"y": 5, "name": "university", "cost": 0.5, "id": 35, "x": 3}, {"y": 0, "name": "diamond", "cost": 1.1, "id": 70, "x": 7}, {"y": 0, "name": "food", "cost": 0.5, "id": 30, "x": 3}, {"y": 2, "name": "house", "cost": 1.5, "id": 42, "x": 4}, {"y": 5, "name": "infocenter", "cost": 1.0, "id": 45, "x": 4}, {"y": 7, "name": "burgers", "cost": 0.6, "id": 90, "x": 4}, {"y": 3, "name": "rail", "cost": 1.0, "id": 93, "x": 9}], "edges": [{"from_id": 70, "weight": 1.8, "to_id": 45}, {"from_id": 70, "weight": 1.8, "to_id": 90}, {"from_id": 70, "weight": 1.8, "to_id": 93}, {"from_id": 30, "weight": 1.8, "to_id": 13}, {"from_id": 30, "weight": 1.8, "to_id": 65}, {"from_id": 30, "weight": 1.8, "to_id": 76}, {"from_id": 30, "weight": 1.8, "to_id": 35}, {"from_id": 30, "weight": 1.8, "to_id": 70}, {"from_id": 30, "weight": 1.8, "to_id": 42}, {"from_id": 30, "weight": 1.8, "to_id": 45}, {"from_id": 30, "weight": 1.8, "to_id": 90}, {"from_id": 30, "weight": 1.8, "to_id": 93}, {"from_id": 42, "weight": 1.8, "to_id": 13}, {"from_id": 42, "weight": 1.8, "to_id": 65}, {"from_id": 42, "weight": 1.8, "to_id": 76}, {"from_id": 42, "weight": 1.8, "to_id": 35}, {"from_id": 42, "weight": 1.8, "to_id": 70}, {"from_id": 42, "weight": 1.8, "to_id": 30}, {"from_id": 42, "weight": 1.8, "to_id": 45}, {"from_id": 42, "weight": 1.8, "to_id": 90}, {"from_id": 42, "weight": 1.8, "to_id": 93}, {"from_id": 45, "weight": 1.8, "to_id": 13}, {"from_id": 45, "weight": 1.8, "to_id": 65}, {"from_id": 45, "weight": 1.8, "to_id": 76}, {"from_id": 45, "weight": 1.8, "to_id": 35}, {"from_id": 45, "weight": 1.8, "to_id": 70}, {"from_id": 45, "weight": 1.8, "to_id": 30}, {"from_id": 45, "weight": 1.8, "to_id": 42}, {"from_id": 45, "weight": 1.8, "to_id": 90}, {"from_id": 45, "weight": 1.8, "to_id": 93}, {"from_id": 90, "weight": 1.8, "to_id": 13}, {"from_id": 90, "weight": 1.8, "to_id": 65}, {"from_id": 90, "weight": 1.8, "to_id": 76}, {"from_id": 90, "weight": 1.8, "to_id": 35}, {"from_id": 90, "weight": 1.8, "to_id": 70}, {"from_id": 90, "weight": 1.8, "to_id": 30}, {"from_id": 90, "weight": 1.8, "to_id": 42}, {"from_id": 90, "weight": 1.8, "to_id": 45}, {"from_id": 90, "weight": 1.8, "to_id": 93}, {"from_id": 93, "weight": 1.8, "to_id": 13}, {"from_id": 93, "weight": 1.8, "to_id": 65}, {"from_id": 93, "weight": 1.8, "to_id": 76}, {"from_id": 93, "weight": 1.8, "to_id": 35}, {"from_id": 93, "weight": 1.8, "to_id": 70}, {"from_id": 93, "weight": 1.8, "to_id": 30}, {"from_id": 93, "weight": 1.8, "to_id": 42}, {"from_id": 93, "weight": 1.8, "to_id": 45}, {"from_id": 93, "weight": 1.8, "to_id": 90}], "height": 8}

def view_objects(content):
    for i in content["nodes"]:
        print(i["name"])

def create_matrix(content):
    arr=[]
    for i in range(len(content["nodes"])):
        lst=[]
        for j in range(len(content["nodes"])):
            if i==j:
                lst.append(content["nodes"][i]["cost"])
            else:
                lst.append(0)
        arr.append(lst)
    return arr

start_point=0

def find_path(content,lst,path,all_ways=[]):
    if len(lst)==0:
        return path
    for i in lst:
        lst.remove(i)
        path.append(i)
        all_ways.append(find_path(content,lst,path,all_ways))
    return all_ways
        
lst=[0,1,2,3,4,5,6,7,8,9]
lst.remove(start_point)
print(find_path(content,lst,[start_point]))