# Hybrid Sort Analysis 

**Insertion Sort** Time Complexity 
Best case: **O(n)**
Worst case: **O(n^2)**

**Merge Sort** Time Complexity 
Best case: **O(nlog(n))**
Worst case: **O(nlog(n))**

**Hybrid Sort** Time Complexity 
Best case: **O(n + nlog(n/k))** where k is the threshold number, which is the maximum size of subarray to switch to insertion sort  
Worst case: **O(nk + nlog(n/k)** 

Insertion sort runs faster at subarray of smaller size as its swapping mechanism has cheaper/lesser operations per iteration. To determine the best threshold to switch to insertion sort, we have to plot the graph of insertion sort and merge sort to see at how many n does insertion sort run better than merge sort. 
