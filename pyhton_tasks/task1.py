def find_missing_number(arr: list):
    n = len(arr)            # length of the array
    total_sum = n * (n + 1) // 2  # sum of n natural numbers
    array_sum = sum(arr)
    return total_sum - array_sum 


arr = [3, 0, 1]
print(find_missing_number(arr)) 

arr1=[0,1,2,3,4,5,6,7,9,10]
print(find_missing_number(arr1))