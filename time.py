import time
from time import perf_counter

t1_start=perf_counter()
while True:
    time.sleep(1)
    t1_stop=perf_counter()
    print("%.f"%(t1_stop-t1_start))
