import json

f=open("graph.json","r")
content=json.load(f)

print(content['nodes'])
def create_matrix(content):
    arr=[]
    for i in range(len(content['nodes'])):
        lst=[]
        for j in range(len(content['nodes'])):
            lst.append(0)
        arr.append(lst)
    
#    for i in content['nodes']:
#        arr[i['id']-1][i['id']-1]=i['cost']
        
    for i in content['edges']:
        arr[i['from_id']-1][i['to_id']-1]=1
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

def all_paths(arr,node=0,lst=[],main_lst=[]):
    temp_lst=lst.copy()
    temp_lst.append(node)
    children=find_children(arr,node)
    if len(children)==0:
        main_lst.append(temp_lst)
    for i in children:
        all_paths(arr,i,temp_lst,main_lst)
    return main_lst
    
arr=create_matrix(content)
pprint(arr)
print(all_paths(arr,0))
#print(find_children(arr,0))