import random

def Boruvka(n, graph):

    par = list(range(n + 1))

    mst_w = 0
    mst_graph = []

    cnt = n

    def find(i):
        if par[i] == i:
            return i

        par[i] = find(par[i])
        return par[i]

    def union_set(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            par[a] = b
            return True
        else:
            return False

    while cnt > 1:
        min_w = [-1] * (n + 1)

        for id, (u, v, w) in enumerate(graph):
            set_u = find(u)
            set_v = find(v)

            one_comp:bool = (set_u != set_v)

            if one_comp == True:
                if min_w[u] == -1 or graph[min_w[set_u] ][2] > w:
                    min_w[u] = id
                if min_w[v] == -1 or graph[min_w[set_v] ][2] > w:
                    min_w[v] = id


        for i in range(n):
            curr_id = min_w[i + 1]

            if curr_id != -1:
                rem_u, rem_v, rem_w = graph[curr_id]

                if union_set(rem_u, rem_v) != False:
                    mst_w = mst_w + rem_w
                    mst_graph.append((rem_u, rem_v, rem_w) )
                    cnt = cnt - 1

    return mst_w, mst_graph





N = int(input() )

M = int(input() )

INIT = []

for i in range(M):
    v, u, w = map(int, input().split() )

    spisok = (v, u, w)

    INIT.append(spisok)

w, mst = Boruvka(N, INIT)

print(w)

for i in mst:
    print(i[0], i[1], i[2])



