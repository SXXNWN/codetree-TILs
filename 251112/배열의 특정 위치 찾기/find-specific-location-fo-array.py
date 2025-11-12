arr = list(map(int , input().split()))
arr_even = arr[1::2]
arr_3 = arr[2::3]



print(f"{sum(arr_even)} {sum(arr_3)/len(arr_3):.1f}") 
