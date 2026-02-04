'''
import array
arr = array.array('i', [12,45,78,36])  
print(arr,type(arr))
arr.append(40)
print(arr)
arr.append(12.45)
print(arr)
'''

'''
array : it is collection  of elements of same data type
python dosent support array directly
numpy:
'''
import numpy as np
arr = np.array([10,20,20])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(0))
print(np.ones(5))
print("Even numbers:",np.arange(2,10,2))
print("Odd numbers:",np.arange(1,10,2))
n = int(input("Enter size of array: "))
ele = list(map(int,input("Enter elements: ").split()))
print("Array elements:",np.array(ele))