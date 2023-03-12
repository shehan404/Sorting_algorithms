# Sorting Algorithms

Sorting algorithms are used for rearranging items in an array or a list. Selection Sort, Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Counting Sort, Radix Sort are popular sorting algorithms.

In this repository above sorting algorithms have been implemented using python to output the **ascending order**.


## 1. Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly swaps adjacent elements if the first element is greater than the second one from the beginning to the end of the list until it is sorted. 

<img src="images/bubble_sort.gif" width="400" >

### Time complexity
* Best Case - Ω(n)
* Avarage Case - θ(n<sup>2</sup>)
* Worst Case - O(n<sup>2</sup>)

### Space complexity
* Worst Case - O(1)


## 2. Selection Sort

In selection sort smallest element of the unsorted portion is swapped with the first element of the unsorted portion.This process is done repeatedly until whole list is sorted.

<img src="images/selection_sort.gif" width="400" >

### Time complexity
* Best Case - Ω(n<sup>2</sup>)
* Avarage Case - θ(n<sup>2</sup>)
* Worst Case - O(n<sup>2</sup>)

### Space complexity
* Worst Case - O(1)


## 3. Insertion Sort

Array is divided into two parts that sorted and unsorted by considering first element of the array is sorted. Then next element is placed in correct position in the sorted part of the array.

<img src="images/insertion_sort.gif" width="400" >

### Time complexity
* Best Case - Ω(n)
* Avarage Case - θ(n<sup>2</sup>)
* Worst Case - O(n<sup>2</sup>)

### Space complexity
* Worst Case - O(1)


## 4. Merge Sort

Divide and conquer method is used in merge sort algorithm. The unsorted array is divided into small subarrays and then they sorted and merged to obtain sorted array

<img src="images/merge_sort.gif" width="400" >

### Time complexity
* Best Case - Ω(n log(n))
* Avarage Case - θ(n log(n))
* Worst Case - O(n log(n))

### Space complexity
* Worst Case - O(n)