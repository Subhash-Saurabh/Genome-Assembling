#uses python2
from __future__ import print_function
import operator

def eulerian_path(adj,in_degree,out_degree,edge):
    for node,value in in_degree.items():
        if value  != out_degree[node]:
            print(0)
            return

    x = 1
    path = []
    out_edge = {}

    insert_pos = 0
    while edge :

        if insert_pos == 0:
            path.append(x)
        else:
            path.insert(insert_pos,x)
            insert_pos+=1


        if adj[x] != []:

            adj_node = adj[x][0]
            adj[x].remove(adj_node)
            edge -= 1

            out_edge[x] = len(adj[x])

            x = adj_node

            if not edge:
                if insert_pos == 0:
                    path.append(x)
                else:
                    path.insert(insert_pos,x)
                    insert_pos+=1


        else:
            node,value = sorted(out_edge.items(), key=operator.itemgetter(1),reverse = True)[0]
            insert_pos = path.index(int(node))
            x = node
            del path[insert_pos]


    

    print (1)
    for i in path[:-1]:
        print(i,end = " ")



node ,edge = map(int,raw_input().split())

in_degree = {x:0 for x in range(1,1+node)}
out_degree = {x:0 for x in range(1,1+node)}

adj = {}
i = 0
while i < edge:
    u,v = map(int,raw_input().split())
    if u not in adj:
        adj[u] = []
    adj[u].append(v)

    in_degree[v] += 1
    out_degree[u] += 1

    i+=1

eulerian_path(adj,in_degree,out_degree,edge)
