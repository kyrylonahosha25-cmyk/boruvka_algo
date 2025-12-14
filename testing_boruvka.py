import random

import time

def Boruvka_with_list(n, graph):

    par = list(range(n + 1))

    mst_w = 0

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

            if set_u != set_v:

                if min_w[set_u] == -1 or graph[min_w[set_u]][2] > w:
                    min_w[set_u] = id
                if min_w[set_v] == -1 or graph[min_w[set_v]][2] > w:
                    min_w[set_v] = id


        for i in range(n):

            curr_id = min_w[i + 1]

            if curr_id != -1:
                rem_u, rem_v, rem_w = graph[curr_id]
                if union_set(rem_u, rem_v):
                    mst_w += rem_w
                    cnt -= 1

    return mst_w


def boruvka_by_matrix_implement(n, matrix):

    par = list( range(n + 1) )
    mst_w = 0
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
        min_edge = {}

        for u in range(n + 1):
            for v in range(u + 1, n + 1):
                w = matrix[u][v]
                if w > 0:
                    set_u = find(u)
                    set_v = find(v)

                    if set_u != set_v:

                        if set_u not in min_edge or min_edge[set_u][2] > w:
                            min_edge[set_u] = (u, v, w)

                        if set_v not in min_edge or min_edge[set_v][2] > w:
                            min_edge[set_v] = (u, v, w)


        for ider in min_edge:
            rem_u, rem_v, rem_w = min_edge[ider]

            if union_set(rem_u, rem_v):

                mst_w += rem_w
                cnt -= 1


    return mst_w

def generate_data(n, delta):

    limit = n * (n - 1) // 2
    needed_cnt = int(delta * limit)

    if needed_cnt < n - 1:
        needed_cnt = n - 1

    edges_set = set()

    nodes = list(range(0, n + 1))
    random.shuffle(nodes)

    for i in range(2, n + 1):
        u = nodes[i]
        v = nodes[random.randint(1, i - 1)]

        edge = tuple(sorted((u, v)))
        edges_set.add(edge)

    while len(edges_set) < needed_cnt:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v:
            edge = tuple(sorted((u, v)))
            if edge not in edges_set:
                edges_set.add(edge)

    INIT = []
    matrix = [[0] * (n + 1) for _ in range(n + 1)]

    for u, v in edges_set:
        w = random.randint(1, 1000)
        INIT.append((u, v, w))
        matrix[u][v] = w
        matrix[v][u] = w

    return INIT, matrix


def run_experiments():

    sizes = [1, 2, 3, 5, 10, 20, 30, 35, 50, 75, 100, 125, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    deltas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98]

    iters = 20

    print(f"{'Кількість вершин':<16} | {'Щільність':<9} | {'Час для списку суміжності':<25} | {'Час для матриці суміжності':<29}")
    print("-" * 45)

    for n in sizes:
        for d in deltas:

            t_list = 0
            t_matrix = 0

            for _ in range(iters):
                INIT, MATRIX = generate_data(n, d)

                start = time.perf_counter()
                Boruvka_with_list(n, INIT)
                t_list += time.perf_counter() - start

                start = time.perf_counter()
                boruvka_by_matrix_implement(n, MATRIX)
                t_matrix += time.perf_counter() - start

            avg_1 = t_list / iters
            avg_2 = t_matrix / iters

            print(f"{n:<5} | {d:<5} | {avg_1:.6f}        | {avg_2:.6f}")

if __name__ == "__main__":
    run_experiments()
