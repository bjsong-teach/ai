# 규칙:
# 컴퓨터가 랜덤으로 "동물" 또는 "동물이 아닌 것"(예: 책, 나무)을 제시.
# 사용자가 "예"(동물) 또는 "아니오"(동물이 아님)로 맞추기.
# 맞추면 점수 1점, 틀리면 힌트 제공 후 재도전 기회.
# 3문제 완료 시 점수로 결과 출력(90점 만점 기준).
# 한번도 안틀리면 보너스 점수 10점
#

#items = ["고양이", "강아지", "책", "나무", "펭귄", "자동차"]

import random
items = ["고양이", "강아지", "책", "나무", "펭귄", "자동차"]
animals = ["고양이", "강아지","펭귄"]
score =0
totalCount =3
totalattemp = 0
CorrectCount =0 
#print("동물 맞추기 게임을 시작합니다. 동물인지 아닌지 y/n으로 대답하세요")
#item = random.sample(items,3) 
while totalCount > totalattemp:
    item = random.choice(items)
    items.remove(item)
    answer = input(f"{item}은/는 동물인가요? y/n").lower().strip()

    if answer == "y":
        if item in animals:
            CorrectCount += 1
            score += 30
            print("정답을 맞추셨습니다.")
        else:
            print("틀리셨네요")
    else:
        if item not in animals:
            CorrectCount += 1
            score += 30    
            print("정답을 맞추셨습니다.")
        else:
            print("틀리셨네요")
    
    if CorrectCount == 3:
        score += 10
        print(f"모든 항목을 맞추셔서 10점의 가산점을 드려 최종 점수는 {score}입니다.")
    elif totalattemp==3:
        print(f"최종 점수는 {score}입니다.")


    totalattemp+=1

