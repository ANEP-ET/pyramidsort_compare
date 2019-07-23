import sys
import os
import time

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
from Pyramid import pyramidize_min

a = [9, 8, 7, 6, 5, 4, 3, 2, 1] # Sorted in reverse order
print("==== Test start ====")
tic = time.process_time()
a_prime = pyramidize_min(a)
toc = time.process_time()
print(a_prime)
print("==== Test end and took {} second(s) ====".format(toc - tic))
