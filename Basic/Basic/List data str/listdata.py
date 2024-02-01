#print num using while and for loop
         #while loop
num=[10,203,3,4,56,3,5,6,55,5]
i=0                               
while i<=9:                     #hard coding
    print(num[i])
    i=i+1
  
  
#whitout hard coding
num=[10,203,3,4,56,3,5,6,55,5]
i=0
while i<=len(num)-1:
    print(num[i])
    i=i+1

#using for loop
num=[10,203,3,4,56,3,5,6,55,5]
for nums in num:
    print(nums)
