def add(a,b):
    return a+b
result = add(1,2)
result1 = add(result,2)
print(result1)

def say():
    return "hi"
print(say())

def sub(a,b):
    return a-b

result = sub(b=4, a=2)
result1 = sub(4, 2)
print(result)
print(result1)

def add_many(*args):
    result =0
    for i in args:
        result += i
    return result
add_a_lot = add_many(1,2,3,4,5,7)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(add_a_lot)
print(result)

def add_mul(choice,*args):
    if choice=="add":
        result =0
        for i in args:
            result += i
    if choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

a = add_mul("add",1,2,3,4,54,56,6,6,43,3,3,54,4,34,34,34,3,34,3,34)
b = add_mul("mul",1,2,3,4,54,56,6,6,43,3,3,54,4,34,34,34,3,34,3,34)
print(a,b)


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3,height =4)

def add_and_mul(a,b):
    return a+b, a*b
print(add_and_mul(3,4))

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

def say_nick(nick):
    if nick=='바보':
        return
    print(f"나의 별명은 {nick}입니다.")
say_nick('바보')
say_nick('천재')

def say_myself(name, age, gender=True, short='1'):
    print(f"나의 이름은 {name}입니다.")
    print(f"나의 나이는 {age}입니다.")
    if gender:
        print("여자입니다.")
    else:
        print("남자입니다.")

say_myself('나',34,0)
say_myself('나',34)

add = lambda a,b:a+b
def add(a,b):
    return a+b



'''
일반 프로그램 함수 방법
function add(a,b){
    return a+b
}
'''