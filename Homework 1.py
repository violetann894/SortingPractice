import math as m

##The selectionSort method picks a value and iterates through the list to find its place in the order.
##It does this until the list is in order. 
##This method accepts the list A and the length of the list n.
def selectionSort(A, n):

    ##Iterate through the list
    for i in range(n):

        ##The smallest variable holds the index of the smallest value
        ##Initialize the smallest variable with the current index
        smallest = i

        ##Iterate through part of the list with indicies greater than the current one
        for j in range(i+1, n):

            ##If the current value is smaller than the smallest value
            if A[j] < A[smallest]:

                ##Set the smallest index to the current one
                smallest = j

        ##Initialize a temp variable that holds the current value of index i
        temp = A[i]

        ##Set the value of index i to the value of the smallest index
        A[i] = A[smallest]

        ##Set the value of index smallest equal to the temp value
        A[smallest] = temp

    ##Returns the list
    return A


##The mergeSort method seperates the two parts of a list, puts them in the correct order, and merges them back together.
##This method accepts the list A, the left most index p and the right most index r.
def mergeSort(A, p, r):

    ##If the left index is less than the right index
    if p < r:

        ##Find the middle index
        q = m.ceil((p+r)/2) - 1

        ##Run the mergeSort again from the left most index to the middle index
        mergeSort(A, p, q)

        ##Run the mergeSort again from the middle index plus one to the right most index 
        mergeSort(A, q + 1, r)

        ##Run the merge method to combine the two sides together
        merge(A, p, q, r) 

    ##Return the sorted list
    return A

##The merge method puts all the sublists back together to form the sorted list
##This method accepts the list A, the left most index p, the middle index q and the right most index r
def merge(A, p, q, r):

    n1 = q - p + 1

    n2 = r - q

    L = []

    for i in range(n1 + 2):
        L.append(0)

    R = []

    for i in range(n2 + 2):
        R.append(0)

    L[n1 + 1] = m.inf

    R[n2 + 1] = m.inf

    for i in range(n1):
        L[i] = A[p + i -1]

    for j in range(n2):
        R[j] = A[q+j]

    i = 0

    j = 0

    for k in range(p, r - 4):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A


##Testing of the methods below this comment

A = [5, 4, 3, 2, 1]

print(selectionSort(A, len(A)))
print(mergeSort(A, 0, len(A)))
