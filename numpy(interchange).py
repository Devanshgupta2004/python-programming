import numpy as np 
nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)
print("\nNew array after swapping first and last columns of the said array:")
new_nums = nums[:, ::-1]
print(new_nums)
