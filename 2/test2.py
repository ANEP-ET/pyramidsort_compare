import sys
import os
import time

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
from Pyramid import pyramidize_min

a = [1, 3, 2, 8, 7, 6, 5, 10, 9, 8, 7, 6, 6, 5, 5, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91] # Minimum heap
print("==== Test start ====")
tic = time.process_time()
a_prime = pyramidize_min(a)
toc = time.process_time()
print(a_prime)
print("==== Test end and took {} second(s) ====".format(toc - tic))
