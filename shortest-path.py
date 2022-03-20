#Shortest path for an unweighted undirected graph

def add_edge(list,source,destination):
    list[source].append(destination)
    list[destination].append(source)
    


def SPP(list,s,d):
    dist=0
    pre=[-1 for i in range(len(list))] 
    queue=[s]
    visited=[False for i in range(vertices)]
    while queue:
        q=queue.pop(0)
        visited[q]=True
        for i in list[q]:
            if(visited[i]==False):
                queue.append(i)
                pre[i]=q
        dist+=1
        if d in list[q]: break
    print("Predecessor for each vertice:",pre)
    print("Shortest path distance:",dist)

    #For finding shortest path vertices
    path=[]
    path.append(d)
    #print(path)
    #print(path[0])
    while path[len(path)-1]!=s: 
        path.append(pre[path[len(path)-1]])
    print("Shortest path:",end=" ")
    for i in range(len(path)-1,-1,-1):
        print(path[i],end=" ")


vertices=8
list=[[] for i in range(vertices)]
add_edge(list, 0, 1)
add_edge(list, 0, 3)
add_edge(list, 1, 2)
add_edge(list, 3, 4)
add_edge(list, 3, 7)
add_edge(list, 4, 5)
add_edge(list, 4, 6)
add_edge(list, 4, 7)
add_edge(list, 5, 6)
add_edge(list, 6, 7)

SPP(list,0,7)
#print(list)
