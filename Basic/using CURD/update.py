#update

# num=[10,20,30,40,50]
# 
# #using append
# num.append(60)
# print(num)
# 
# #using insert
# num.insert(1,15)
# print(num)

#using extend
num=[10,20,30,40,50]
num2=[60,12,10,45,33]
num.extend(num2)
num2.extend(num)
print(num)
print(num2)

#using sort
l=[190,3,43,24,42]
l.sort()
print(l)

#using count
num=[10,20,30,30,40,50]
print(num.count(30))

#using reverse
num=[10,20,30,30,40,50]
num.reverse()
print(num)

