#CTA Project 2021 - Laura Brogan
#BENCHMARKING
#Resourses used:https://github.com/NiamhOL/Computational-Thinking-with-Algorithms-Project-2020/blob/master/CTA%20Project%20python.py
              #:https://github.com/shkyler/gmit-cta-project/blob/master/project.py

#This programe can run for a long time give warning to user.
print("Programe in Progress.....")

#Import libraries required for the project
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Defining 5 Sorting Algorithms
#Selection Sort
#Resourse used: https://stackabuse.com/selection-sort-in-python/
def selectionsort(arr):
    # i is the amount of items to be sorted
    for i in range(len(arr)-1):
        #Start with the first item in the array and assume it is the lowest 
        min_index = i
        # J is used to loop thorugh the ramaining items in the array.
        for j in range(i+1, len(arr)-1):
            #If  a lower item is found than that of min_index above min_index is updated
            if arr[j] < arr[min_index]:
                min_index = j
        #When the lowest item of the array is found swap it with the first item in the arrary
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return(arr)


#Quick Sort
#Resourse used: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html
def quicksort(array):
    # This is calling a recursive function that takes in the array
   quicksorthelper(array,0,len(array)-1)

#This function helps with the sorting process, if the first items is < 1  the item is sorted if not it partitions the array and recursively sorts. 
def quicksorthelper(array,first,last):
   if first<last:
       #finding where to split the array
       splitpoint = partition(array,first,last)
       #call the function on the two halfs of the array
       quicksorthelper(array,first,splitpoint-1)
       quicksorthelper(array,splitpoint+1,last)

#Function using pivot element to partition the array.
def partition(array,first,last):
   pivotvalue = array[first]
#This function takes the first element as pivot, places the pivot element at the correct position in sorted array and places all higher
#than the pivot to the left of the pivot and all smaller elememts to right of the pivot. 
   leftmark = first+1
   rightmark = last

   done = False
   while not done:
