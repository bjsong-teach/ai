#2.
'''
result=0
i=1
while i <= 1000:
    if i%3==0:
        result +=i
    i +=1
print(result)

print("-"*50)
i=0
while True:
    i += 1
    if i > 5 : break
    print("*", end="")

a= range(101)
for i in a:
    print(i,end=" ")

print("-"*50)
marks = [70,60,55,75,89,98,80,80,85,100]
result = 0
for i in marks:
    result += i

c_marks = len(marks)
print(c_marks)
print(result)
avg = result/c_marks
print(avg)
print("-"*50)
'''
numbers = [1,2,3,4,5]
result=[]
for n in numbers:
    if n%2==0:
        result.append(n*2)

print(result) 
result = [n*2 for n in numbers if n%2==0]

#문제1 : 1부터 10까지 정수에서 3의 배수를 리스트 형태로 출력하시오.

#문제2 : 1부터 10까지 정수에서 5의 배수에 5의 배수가 아닌 값을 더하여 리스트 형태로 출력하시오.
#5+(1+2+3+4+6+7+8+9)
a=range(1,11)
result5=[]
summod = 0
for i in a:
    if i%5==0:
        result5.append(i)
    else:
        summod += i
result = []    
for k in result5:
    result.append(k+summod)
print(summod)
print(result5)
print(result)


# 1부터 100까지 중 2의 배수이고 3의 배수인 수를 리스트 형태로 구하시오.
result1 = []
for i in range(1,101) :
    if i%2==0 and i%3==0:
        result1.append(i)

result1 = [i for i in range(1,101) if i%2==0 and i%3==0]
print(result1)

