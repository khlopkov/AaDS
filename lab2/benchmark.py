from graph import Graph
import time

COEFF = 10

n = 9900
m = n * n // COEFF

time_start = time.time()
graph = Graph(n, m)
init_time = round((time.time() - time_start) * 1000)
print(init_time)

while n <= 10000:

    print("n: " + str(n))
    time_start = time.time()
    graph.dijktstra_dheap(2, 2)
    exec_time2 = round((time.time() - time_start) * 1000)

    time_start = time.time()
    graph.dijktstra_dheap(3, 2)
    exec_time3 = round((time.time() - time_start) * 1000)

    print("exec time: d=2: " + str(exec_time2) + " d=10: " + str(exec_time3))

    n += 100
    graph.extend(100, COEFF)
