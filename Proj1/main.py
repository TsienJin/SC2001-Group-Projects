# Importing functions for generating and sorting arrays
from test.generateTest import *
from sort.insertSort import *
from sort.mergeSort import *

#Import a timer function to time runtime
import timeit

def main() -> None:
    # pass
    
    # Generate an array
    myArray = GenerateTestData(100)
    print("Unsorted array:\n{}\n".format(myArray.array))
    
    # Insertion Sort on Generated Array
    doInsert = InsertSort(myArray.array)
    timeStartInsertSort = timeit.default_timer()
    doInsert.sort()
    timeStopInsertSort = timeit.default_timer()
    timeRuntimeInsertSort = timeStopInsertSort - timeStartInsertSort
    
    print("The result of Insertion Sort is:\n{}".format(doInsert.array))
    print("Validation check: {}\n"
          "Number of Key comparisons done: {}\n"
          "Number of Swaps done: {}\n"
          "Time Taken: {:.2f} ms"
          .format(myArray.validate(doInsert.array), doInsert.comparison, doInsert.swaps, 1000 * (timeRuntimeInsertSort)))


    # Merge Sort on Generated Array
    # doMerge = MergeSort(myArray.array)
    # doMerge.sort()
    # print("The result of Merge Sort is: {}".format(doMerge.array))
    # print("Validation check: {}".format(myArray.validate(doMerge.array)))



if __name__ == "__main__":
    main()