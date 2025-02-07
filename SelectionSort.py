#The selectionSort method picks a value and iterates through the list to find its place in the order.
#It does this until the list is in order.
#This method accepts the list A and the length of the list n.
def selectionSort(A, n):

    #Iterate through the list
    for i in range(n):

        #The smallest variable holds the index of the smallest value
        #Initialize the smallest variable with the current index
        smallest = i

        #Iterate through part of the list with indices greater than the current one
        for j in range(i+1, n):

            #If the current value is smaller than the smallest value
            if A[j] < A[smallest]:

                #Set the smallest index to the current one
                smallest = j

        #Initialize a temp variable that holds the current value of index i
        temp = A[i]

        #Set the value of index i to the value of the smallest index
        A[i] = A[smallest]

        #Set the value of index smallest equal to the temp value
        A[smallest] = temp

    #Returns the list
    return A

#Testing of method below this comment

A = [5, 4, 3, 2, 1]

print("Original array: " + str(A))
print("Sorted array using selection sort: " + str(selectionSort(A, len(A))))
