def selection_sort(arr):

    for i in range(len(arr)-1):
        min_index=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

#enter the array which want to sort here
to_sort = [2,3,6,1,10,7,9,4,0,5]

print(selection_sort(to_sort))