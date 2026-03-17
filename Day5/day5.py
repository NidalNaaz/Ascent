#reverse ordered string

string = 'jackhammer jorkins 65'
reverse = '' 
words = string.split()

for i in range (len(words)):
    reverse += words[-i-1] + ' '
    
print(reverse)

#o/p: 65 jorkins jackhammer 

#two sum redo (easier, simplified without repeats)

array = [1,14,12,3,13,2,23,2345,432,10,5,-5,20,0,15]
target = 15

for i in range (len(array)):
    for j in range (i, len(array)):
        if (array[i]+array[j] == target):
            print(array[i],array[j])

#o/p: 1 14, 12 3, 13 2, 10 5, -5 20, 0 1      
