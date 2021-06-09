#CTA Project 2021
#Merge Sort
#Resourse used:https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html

def mergesort(array):
    #print is used in testing to see the breakdown of sorting process
    print("Splitting ",array)
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
    print("Merging ",array)
#Sample array
array = [54,26,93,17,77,31,44,55,20]
#Run merge sort on the sample array
mergesort(array)
#Print array for testing to see results of running merge sort.
print(array)
#Laura Brogan 11/04/2021