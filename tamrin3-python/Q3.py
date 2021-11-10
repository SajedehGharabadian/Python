
n = int(input("enter list length :"))

list = []
list_sort = []

for i in range (n) :
    x = int(input("enter number element :"))
    list.append(x)
    list_sort.append(x)

list_sort.sort()


if (list == list_sort) :
    print("list is sorted!")
else :
    print("list is not sorted")

