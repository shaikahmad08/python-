nums=[1,2,3,4,5,6]
def myfunc(nums):
    return nums+1
newnum=list(map(myfunc,nums))
print(nums)
print(newnum)


name=['sk']
def func(name):
    return name+'Ahmad'
names=list(map(func,name))
print(name)
print(names)
