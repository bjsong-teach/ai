# 마법의 세계에 오신 것을 환영합니다! 현재 마법의 숲에 있습니다.
# 명령어: '탐험', '상태', '종료'
# 상태는 아이템 리스트와 지역이 나온다.
# 무엇을 하시겠습니까?: 탐험
# 마법의 숲에서 마법 지팡이를 발견했습니다!
# 마법 지팡이를 획득했습니다! 축하드립니다.
# 무엇을 하시겠습니까?: 탐험
# 마법의 숲에서 늑대와 마주쳤습니다! '도망치기' 또는 '공격' 선택하세요.
# 선택: 도망치기 - 100% 성공
# 선택: 공격 - 50% 성공
# 승리시 아이템 얻을 확율 20% 증가
# 무엇을 하시겠습니까?: 탐험
# 마법의 숲에서 황금 왕관을 발견했습니다!
# 황금 왕관을 획득했습니다! 축하드립니다.
# 무엇을 하시겠습니까?: 탐험
# 마법의 숲에서 보석 목걸이를 발견했습니다!
# 보석 목걸이를 획득했습니다! 축하드립니다.
# 모든 보물을 찾았습니다! 마법의 승리!
# random.random()
locations = ["마법의 숲", "고대 성", "용의 동굴", "신비의 사막"]
treasures = ["마법 지팡이", "황금 왕관", "보석 목걸이"]
enemies = ["늑대", "해적", "드래곤"]

import random
#print(int(random.random()*100))
findAni = 30
attackSuc = 40
findRadio = 50
upRadio = 20
getTreasure = []

while True:
    UserStatus = input("탐험, 상태, 종료중 하나를 입력하세요.").strip()
    NowLocation = random.choice(locations)
    if UserStatus=='종료':
        print("게임을 종료합니다.")
        break
    elif UserStatus == '상태':
        print(getTreasure)
        print(NowLocation)
    elif UserStatus == "탐험":
        MeetRadio = int(random.random()*100)
        if MeetRadio>findAni:
            anim = random.choice(enemies)
            UserAttckYN = input(f"{anim}을 만났습니다. 도망치기, 공격 중 하나를 입력하세요.").strip()
            if UserAttckYN == "공격":
                AttackRadio = int(random.random()*100)
                if AttackRadio >attackSuc:
                    print("공격에 성공하였습니다.")
                    findRadio+=upRadio
                else:
                    print("당신은 사망하였습니다.")
                    break
            else:
                print("당신은 도망치는데 성공하였습니다.")
        fR = int(random.random()*100)
        gT = random.choice(treasures)
        if fR>=findRadio:
            getTreasure.append(gT)
            treasures.remove(gT)
            messageAppend = f"{gT}를 획득하였습니다."
        else:
            messageAppend = ""
        print(f"당신은 {NowLocation}에 도착하였습니다. {messageAppend}")

    if len(getTreasure)==3: 
        print("당신은 모든 아이템을 획득하였습니다.")
        break


