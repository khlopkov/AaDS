import graph

n = 10
m = 20
q = 1
r = 10

my_graph = graph.init_graph(n, m, q, r)

heap = graph.dijkstra_d_heap(my_graph, 2, 2)

for i in range(0, len(my_graph)):
    out = str(i) + ": "
    p = my_graph[i]
    while p is not None:
        out += "["
        out += str(p.name) + ", " + str(p.weight)
        out += "]"
        p = p.next
    print(out)

for i in heap.index:
    out = str(heap.node[i].name) + ": "
    out += str(heap.node[i].key)
    print(out)


