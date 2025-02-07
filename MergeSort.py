import math as m

##The mergeSort method separates the two parts of a list, puts them in the correct order, and merges them back together.
##This method accepts the list A, the left most index p and the right most index r.
def mergeSort(A, p, r):

    ##If the left index is less than the right index
    if p < r:

        ##Find the middle index
        
        q = (p+r)//2

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

    for i in range(n1 + 1):
        L.append(0)

    R = []

    for i in range(n2 + 1):
        R.append(0)

    for i in range(n1):
        L[i] = A[p + i - 1]

    for j in range(n2):
        R[j] = A[q + j]

    L.append(m.inf)
    R.append(m.inf)

    i = 0

    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A


##Testing of the methods below this comment

A = [5, 4, 3, 2, 1]

print(mergeSort(A, 0, len(A)))
