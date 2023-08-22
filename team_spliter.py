import random

#input number of candidates 
length = int(input("Number of candidates you have : "))
temp = int(input('Number of members you want in one group : '))
print('Enter names of the candidates : ')
names =[]

#append the input names into a list
for i in range(length):
    input_name = input()
    names.append(input_name)

#function to divide the members into groups 
def group(names,temp):
    random.shuffle(names)
    res=[]
    for i in range(0,len(names),temp):
        res.append(names[i:i+temp])
    return res

#calling group function
Split_group = group(names,temp)

#printing the groups 
for i in range(len(Split_group)):
     print('\n')
     print('Group',i+1,':-')
     print(' ,'.join(Split_group[i]))