#valid anagram

string1 = "silent"
string2 = "listen"

dict1 = {}
dict2 = {}

for i in string1:
    count = 0
    for j in string1:
        if (i == j):
            count += 1
    dict1[i] = count
    
for i in string2:
    count = 0
    for j in string2:
        if (i == j):
            count += 1
    dict2[i] = count   

if (dict1 == dict2):
    print('yes')
else:
    print('no')

#o/p: yes

#Finding duplicate numbers

array = [1,32,4,6,33,6,7,7]
dict1 = {}

for i in array:
    count = 0
    for j in array:
        if (i == j):
            count += 1
    dict1[i] = count
    
for key, value in dict1.items():
    if (value > 1):
        print(key)

#o/p: 6 7 

#hashmapping twosum

array = [1,2,8,8,3,1,4,8,9]
target = 11

seen = {}
count = 0

for i in array:
    if target-i in seen:
        print(target-i,i)
        count += 1
    else:
        count += 1
        seen[i] = count

#o/p: 8 3 , 2 9
