#frequency count for string

string = 'mississippi'

dict1 = {}

for i in string:
    count = 0
    
    for j in string:
        
        if (j == i):
            count += 1
    dict1[i] = count
    
    
print(dict1)

#o/p: {'m': 1, 'i': 4, 's': 4, 'p': 2}

#Also, lost a bnch of code after github decided to reset itself after a day of ignoration. Next time in shaa Allah.
