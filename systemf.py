import sys

args = sys.argv[1:]
for i in args:
    filename = i
    f=open(filename,'r')
    data = f.read()
print(data)