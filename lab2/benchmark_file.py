import graph
import time

COEFF = 100
INITIAL_N = 100
STEP = 10
Q = 1
R = 1000000

n = INITIAL_N
m = n * n // COEFF

time_start = time.time()
my_graph = graph.init_graph(n, m, Q, R)
init_time = round((time.time() - time_start) * 1000)
print(init_time)

file = open("bench_b.txt", "w")

while n <= 10000:
    my_graph = graph.init_graph(n, m, Q, R)
    print(n)
    file.write(str(n) + '\t')
    time_start = time.time()
    graph.dijkstra_d_heap(my_graph, 2, 2)
    exec_time2 = round((time.time() - time_start) * 1000000)
    file.write(str(exec_time2) + '\t')

    time_start = time.time()
    graph.dijkstra_d_heap(my_graph, 3, 2)
    exec_time3 = round((time.time() - time_start) * 1000000)
    file.write(str(exec_time3) + '\n')
    n += STEP
    m = n * n // COEFF
