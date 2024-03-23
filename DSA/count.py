def counting_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    range_of_elements = max_num - min_num + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count occurrences of each element in the input array
    for i in range(len(arr)):
        count[arr[i] - min_num] += 1

    # Modify the count array to store the position of each element in the sorted output
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array based on the modified count array
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i] - min_num] - 1] = arr[i]
        count[arr[i] - min_num] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array:", arr)

counting_sort(arr)
print("Sorted array:", arr)
