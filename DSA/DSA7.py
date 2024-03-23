# Ex-7= selection sort and INSERTION

# selection o(n**2)
def sel(num):
    for i in range(len(num)):
        min = i
        for j in range(i + 1, len(num)):
            if num[min] > num[j]:
                min = j
        num[i], num[min] = num[min], num[i]
    print(num)

clist = list(map(int,input("Enter the list elements:").strip().split(" ")))
print(clist, "\n after sorting!!!!")
sel(clist)

