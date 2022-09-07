# Importing functions for generating and sorting arrays
from test.generateTest import *
from sort.insertSort import *
from sort.mergeSort import *

#Import a timer function to time runtime
import timeit

def main() -> None:
    # pass
    
    # Generate an array
    # myArray = GenerateTestData(100)
    # print("Unsorted array:\n{}\n".format(myArray.array))
    
    # Insertion Sort on Generated Array
    # doInsert = InsertSort(myArray.array)
    # timeStartInsertSort = timeit.default_timer()
    # doInsert.insertionSort()
    # timeStopInsertSort = timeit.default_timer()
    # timeRuntimeInsertSort = timeStopInsertSort - timeStartInsertSort
    
    # print("The result of Insertion Sort is:\n{}".format(doInsert.array))
    # print("Validation check: {}\n"
    #       "Number of Key comparisons done: {}\n"
    #       "Number of Swaps done: {}\n"
    #       "Time Taken: {:.2f} ms"
    #       .format(myArray.validate(doInsert.array), doInsert.comparison, doInsert.swaps, 1000 * (timeRuntimeInsertSort)))


    # Merge Sort on Generated Array
    # doMerge = MergeSort(myArray.array)
    # doMerge.sort()
    # print("The result of Merge Sort is: {}".format(doMerge.array))
    # print("Validation check: {}".format(myArray.validate(doMerge.array)))

    #DO INSERTION SORT AND PUT IN CSV FILE
    
    result = open("Proj1/result/result.csv", "w") # Overwrites file if exist, else creates new file
    result.write("Size of Array, Insertion Sort Time (ms), Merge Sort Time (ms), Hybrid Sort Time (ms)\n")
    result.close()
    
    # for i in range(1000, 1010000, 10000):
    for i in range(10, 11, 100):
        testData = GenerateTestData(i)
        
        doInsert = InsertSort(testData.array)
        timeStartInsertSort = timeit.default_timer()
        doInsert.insertionSort()
        timeStopInsertSort = timeit.default_timer()
        timeRuntimeInsertSort = 1000 * (timeStopInsertSort - timeStartInsertSort)
        print("{} Validation: {}\n".format(doInsert.name, testData.validate(doInsert.array)))
        
        doMerge = MergeSort(testData.array)
        timeStartMergeSort = timeit.default_timer()
        doMerge.mergeSort(0, len(doMerge.array))
        timeStopMergeSort = timeit.default_timer()
        timeRuntimeMergeSort = 1000 * (timeStopMergeSort - timeStartMergeSort)
        print("{} Validation: {}\n".format(doMerge.name, testData.validate(doMerge.array)))
        print("Merge Sort array:\n{}".format(doMerge.array))
        
        
        # print("The result of Insertion Sort is:\n{}".format(doInsert.array))
        # print("Validation check: {}\n"
        #     "Number of Key comparisons done: {}\n"
        #     "Number of Swaps done: {}\n"
        #     "Time Taken: {:.2f} ms"
        #     .format(testData.validate(doInsert.array), doInsert.comparison, doInsert.swaps, timeRuntimeInsertSort))
        
        result = open("Proj1/result/result.csv", "a") # Writes the result to result.csv
        result.write("{}, {:.2f}, {:.2f}, {:.2f}\n".format(i, timeRuntimeInsertSort, timeRuntimeMergeSort, 100))
        result.close()


if __name__ == "__main__":
    main()