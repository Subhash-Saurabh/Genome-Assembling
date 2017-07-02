#python2

import operator
from collections import deque
def mximal_flow(residue,node,sum_l,edge_list):
    flow = 0

    while 1:
        path , value = bfs(residue,node,edge_list)
        if path == []:
            break

        for route in path:
            edge_list[route][3] -= value
            edge_list[route ^ 1][3] += value

        flow += value

    if flow == sum_l:
        print('YES')
        for edge in range(1,len(edge_list),2):
            u,v,l,c = edge_list[edge]
            if (u != node) and (v != node) and (u != node-1) and (v != node-1):
                print(c + l)
    else:
        print('NO')


def bfs(adj,city,edge_list):
    parent = [[0,None]]
    for i in range(1,city+1):
        parent.append([i,None])

    route = []
    queue = deque([city-1])

    while queue != deque([]) and parent[city][0] == city:
        current = queue.popleft()
        if current in adj:
            for node in adj[current]:
                u,v,l,c = edge_list[node]
                if parent[v][0] == v and v != (city-1) and c != 0:
                    queue.append(v)
                    parent[v] = [current,node]

                    if parent[city][0] != city:
                        break

    lst = []
    min_path = float('inf')
    if parent[city][0] != city:
        min_path = find(parent,city,lst,min_path,edge_list)

    return (lst,min_path)

def find(parent,city,lst,min_path,edge_list):
    if parent[city][0] != city:
        lst.append(parent[city][1])
        u,v,l,c = edge_list[parent[city][1]]
        if c < min_path:
            min_path = c
        min_path = find(parent,parent[city][0],lst,min_path,edge_list)
    return min_path

def main():
    node,edge = map(int,raw_input().split())
    residue = {x:[] for x in range(1,node+3)}
    in_flow = {}
    out_flow = {}
    sum_l = 0
    edge_list = []

    for _ in range(edge):
        u,v,l,c = map(int,raw_input().split())
        sum_l += l
        residue[u].append(len(edge_list))
        edge_list.append([u,v,l,c-l])
        residue[v].append(len(edge_list))
        edge_list.append([v,u,l,0])

        if v in in_flow:
            in_flow[v] += l
        else:
            in_flow[v] = l

        if u in out_flow:
            out_flow[u] += l
        else:
            out_flow[u] = l


    source = node + 1
    sink = node + 2
    for key,value in in_flow.items():
        residue[source].append(len(edge_list))
        edge_list.append([source,key,0,value])
        residue[key].append(len(edge_list))
        edge_list.append([key,source,0,0])

    for key,value in out_flow.items():
        residue[key].append(len(edge_list))
        edge_list.append([key,sink,0,value])
        residue[sink].append(len(edge_list))
        edge_list.append([sink,key,0,0])

    mximal_flow(residue,node+2,sum_l,edge_list)


main()
