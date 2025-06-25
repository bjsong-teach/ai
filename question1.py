#1번 국어=80 영어=75 수학=55
a = {'국어':80, '영어':75,'수학':55}
print(a['영어'])
sum = 0
for k in a.values():
    sum += k
print(sum)
i=len(a)
avg = sum/i

print(avg)

a=13
if a%2:
    print('홀수 입니다.')
else:
    print('짝수 입니다.')



pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print('생년월일 :'+yyyymmdd)
print('주민번호 뒷자리 :'+num)
num2 = pin[7:8]
print('성별 :'+num2)

a="a:b:c:d"
b=a.replace(":","#")
print('문자열 바꾸기 :'+b)

a=[1,3,5,4,2]
a.sort()
print('오름차순 정렬 :',a)

a.reverse()
print('내림차순 정렬 :',a)
print(f'내림차순 정렬 :{a}')
print('내림차순 정렬 :'+str(a))
print('내림차순 정렬 :{}'.format(a))

a= ['Life', 'is','too','short']
result = ' a'.join(a)
print(result)
'''
()
'''
