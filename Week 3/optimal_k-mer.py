#uses python2
from __future__ import print_function
import operator

def single_eulerian_path(in_degree,out_degree):
    for node,value in in_degree.items():
        if value  != out_degree[node] or value != 1:
            return 0
    return 1

def k_mer_generate(read,length):
    edge_list = []
    for i in read:
        for j in range(0,len(i)-length+1):
            if i[j:j+length] not in edge_list:
                edge_list.append(i[j:j+length])
    return edge_list

def main(edge_list):

    in_degree = {}
    out_degree = {}


    for i in edge_list:
        u,v = i[:-1] ,i[1:]
        if u == v:
            continue
        if v in in_degree and v in out_degree:
            in_degree[v] += 1
        elif v not in in_degree and v  in out_degree:
            in_degree[v] = 1
        elif v in in_degree and v not in out_degree:
            in_degree[v] += 1
            out_degree[v] = 0
        elif v not in in_degree and v not in out_degree:
            in_degree[v] = 1
            out_degree[v] = 0

        if u in in_degree and u in out_degree:
            out_degree[u] += 1
        elif u in in_degree and u not in out_degree:
            out_degree[u] = 1
        elif u not in in_degree and u in out_degree:
            out_degree[u] += 1
            in_degree[u] = 0
        elif u not in in_degree and u not in out_degree :
            out_degree[u] = 1
            in_degree[u] = 0

    return in_degree,out_degree


length = 4
read = [raw_input() for i in range(5)]
edge_list = k_mer_generate(read,length)


in_degree,out_degree = main(edge_list)
val = single_eulerian_path(in_degree,out_degree)

while val == 0 and length > 0:
    length-=1
    edge_list = k_mer_generate(read,length)
    in_degree,out_degree = main(edge_list)
    val = single_eulerian_path(in_degree,out_degree)

if length > 0:
    print (length)

