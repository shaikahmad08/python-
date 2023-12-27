           #list--its use for CRUD operation
l=[10,20,30,40,40]
print(l)

l.append(50)
print(l)                  #adding last in list 

l.insert(1,10.5)
print(l)                  #adding with indexing num in list

l.reverse()
print(l)                  #in the list value would be reverse

l.remove(10.5)
print(l)                  #remove in the list 

print(l.count(40))        #count in the list value


            #using for and while loop in the list
for l1 in l:
    print(l1)
    
i=0
while i<=len(l)-1:
    print(l[i])
    i=i+1
i=0
while(i<=4):
    print(l[i])
    i=i+1




