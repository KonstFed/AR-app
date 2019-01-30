import json,itertools

f = open("graph.json","r")
content=json.load(f)

#content={"width": 10, "nodes": [{"y": 3, "name": "church", "cost": 1.3, "id": 13, "x": 1}, {"y": 5, "name": "theater", "cost": 2.3, "id": 65, "x": 6}, {"y": 6, "name": "fontain", "cost": 0.3, "id": 76, "x": 7}, {"y": 5, "name": "university", "cost": 0.5, "id": 35, "x": 3}, {"y": 0, "name": "diamond", "cost": 1.1, "id": 70, "x": 7}, {"y": 0, "name": "food", "cost": 0.5, "id": 30, "x": 3}, {"y": 2, "name": "house", "cost": 1.5, "id": 42, "x": 4}, {"y": 5, "name": "infocenter", "cost": 1.0, "id": 45, "x": 4}, {"y": 7, "name": "burgers", "cost": 0.6, "id": 90, "x": 4}, {"y": 3, "name": "rail", "cost": 1.0, "id": 93, "x": 9}], "edges": [{"from_id": 70, "weight": 1.8, "to_id": 45}, {"from_id": 70, "weight": 1.8, "to_id": 90}, {"from_id": 70, "weight": 1.8, "to_id": 93}, {"from_id": 30, "weight": 1.8, "to_id": 13}, {"from_id": 30, "weight": 1.8, "to_id": 65}, {"from_id": 30, "weight": 1.8, "to_id": 76}, {"from_id": 30, "weight": 1.8, "to_id": 35}, {"from_id": 30, "weight": 1.8, "to_id": 70}, {"from_id": 30, "weight": 1.8, "to_id": 42}, {"from_id": 30, "weight": 1.8, "to_id": 45}, {"from_id": 30, "weight": 1.8, "to_id": 90}, {"from_id": 30, "weight": 1.8, "to_id": 93}, {"from_id": 42, "weight": 1.8, "to_id": 13}, {"from_id": 42, "weight": 1.8, "to_id": 65}, {"from_id": 42, "weight": 1.8, "to_id": 76}, {"from_id": 42, "weight": 1.8, "to_id": 35}, {"from_id": 42, "weight": 1.8, "to_id": 70}, {"from_id": 42, "weight": 1.8, "to_id": 30}, {"from_id": 42, "weight": 1.8, "to_id": 45}, {"from_id": 42, "weight": 1.8, "to_id": 90}, {"from_id": 42, "weight": 1.8, "to_id": 93}, {"from_id": 45, "weight": 1.8, "to_id": 13}, {"from_id": 45, "weight": 1.8, "to_id": 65}, {"from_id": 45, "weight": 1.8, "to_id": 76}, {"from_id": 45, "weight": 1.8, "to_id": 35}, {"from_id": 45, "weight": 1.8, "to_id": 70}, {"from_id": 45, "weight": 1.8, "to_id": 30}, {"from_id": 45, "weight": 1.8, "to_id": 42}, {"from_id": 45, "weight": 1.8, "to_id": 90}, {"from_id": 45, "weight": 1.8, "to_id": 93}, {"from_id": 90, "weight": 1.8, "to_id": 13}, {"from_id": 90, "weight": 1.8, "to_id": 65}, {"from_id": 90, "weight": 1.8, "to_id": 76}, {"from_id": 90, "weight": 1.8, "to_id": 35}, {"from_id": 90, "weight": 1.8, "to_id": 70}, {"from_id": 90, "weight": 1.8, "to_id": 30}, {"from_id": 90, "weight": 1.8, "to_id": 42}, {"from_id": 90, "weight": 1.8, "to_id": 45}, {"from_id": 90, "weight": 1.8, "to_id": 93}, {"from_id": 93, "weight": 1.8, "to_id": 13}, {"from_id": 93, "weight": 1.8, "to_id": 65}, {"from_id": 93, "weight": 1.8, "to_id": 76}, {"from_id": 93, "weight": 1.8, "to_id": 35}, {"from_id": 93, "weight": 1.8, "to_id": 70}, {"from_id": 93, "weight": 1.8, "to_id": 30}, {"from_id": 93, "weight": 1.8, "to_id": 42}, {"from_id": 93, "weight": 1.8, "to_id": 45}, {"from_id": 93, "weight": 1.8, "to_id": 90}], "height": 8}

def view_objects(content):
    for i in content["nodes"]:
        print(i["name"])

def create_indexes(content):
    indexes={}
    for i in range(len(content["nodes"])):
        indexes[content["nodes"][i]["id"]]=i
    return indexes

indexes=create_indexes(content)

def create_matrix(content,indexes):
    arr=[]
    for i in range(len(content["nodes"])):
        lst=[]
        for j in range(len(content["nodes"])):
            if i==j:
                lst.append(content["nodes"][i]["cost"])
            else:
                lst.append(0)
        arr.append(lst)
    for i in content["edges"]:
        arr[indexes[i["from_id"]]][indexes[i["to_id"]]]=i["weight"]
    return arr

matrix=create_matrix(content,indexes)

def view_edges(content):
    for i in content["edges"]:
        print(i)

def permutations(path):
    return list(itertools.permutations(path))

def create_nodes(number_of_nodes):
    path=[]
    for i in range(number_of_nodes):
        path.append(i)
    return path

nodes = create_nodes(len(content["nodes"]))

def create_symmetrical_matrix(matrix):
    temp=matrix.copy()
    for i in range(len(temp)):
        for j in range(len(temp)):
            temp[i][j]=temp[j][i]
    return temp

matrix=create_symmetrical_matrix(matrix)

def combinations(items):
    temp= list( set(itertools.compress(items,mask)) for mask in itertools.product(*[[0,1]]*len(items)) )
    temp.remove(temp[0])
    return temp


def find_paths(nodes):
    temp=combinations(nodes)
    paths={}
    for i in range(len(nodes)):
        paths[i]=[]
    for i in temp:
        lst=permutations(i)
        for j in lst:
            start_point=j[0]
            paths[start_point].append(j)
    for i in range(len(nodes)):
        paths[i].remove(paths[i][0])
    return paths

all_paths=find_paths(nodes)

def choose_best_path(all_paths,time,matrix):
    temp={}
    for i in range(len(all_paths)):
        best_cost=0
        best_path=[i]
        for j in all_paths[i]:
            cur_cost=0
            cur_time=0
            not_a_path=False
            for k in range(len(j)):
                cur_cost+=matrix[j[k]][j[k]]
                if k!=len(j)-1:
                    if matrix[j[k]][j[k+1]]==0:
                        not_a_path=True
                        break;
                    cur_time+=matrix[j[k]][j[k+1]]
            if not_a_path:
                continue
            if cur_cost>best_cost and cur_time<time:
                best_cost=cur_cost
                best_path=list(j).copy()
        temp[i]=[best_cost,best_path.copy()]
    return temp

def get_width_and_height(content):
    return [content["width"],content["height"]]

def correct_answer(answer,indexes):
    temp={}
    items=list(indexes.items())
    for i in indexes:
        temp[i]=answer[indexes[i]]
        for j in range(len(temp[i][1])):
            for item in items:
                if item[1]==temp[i][1][j]:
                    temp[i][1][j]=item[0]
                break
    return temp


time = 9

answer = choose_best_path(all_paths,time,matrix)

answer=correct_answer(answer,indexes)

print(answer)
