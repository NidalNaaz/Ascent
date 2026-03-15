#longest word in a sentence

sentence = 'i hate dirtygoofygoobers on a sunday afternoon.'

words = sentence.split()
maxword = words[0]

for word in words:
    if (len(word) > len(maxword)):
        maxword = word
        
print(maxword)

#o/p: dirtygoofygoobers

#first non repeater alphabet

word = 'dirtygoofygoobers'

for i in word:
    count = 0
    for j in word:
        
        if (j == i):
            count +=1 
            
    if (count == 1):
        print(i)
        break

#o/p: d

#second largest number

array = [2,2,3,67,3,7,9,98,6,5,655,5,87,7,4]
maxn = array[0]
secondmaxn = -99999999999999999999999999

for i in array:
    if (i > maxn):
        secondmaxn = maxn
        maxn = i
    elif (i>secondmaxn):
        secondmaxn = i
        
        
print(secondmaxn)

#o/p: 98
