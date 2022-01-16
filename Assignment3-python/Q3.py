
n = int(input("enter list length :"))

list = []
list_sort = []

for i in range (n) :
    x = int(input("enter number element :"))
    list.append(x)
    

for i in range (1,n):
    if list[i] < list [i-1]:
        print("No!")
        exit()
        
print("yes!")

