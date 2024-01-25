fp=open('index1.txt','r')
data=fp.read()
print(data)
fp.close()

fp=open('index1.txt')
data=fp.readlines()
print(data)
fp.close()