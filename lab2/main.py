from graph import Graph
import time

n = 10
m = 20

time_start = time.time()
graph = Graph(n, m)

for i in range(n):
    v = graph.adj[i]
    out = str(i) + ": "
    while v is not None:
        out += "[" + str(v.name) + ", " + str(v.weight) + "],"
        v = v.next
    print(out)

heap = graph.dijktstra_dheap(3, 2)

for i in range(n):
    print(str(heap.node[i].name) + ": " + str(heap.node[i].key))