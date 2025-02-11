import math as m

#The mergeSort method separates the two parts of a list, puts them in the correct order, and merges them back together.
#This method accepts the list A, the left most index p and the right most index r.
def mergeSort(A, p, r):

    #If the left index is less than the right index
    if p < r:

        #Find the middle index
        q = (p+r)//2

        #Run the mergeSort again from the left most index to the middle index
        mergeSort(A, p, q)

        #Run the mergeSort again from the middle index plus one to the right most index
        mergeSort(A, q + 1, r)

        #Run the merge method to combine the two sides together
        merge(A, p, q, r)

    #Return the sorted list
    return A

#The merge method puts the sublists back together to form the sorted list
#This method accepts the list A, the left most index p, the middle index q and the right most index r
def merge(A, p, q, r):

    #The size of left side array
    n1 = q - p + 1

    #The size of the right side array
    n2 = r - q

    #Creating the left side array
    L = []

    for i in range(n1):
        L.append(0)

    # Creating the right side array
    R = []

    for j in range(n2):
        R.append(0)

    #Loop through the left side array
    for i in range(n1):

        #Assign the left side values of the array to the left array
        L[i] = A[p + i]

    #Loop through the right side array
    for j in range(n2):

        #Assign the right side values of the array to the right array
        R[j] = A[q + j + 1]

    #Add infinity to the end of the left side array to mark the end of the array
    L.append(m.inf)

    #Add infinity to the end of the right side array to mark the end of the array
    R.append(m.inf)

    #Set the initial indices for the merge
    i = 0
    j = 0

    #For the length of the array
    for k in range(p, r + 1):

        #Check to see if the value in the left side array is less than or equal to the right side
        if L[i] <= R[j]:

            #If it is less than

            #Set current index of A equal to the value of L at i
            A[k] = L[i]

            #Add one to i
            i += 1

        #Otherwise
        else:

            #Set the current index of A equal to the value of R at j
            A[k] = R[j]

            #Add one to j
            j += 1

    #The left side and the right side have been merged

    #Return the array
    return A


#Testing of the methods below this comment

A = [5, 4, 3, 2, 1]

print("Original array: " + str(A))
print("Sorted array using merge sort: " + str(mergeSort(A, 0, len(A)-1)))
