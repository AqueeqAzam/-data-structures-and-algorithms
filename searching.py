#-----------Linear Search-------------
def linear_search(arr, item):
  for i in range(len(arr)):
    if arr[i] == item:
      return i
  return -1

arr = [12, 34, 56, 1, 100, 46]
linear_search(arr, 56)



#----------Binary Search----------------
def binary_search(arr, low, high, item):
  if low <= high:
    # search
    mid = (low + high)//2

    if arr[mid] == item:
      return mid
    elif arr[mid] > item:
      return binary_search(arr, low, mid-1, item)
    else:
      return binary_search(arr, mid+1, high, item)
  else:
    return -1

arr = [12, 45, 76, 3, 23, 54, 0, 90, 89, 67]
print(binary_search(arr, 0, len(arr)-1, 0))
