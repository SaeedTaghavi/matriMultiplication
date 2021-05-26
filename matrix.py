# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:27:25 2021

@author: computer
"""

import numpy as np
import time 
import tracemalloc
n=10000
tracemalloc.start()
A = np.random.uniform(0.0,1.0,size=(n,n))
B = np.random.uniform(0.0,1.0,size=(n,n))
t1 = time.time()
C = np.matmul(A, B)
t2 = time.time()
print(t2-t1)


current , peak = tracemalloc.get_traced_memory()
print(f"Current: {current/10**6} MB"  )
print(f"peak: {peak/10**6} MB")