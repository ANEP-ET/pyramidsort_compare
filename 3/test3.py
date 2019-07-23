import sys
import os
import time

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
from Pyramid import pyramidize_min, status

a = [32.2, 3.14, 2.7, 6.28, 9.9, 1.2, 68.4, 90.1] # Include decimal
print("==== Test start ====")
tic = time.process_time()
a_prime = pyramidize_min(a)
toc = time.process_time()
print(a_prime)
print("The status of pyramid is {}".format(status(a_prime)))
print("==== Test end and took {} second(s) ====".format(toc - tic))
