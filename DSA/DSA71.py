# INSERTION o(n**2)
def ins(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and key < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
    print(num)
    
mylist = list(map(int,input("Enter the list elements:").strip().split(" ")))
print(mylist, "\n after sorting!!!!")
ins(mylist)
