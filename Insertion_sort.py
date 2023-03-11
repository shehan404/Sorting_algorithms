def insertion_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j]<arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
                i-=1
            else:
                break
    return arr


#enter the array which want to sort here
to_sort = [4,1,6,3,6,8,9,2,12]

print(insertion_sort(to_sort))