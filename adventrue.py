import random  # 랜덤 이벤트와 전투 결과를 생성하기 위한 모듈

# 초기 설정
locations = ["마법의 숲", "고대 성", "용의 동굴", "신비의 사막"]  # 가능한 장소 리스트
treasures = ["마법 지팡이", "황금 왕관", "보석 목걸이"]        # 획득할 보물 리스트
enemies = ["늑대", "해적", "드래곤"]                           # 만날 수 있는 적 리스트

score = 0  # 획득한 보물 수 (목표: 3개)
current_location = random.choice(locations)  # 게임 시작 시 랜덤 장소 선택

# 게임 시작 메시지 출력
print(f"마법의 세계에 오신 것을 환영합니다! 현재 {current_location}에 있습니다.")
print("명령어: '탐험', '상태', '종료'")

# 게임 메인 루프
while True:
    action = input("무엇을 하시겠습니까?: ").lower().strip()  # 사용자 입력 받기, 소문자와 공백 정리

    # 명령어 처리
    if action == "종료":  # '종료' 입력 시 게임 끝
        print("모험을 종료합니다.")
        break
    elif action == "상태":  # '상태' 입력 시 현재 상황 확인
        print(f"현재 위치: {current_location}")
        print(f"획득한 보물: {score}개")
    elif action == "탐험":  # '탐험' 입력 시 랜덤 이벤트 발생
        event = random.choice([*treasures, *enemies, "빈 공간"])  # 보물, 적, 빈 공간 중 하나 선택
        print(f"{current_location}에서 {event}을 발견했습니다!")
        
        if event in treasures:  # 보물 발견 시
            print(f"{event}을 획득했습니다! 축하드립니다.")
            score += 1  # 보물 수 증가
            if score == 3:  # 3개 보물 획득 시 승리
                print("모든 보물을 찾았습니다! 마법의 승리!")
                break
        elif event in enemies:  # 적과 마주친 경우
            print(f"{event}와 마주쳤습니다! '도망치기' 또는 '공격' 선택하세요.")
            fight_choice = input("선택: ").lower().strip()  # 전투 선택 입력
            if fight_choice == "공격":  # '공격' 선택
                if random.random() < 0.5:  # 50% 확률로 승리
                    print(f"당신이 {event}를 이겼습니다!")
                else:  # 50% 확률로 패배
                    print(f"{event}에게 졌습니다. 게임 오버!")
                    break
            elif fight_choice == "도망치기":  # '도망치기' 선택
                print("성공적으로 도망쳤습니다!")
                if random.random() < 0.2:  # 20% 확률로 보물 발견
                    treasure = random.choice(treasures)  # 랜덤 보물 선택
                    print(f"도망치는 중 {treasure}을 우연히 발견했습니다!")
                    score += 1  # 보물 수 증가
                    if score == 3:  # 3개 달성 시 승리
                        print("모든 보물을 찾았습니다! 마법의 승리!")
                        break
            else:  # 잘못된 선택
                print("잘못된 선택입니다. 공격당했습니다. 게임 오버!")
                break
        else:  # 빈 공간
            print("아무것도 발견하지 못했습니다.")
    else:  # 알 수 없는 명령어
        print("알 수 없는 명령어입니다. '탐험', '상태', '종료' 중 선택하세요.")