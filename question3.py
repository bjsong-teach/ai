# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1,000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.


#
# 숫자 맞추기 게임
# import random
# r_number = random.randint(1,100)
# 위와 같은 방식으로 컴퓨터가 임의의 숫자를 기억하게 한 다음 입력 받은 값이 
# 컴퓨터의 숫자와 비교하여 크다면 다운을!
# 작다면 업을 나오게 하여 사용자가 숫자를 맞추는 게임!
# 총 몇번의 시도를 통해 맞출 수 있는지 나와야 함

import random
r_number = random.randint(1,100)
user_count = 0
while True:
    try:
        user_num = int(input("숫자를 입력하세요."))
        user_count+=1
        if r_number > user_num:
            print('업')
        elif r_number < user_num:
            print('다운')
        else:
            print(f'{user_count}의 횟수에 정답을 맞추셨습니다.')
            break
    except Exception as e  :
        print(e)
