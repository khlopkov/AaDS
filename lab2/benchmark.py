import graph
import time

COEFF = 10
STEP = 100

n = 100
m = n * n // COEFF
Q = 1
R = 1000000


while n <= 10000:
    time_start = time.time()
    my_graph = graph.init_graph(n, m, Q, R)
    init_time = round((time.time() - time_start) * 1000)
    print("n: " + str(n))
    print("init time:" + str(init_time))

    time_start = time.time()
    graph.dijkstra_d_heap(my_graph, 2, 2)
    exec_time2 = round((time.time() - time_start) * 1000)

    time_start = time.time()
    graph.dijkstra_d_heap(my_graph, 3, 2)
    exec_time3 = round((time.time() - time_start) * 1000)

    print("exec time: d=2: " + str(exec_time2) + " d=3: " + str(exec_time3))

    n += STEP
    m = n * n // COEFF
