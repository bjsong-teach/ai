def is_add(number):
    if number%2:
        return '홀수입니다.'
    else:
        return '짝수입니다.'
    
def avg_numbers(*args):
    result =0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))
'''
input1 = input('첫번째 숫자를 입력하세요.')
input2 = input('두번째 숫자를 입력하세요.')
total = int(input1)+int(input2)
total = int(input1+input2)
'''
print("you", "need", "love")

f1= open("newfile1.txt", 'w')
f1.write("Life is too Short!!!!!")
f1 = open("newfile1.txt", 'r')
data = f1.read()
print(data)

f=open('test.txt','w')
f.write('Life is too Short!!!!!\nYou need Java')
f.close()
f=open('test.txt','r')
body=f.read()
body = body.replace("Java","Python")
print(body)
f=open('test.txt','w')
f.write(body)
f.close()