#Moving the first point right until the first element is greater pivot is found.
       while leftmark <= rightmark and array[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
#Moving the second point right until the first element is less than pivot.
       while array[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
#Stop when when cross over occurs 
       if rightmark < leftmark:
           done = True
          #Swap the values that are out of place 
       else:
           temp = array[leftmark]
           array[leftmark] = array[rightmark]
           array[rightmark] = temp
 #Swap with the pivot value 
   temp = array[first]
   array[first] = array[rightmark]
   array[rightmark] = temp


   return rightmark
   #return array


#Counting sort  
#Resourse used:https://www.programiz.com/dsa/counting-sort
def countingsort(array):
    size = len(array)
    output = [0] * size

    #Start count array
    count = [0] * 10000

    #Put the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    #Keep cummulative count
    for i in range(1, 10000):
        count[i] += count[i - 1]

    #Find the index of each element of the original array in count array
    #place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    #Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

    return(array)


#Bubble Sort
#Resourse used: https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
def bubblesort(array):
    n = len(array)

    for i in range(n):
        #If there's nothing left to sort terminate the sort function
        already_sorted = True
        #Look at each item of the list one by one and compare it to the adjacent item.
        #Each iteration reduces the amount of the array that is looked at as the remaining itens are already sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                #If the item you are looking at is larger than the adjacent value then they are swaped.
                array[j], array[j + 1] = array[j + 1], array[j]

                #As swaping two elements, mark already_sorted to false so the algorithm doesn't finish prematurely.
                already_sorted = False

        #If no swaps in the last iteration the array is already sorted and can be terminated.
        if already_sorted:
            break

    return array

#Merge sort 
#Resourse used:https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
def mergesort(array):
    #print is used in testing to see the breakdown of sorting process
    #print("Splitting ",array)
    #This recursive algorithm splits the list in half
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]
    
        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        #It continues to divide the array until each item is individual 
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1
    #Once it is divided it is them merged into the correct order as it look at each individual sub array
        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
    #print is used in testing to see the breakdown of sorting process
    #print("Merging ",array)
    return (array)


#Functions to benchmark the algorithms

#Create a function to be used for generating the test arrays
def array_create(size):
  #return the array of the selected size
  return [np.random.randint(1000) for i in range(size)]

#Defining a function that takes an array and a sorting algorithm and times how long it takes to run
def timer(input_array,sort_algo):
  start = time.time()
  sort_algo(input_array)
  end = time.time()
  return (end-start)

#Defines a function to calculate the average running time of a sorting algorithm
def average_time(num_runs, size, sort_algo):
  #use an array to store the results of each trial
  trial_times = []
  #use a while loop to run the algorithm the specified number of times 
  counter = 0
  while counter < num_runs:
    input_array = array_create(size)
    trial_times.append(timer(input_array,sort_algo))
    counter = counter + 1
  #return the average time it takes to run the algorithm  
  return (sum(trial_times)/len(trial_times))

#Formatting the output

#create a function to carry out the trials
def algo_trial(algo, test_size):
  #this function takes each algorithm and test size and returns the average result of 10 trials in ms - formatted to 3 decimal places
  #on each algorithm
  return float("{:10.3f}".format(average_time(10,test_size,algo)*1000))

#create a columns
#pass a list of sorting algorithms and a test size
def col_create(algos, test_size):  
  #the algorithm will test each algorthim for a given test size ..
  col = []
  for i in algos:
    col.append(algo_trial(i, test_size))
  #Return a list of results  
  return(col)  

#Defining a function that creates a pandas dataframe based on a data dictionary passed to it
def df_create(data_dict):
  #create the data frame, set the index to the "size" field and return the dataframe
  data = pd.DataFrame(data_dict)
  data.set_index("size",inplace=True)
  return data

#Defining a function that creates a pandas dataframe and plots the results based on the data dictionary,
#Dest input sizes and sorting algorithms passed to it
def results_plot(data_dict, test_size, sort_algos):
  #create a pandas dataframe based on the data passed to it
  data = df_create(data_dict)
  #loop through the list of test sizes
  for i in range(len(sorts)):
    plt.plot(test_size, data.iloc[i], label=sort_algos[i])
  plt.xlabel("Input Size, n")  
  plt.ylabel("Average Running Time, milliseconds")
  plt.title ("Benchmarking Sorting Algorithms")
  plt.legend()
  plt.show()

#User Interface  
#create a list of the sorting algorithms to be tested
#sorts is used to index the data frame
sorts = ['Selection Sort', 'Quick Sort', 'Counting Sort', 'Bubble Sort', 'Merge Sort']
#algorithms is the list of the function names
algorithms = [selectionsort, quicksort, countingsort, bubblesort, mergesort]
#n_trial is a list of input sizes to be tested
n_trial = [100,250,500,750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
#trial is a data dictionary used to create the columns for the pandas dataframe
trial = {"size":sorts, "100":col_create(algorithms,100), "250":col_create(algorithms,250),"500":col_create(algorithms,500),"750":col_create(algorithms,750), "1000":col_create(algorithms,1000),"1250":col_create(algorithms,1250),"2500":col_create(algorithms,2500), "3750":col_create(algorithms,3750), "5000":col_create(algorithms,5000), "6250":col_create(algorithms,6250), "7500":col_create(algorithms,7500), "8750":col_create(algorithms,8750), "10000":col_create(algorithms,10000)}

#the main() function is the users interface 
def main():
  #The user can select 1 of 3 options graph/table/quit
  allowed_modes = ["graph", "table","quit"]
  mode_chosen = input("How would you like to view the benchmark test? - graph/table/quit   ")
  #use a while loop to check the user input
  while mode_chosen not in allowed_modes:
    mode_chosen = input("How would you like to view the benchmark test? - graph/table/quit   ")
  #use conditional to decide which functions to call based on user input
  if mode_chosen == "graph":
    results_plot(trial, n_trial, sorts)
    main()
  elif mode_chosen == "table":  
    print(df_create(trial).to_string())
    main()
 
  else:
    quit()
      
print()
main()
#Laura Brogan 01/05/2021