class Node(object):
    def __init__(self,value):
        self.value=value
        self.edges=[]
        self.visited=False

class Edge(object):
    def __init__(self,value,node_from,node_to):
        self.value=value
        self.node_from=node_from
        self.node_to=node_to
        
class Graph(object):
    def __init__(self,nodes=[],edges=[]):
        self.nodes=nodes
        self.edges=edges
        self.node_map={}
        
    def insert_Node(self,new_node_val):
        new_node=Node(new_node_val)
        self.nodes.append(new_node)
        self.node_map[new_node_val]=new_node
        
    
    def insert_edge(self,new_edge_val,node_from_val,node_to_val):
        node_from_found=None
        node_to_found=None
        for node in self.nodes:
            if node_from_val==node.value:
                node_from_found=node
            if node_to_val==node.value:
                node_to_found=node
        if(node_from_found==None):
            node_from_found=Node(node_from_val)
            self.nodes.append(node_from_found)
            self.node_map[node_from_val]=node_from_found
        if(node_to_found==None):
            node_to_found=Node(node_to_val)
            self.nodes.append(node_to_found)
            self.node_map[node_to_val]=node_to_found
        new_edge=Edge(new_edge_val,node_from_found,node_to_found)
        node_from_found.edges.append(new_edge)
        node_to_found.edges.append(new_edge)
        self.edges.append(new_edge)
    
    def get_Edge_list(self):
        list=[]
        for edge in self.edges:
            list.append((edge.value,edge.node_from.value,edge.node_to.value))
        return list
        
    def get_adjacency_list(self):
        list=[]
        max_node=self.find_max_node_val()
        #print(max_node)
        list=[None]*(max_node+1)
        #print(list)
        for edge in self.edges:
            if not list[edge.node_from.value]:
                list[edge.node_from.value]=[(edge.value,edge.node_to.value)]
            else:
                list[edge.node_from.value].append((edge.value,edge.node_to.value))
        return list
        
    def get_adjacency_matrix(self):
        list=[]
        max_node=self.find_max_node_val()
        list=[[0 for i in range(max_node+1)] for j in range(max_node+1)]
        for edge in self.edges:
                list[edge.node_from.value][edge.node_to.value]=edge.value
        return list
        
            
    def find_max_node_val(self):
        max_node=-1
        #print(self.nodes)
        if(len(self.nodes)):
            for node in self.nodes:
                if(node.value>max_node):
                    max_node=node.value
        return max_node
        
    def DFSr(self,start_node_val):
        self.clear_visited()
        start_node=self.node_map.get(start_node_val)
        #print(start_node.value)
        return self.dfs_helper(start_node)
        
    def dfs_helper(self,start_node):
        list=[start_node.value]
        start_node.visited=True
        for edge in self.edges:
            if(edge.node_from.value==start_node.value and edge.node_to.visited==False):
                list.extend(self.dfs_helper(edge.node_to))
        return list
        
    def BFSq(self,start_node_val):
        list=[]
        node=self.node_map[start_node_val]
        
        self.clear_visited()
        queue=[node]
        node.visited=True
        while queue:
            node=queue.pop(0)
            list.append(node.value)
            #print(list)
            for e in node.edges:
                if(e.node_from.value==node.value and  (not e.node_to.visited)):
                    e.node_to.visited=True
                    queue.append(e.node_to)
            #print(queue)
        return list
        
    def clear_visited(self):
        for node in self.nodes:
            node.visited=False
            
    
        

graph=Graph()
graph.insert_edge(51, 0, 1)     # MV <-> SF
graph.insert_edge(51, 1, 0)     # SF <-> MV
graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
graph.insert_edge(932, 2, 4)    # London <-> Berlin
graph.insert_edge(932, 4, 2)    # Berlin <-> London
graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London
print("Edge list\n",graph.get_Edge_list())
print("Adjacency list\n",graph.get_adjacency_list())
print("Adjacency matrix\n",graph.get_adjacency_matrix())
print("DFSr\n",graph.DFSr(2))
print("BFSq\n",graph.BFSq(2))
