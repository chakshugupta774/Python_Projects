len_gth = int(input("Enter the length of your list\n"))
items = []
temp = ''

for i in range(len_gth):
    items.append(input("Enter {} item : ".format(i+1)))

for i in range(len_gth-1):
    temp = temp + items[i] + ", "
temp = temp + 'and ' + items[len_gth-1]
print("The required items is ",temp)
 

