import heapq
import math
import os
import random
import re
import sys

def kth_largest(k, initial_stream):
    # Write your code here
    heapq.heapify(initial_stream)
    print("Ist",initial_stream)

    
    for i in range(len(initial_stream) - k):
        print("Ist",initial_stream)
        heapq.heappop(initial_stream)
        print("2nd",initial_stream) 

    print("Ist",initial_stream)

        


print(kth_largest(3, [5,2,3,4,8]))