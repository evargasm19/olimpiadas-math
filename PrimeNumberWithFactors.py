'''
Created on Apr 29, 2023

@author: Edwin
'''
x=5
z=1
factor=[]
for y in range(1,x+1) :
        
    if x % y == 0 :
        factor=factor+[y]
        
    else : z=z+1
print('factors of ' + str(x) + ' : ' + str(factor))    

if 2==len(factor) :
    print(str(x) + ' is a Beatiful PRIME number')
else : 
    
    print(str(x) + ' NO ES Pr')
