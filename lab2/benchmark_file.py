from graph import Graph
import time

COEFF = 1
INITIAL_N = 100
STEP = 100

n = INITIAL_N
m = n * n // COEFF

time_start = time.time()
graph = Graph(n, m)
init_time = round((time.time() - time_start) * 1000)
print(init_time)

file = open("bench_b.txt", "w")

while n <= 4000:

    print(n)
    file.write(str(n) + '\t')
    time_start = time.time()
    graph.dijktstra_dheap(2, 2)
    exec_time2 = round((time.time() - time_start) * 1000)
    file.write(str(exec_time2) + '\t')

    time_start = time.time()
    graph.dijktstra_dheap(3, 2)
    exec_time3 = round((time.time() - time_start) * 1000)
    file.write(str(exec_time3) + '\n')
    if n == 1000:
        STEP = 1000
    n += STEP
    graph.extend(STEP, COEFF)
