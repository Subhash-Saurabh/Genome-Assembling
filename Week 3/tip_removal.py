#python2
def solve(edge_list):
    pot_tip = {}
    total = 0
    graph,rev_graph,in_degree,out_degree = main(edge_list)

    for i in out_degree:
        if (in_degree[i] == 0 and out_degree[i] == 1) or (in_degree[i] == 1 and out_degree[i] == 0):
            pot_tip[i] = (in_degree[i],out_degree[i])


    while pot_tip != {}:
        key,value = pot_tip.popitem()
        in_val,out_val = value

        if in_val == 0:
            total += 1
            back = list(graph[key].keys())[0]
            del graph[key][back]
            del rev_graph[back][key]
            in_degree[back] -= 1
            out_degree[key] -= 1
            if in_degree[back] == 0 and out_degree[back] == 1:
                pot_tip[back] = (in_degree[back],out_degree[back])

        elif out_val == 0:
            total += 1
            back = list(rev_graph[key].keys())[0]
            del rev_graph[key][back]
            del graph[back][key]
            out_degree[back] -= 1
            in_degree[key] -= 1
            if in_degree[back] == 1 and out_degree[back] == 0:
                pot_tip[back] = (in_degree[back],out_degree[back])

    print(total)


def test_k_mer(fname,length = 15):
    edge_list = []


    with open(fname) as f:
        for read in f:
            read = read.strip()
            for j in range(0,len(read)-length+1):
                if read[j:j+length] not in edge_list:
                    edge_list.append(read[j:j+length])

    return edge_list



def k_mer_generate(length = 15):
    edge_list = []

    try:
        while 1:
            read = raw_input()
            for j in range(0,len(read)-length+1):
                if read[j:j+length] not in edge_list:
                    edge_list.append(read[j:j+length])
    except EOFError:
        pass

    return edge_list


def main(edge_list):
    graph = {}
    rev_graph={}

    in_degree = {}
    out_degree = {}


    for i in edge_list:
        u,v = i[:-1] ,i[1:]

        if u not in graph:
            graph[u] = {}
        graph[u][v] = 0
        if v not in rev_graph:
            rev_graph[v] = {}
        rev_graph[v][u] = 0


        if v in in_degree and v in out_degree:
            in_degree[v] += 1
        elif v not in in_degree and v in out_degree:
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

    return graph,rev_graph,in_degree,out_degree


edge_list = k_mer_generate()
solve(edge_list)
