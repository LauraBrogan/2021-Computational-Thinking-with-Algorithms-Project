#CTA Project 2021
#Counting Sort
#Resourse used:https://www.programiz.com/dsa/counting-sort
def countingsort(array):
    size = len(array)
    output = [0] * size

    #Start count array
    count = [0] * 10000

    #Put the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    #Keep cumulative count
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

#Sample array   
array = [2,4,4,8,6,6,2]
#Run counting sort on the sample array
countingsort(array)
#Print array for testing to see results of running counting sort.
print(array)

#Laura Brogan 11/04/2021