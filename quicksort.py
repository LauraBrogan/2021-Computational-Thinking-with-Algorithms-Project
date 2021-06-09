#CTA Project 2021
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
#sample array
array = [54,26,93,17,77,31,44,55,20]
#Run quick sort on the sample array
quicksort(array)
#Print array for testing to see results of running quick sort.
print(array)
#Laura Brogan 10/04/2021


