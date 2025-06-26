#가위 바위 보 게임
# import random
# choices = ['가위','바위', '보']
# computersChoice = random.choice(choices)

# 컴퓨터와 가위바위보를 해서 
# 이기면 "당신이 승리하셨습니다." 컴퓨터의 선택과 나의 선택을 같이 보여주기
# 지면 "컴퓨터가 승리하였습니다." 컴퓨터의 선택과 나의 선택을 같이 보여주기
# 비기면 "무승부입니다."

# q를 누르면 종료됩니다.

import random
choices = ['가위','바위', '보']

while True:
    try:
        computersChoice = random.choice(choices)

        userChoice = input("가위 바위 보중 하나를 입력하세요. 종료하려면 q를 누르세요.").strip()
       
        if userChoice=='q':
            break

        if userChoice in choices:
            if userChoice == computersChoice:
                print("무승부입니다.")
            elif (userChoice=='가위' and computersChoice=="보") or \
                 (userChoice=='바위' and computersChoice=="가위") or \
                 (userChoice=='보' and computersChoice=="바위"):
                print(f"당신이 승리했습니다. 나의 선택은 {computersChoice}이고 당신의 선택은 {userChoice}입니다.")
                # 가위 : 보 # 바위 : 가위 # 보 : 바위
            else:
                print(f"컴퓨터가 승리했습니다. 나의 선택은 {computersChoice}이고 당신의 선택은 {userChoice}입니다.")
        else:
            print("잘못 내셨습니다.")
    except Exception as e:
        print(e)
