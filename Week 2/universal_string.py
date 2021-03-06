#uses python2
from __future__ import print_function
import operator

def eulerian_path(adj,in_degree,out_degree,edge,first_node):
    for node,value in in_degree.items():
        if value  != out_degree[node]:
            return

    x = first_node
    path = []
    out_edge = {}

    insert_pos = 0
    while edge :
# conditions if we need to insert in path or append
        if insert_pos == 0:
            path.append(x)
        else:
            path.insert(insert_pos,x)
            insert_pos+=1
# to check a path
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
            insert_pos = path.index(node)
            x = node
            del path[insert_pos]

    return path




num = input()
edge = 2**num
edge_list = [ bin(i)[2:].zfill(num) for i in range(edge)]

first_node = edge_list[0][:-1]

in_degree = {}
out_degree = {}

adj = {}

for i in edge_list:
    u,v = i[:-1] , i[1:]
    if u not in adj:
        adj[u] = []
    adj[u].append(v)

    if v in in_degree:
        in_degree[v] += 1
    else:
        in_degree[v] = 1
    if u in out_degree:
        out_degree[u] += 1
    else:
        out_degree[u] = 1

path = eulerian_path(adj,in_degree,out_degree,edge,first_node)
circular_string = path[0]
for i in path[1:]:
    circular_string = circular_string + i[-1]

print(circular_string)
