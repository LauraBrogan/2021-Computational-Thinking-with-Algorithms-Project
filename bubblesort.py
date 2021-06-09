#CTA Project 2021
#Bubble Sort
#Resourse used: https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
def bubblesort(array):
    n = len(array)

    for i in range(n):
        # If there's nothing left to sort terminate the sort function
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

    #return array
#Sample array   
array = [54,26,93,17,77,31,44,55,20]
#Run bubble sort on the sample array
bubblesort(array)
#Print array for testing to see results of running bubble sort.
print(array)

#Laura Brogan 11/04/2021