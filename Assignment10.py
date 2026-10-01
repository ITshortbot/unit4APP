#apply  numpy to create 1D arry with random numbers and perforn slicing, index and calculae average, mean, median and standard deviation of the array then apply broad casting to the array and perform the same calculations on the new array.
import numpy as np
def create_random_array(size, low, high):
    import numpy as np
    return np.random.randint(low, high, size)
def slice_array(arr, start, end):
    return arr [start:end]
def index_array(arr, index):
    return arr[index]
def calculate_mean(arr):
    return np.mean(arr)
def calculate_median(arr):
    return np.median(arr)
def calculate_std_dev(arr):
    return np.std(arr)
def apply_broadcasting(arr, value):
    return arr + value
def main():
    size = int(input("Enter the size of the array: "))
    low = int(input("Enter the lower bound for random numbers: "))
    high = int(input("Enter the upper bound for random numbers: "))
    arr = create_random_array(size, low, high)
    print(f"Original Array: {arr}")
    
    start = int(input("Enter the start index for slicing: "))
    end = int(input("Enter the end index for slicing: "))
    sliced_arr = slice_array(arr, start, end)
    print(f"Sliced Array: {sliced_arr}")
    
    index = int(input("Enter the index to access in the array: "))
    indexed_value = index_array(arr, index)
    print(f"Value at index {index}: {indexed_value}")
    
    mean = calculate_mean(arr)
    median = calculate_median(arr)
    std_dev = calculate_std_dev(arr)
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
    
    value = int(input("Enter a value to add to each element of the array (broadcasting): "))
    new_arr = apply_broadcasting(arr, value)
    print(f"New Array after Broadcasting: {new_arr}")
    
    new_mean = calculate_mean(new_arr)
    new_median = calculate_median(new_arr)
    new_std_dev = calculate_std_dev(new_arr)
    
    print(f"New Mean: {new_mean}")
    print(f"New Median: {new_median}")
    print(f"New Standard Deviation: {new_std_dev}")


if __name__ == "__main__":
    main()
