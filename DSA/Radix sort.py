def counting_sort(arr, num):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // num
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // num
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    num = 1

    while max_num // num > 0:
        counting_sort(arr, num)
        num *= 10

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)

radix_sort(arr)
print("Sorted array:", arr)
