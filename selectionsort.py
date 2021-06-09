#CTA Project 2021
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
#Sample array
#arr = [6,2,51,69,46,63,69]
arr = [19,52,78,10,46,32,31,26,78]
#Run selection sort on the sample array
selectionsort(arr)

#Print array for testing to see results of running selection sort.
print(arr)  
#Laura Brogan 10/04/2021

