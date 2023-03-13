def quick_sort(arr):

    if len(arr)<2:
        return arr

    else:
        pivot = len(arr)-1
        j=-1
        for i in range(len(arr)):
            if arr[i]<=arr[pivot] or i==pivot:
                j+=1
                arr[i],arr[j]=arr[j],arr[i]

        left = arr[:j]
        right = arr[j:]
        return quick_sort(left) + quick_sort(right)

#enter the array which want to sort here
to_sort=[2,4,9,3,6,8,5,3]

print(quick_sort(to_sort))