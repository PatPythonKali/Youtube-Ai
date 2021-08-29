import time
import numpy as np

start = time.time()
arr = np.array(range(1000000))
lst = range(1000000)

for x in lst:
    print(x)

end = time.time()
print(f"Execution time is {round(end - start, 2)}")