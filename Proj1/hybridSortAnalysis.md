# Hybrid Sort Analysis 

**Insertion Sort** Time Complexity 
<br> Best case: **O(n)**
<br>Worst case: **O(n^2)**

**Merge Sort** Time Complexity 
<br> Best case: **O(nlog(n))**
<br> Worst case: **O(nlog(n))**

**Hybrid Sort** Time Complexity 
<br> Best case: **O(n + nlog(n/k))** , where k is the threshold number, which is the maximum size of subarray to switch to insertion sort  
Worst case: **O(nk + nlog(n/k)** 

## Analysis 
Insertion sort runs faster at subarray of smaller size as its swapping mechanism has cheaper/lesser operations per iteration. To determine the best threshold to switch to insertion sort, we have to plot the graph of insertion sort and merge sort to see at how many n does insertion sort run better than merge sort. 
