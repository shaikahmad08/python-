fp=open('index.txt','r')
data=fp.read()
print(data)
fp.close()

fp=open('index.txt')
data=fp.read(94)
print(data)
fp.close()

fp=open('index.txt')
data=fp.readlines()
print(data)
fp.close()

fp=open('index.txt')
data=fp.readline()
print(data)
fp.close()