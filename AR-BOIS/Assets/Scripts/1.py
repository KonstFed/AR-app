import json

f=open("graph-2.json","r")
content=json.load(f)
f.close()

def view_objects(content):
    for i in content["nodes"]:
        print(i["name"])

def view_edges(content):
    for i in content["edges"]:
        print(i)

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

def find_children(arr,node):
    lst=[]
    for i in range(len(arr[0])):
        if arr[node][i]!=0 and node!=i:
            lst.append(i)
    return lst

def pprint(arr):
    for i in arr:
        print(i)

def all_paths(arr,node,lst=[],main_lst=[],count=0):
    temp_lst=lst.copy()
    temp_lst.append(node)
    children=find_children(arr,node)
    if len(children)==0:
        main_lst.append(temp_lst)
    for i in children:
        if i not in temp_lst:
            count+=1
            all_paths(arr,i,temp_lst,main_lst,count)
        else:
            if count==len(arr):
                main_lst.append(temp_lst)
    return main_lst
    
arr=create_matrix(content,indexes)

def find_id(element,indexes):
    for i in indexes:
        if indexes[i]==element:
            return i


def best_path(matrix,arr,time):
    global allall
    best_cost=0
    best_time=0
    best_path=[]
    for i in arr:
        cur_cost=0
        cur_time=0
        for j in range(len(i)):
            if j!=len(i)-1:
                element1=i[j]
                element2=i[j+1]
                cur_time+=matrix[element1][element2]
            cur_cost+=matrix[i[j]][i[j]]
        if cur_cost>=best_cost and cur_time<time:
            if cur_cost>best_cost:
                best_cost=cur_cost
                best_time=cur_time
                best_path=i.copy()
            else:
                if cur_time<best_time:
                    best_cost=cur_cost
                    best_time=cur_time
                    best_path=i.copy()
    return [best_cost,best_path]


def decode_path(path,indexes):
    way=path[1].copy()
    temp=[]
    for i in way:
        for j in indexes:
            if indexes[j]==i:
                temp.append(j)
                break
    return [path[0],temp]

time=10
ourway=[0]

for i in range(len(arr)):
    paths = all_paths(arr,i)
    path=decode_path(best_path(arr,paths,time),indexes)
    if path[0]>ourway[0]:
        ourway=path.copy()



def find_name_by_id(content,idd):
    for i in content["nodes"]:
        if i["id"]==idd:
            return i["name"]
        
def find_XandY_by_id(content,idd):
    for i in content["nodes"]:
        if i["id"]==idd:
            return str(i["x"])+" "+str(i["y"])


def output(content,path):
    file=open("output.txt","w")
    file.write(str(content["width"])+" "+str(content["height"])+" "+str(len(content["nodes"]))+"\n")
    for i in content["nodes"]:
        file.write(i["name"]+" "+str(i["x"])+" "+str(i["y"])+"\n")
    file.write(str(len(path[1]))+"\n")
    for i in path[1]:
        file.write(find_XandY_by_id(content,i)+" ")
    file.close()

output(content,ourway)
print(ourway)

print("Success!")