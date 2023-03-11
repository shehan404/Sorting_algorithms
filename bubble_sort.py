#this function implement the bubble sort
def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

#enter the array which want to sort here
to_sort=[4,5,6,4,6,8,4,2,1]

print(bubble_sort(to_sort))

