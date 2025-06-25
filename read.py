f=open('newfile.txt','r')
lines=f.readlines()
print(lines)
'''
for line in lines:
   print(line)
f.close()
'''
f=open('newfile.txt','r')
data = f.read()
print(data)

