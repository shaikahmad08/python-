    #lambda
myfun=['sk','vamsi','baasha']
myfunc=list(map(lambda x:x+'hello',myfun))
print(myfunc)

#print only first capital letters and reaming small 

myfun = ['sk', 'ahmad', 'baasha']
# using lambda 
myfunc = list(map(lambda myfun: myfun.title(), myfun))
print(myfunc)

#using for loop
for myfun in myfunc:
    print(myfun.title())
    
#using while loop
i=0
while i<=len(myfun)-1:
    print(myfun[i].title())
    i=i+1