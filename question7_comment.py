# 규칙:
# 컴퓨터가 랜덤으로 "동물" 또는 "동물이 아닌 것"(예: 책, 나무)을 제시.
# 사용자가 "예"(동물) 또는 "아니오"(동물이 아님)로 맞추기.
# 맞추면 점수 1점, 틀리면 힌트 제공 후 재도전 기회.
# 3문제 완료 시 점수로 결과 출력(90점 만점 기준).
# 한번도 안틀리면 보너스 점수 10점

import random  # 무작위 항목 선택을 위해 random 모듈 임포트

# 항목 리스트 (동물과 비동물 혼합)
items = ["고양이", "강아지", "책", "나무", "펭귄", "자동차"]
# 동물만 포함된 리스트 (정답 기준)
animals = ["고양이", "강아지", "펭귄"]
# 점수 초기화 (90점 만점 기준, 문제당 30점)
score = 0
# 총 문제 수 (3문제)
total_count = 3
# 시도한 문제 수 초기화
total_attempt = 0
# 연속 정답 수 초기화 (보너스 점수 계산용)
correct_count = 0

# 게임 시작 메시지 (주석 처리된 부분은 참고용)
# print("동물 맞추기 게임을 시작합니다. 동물인지 아닌지 y/n으로 대답하세요")
# item = random.sample(items, 3)  # 3개 항목 무작위 선택 (사용 안 함)

# 게임 루프 (3문제 반복)
while total_count > total_attempt:
    # 리스트에서 무작위 항목 선택 후 제거 (중복 방지)
    item = random.choice(items)
    items.remove(item)
    # 사용자에게 질문 출력
    answer = input(f"{item}은/는 동물인가요? y/n").lower().strip()  # 소문자, 공백 제거

    # "예" (y) 입력 처리
    if answer == "y":
        if item in animals:  # 동물일 경우
            correct_count += 1  # 연속 정답 수 증가
            score += 30        # 점수 30점 추가
            print("정답을 맞추셨습니다.")
        else:  # 동물이 아닐 경우
            print("틀리셨네요")  # 힌트 제공 없음 (규칙 미준수)
    # "아니오" (n) 입력 처리
    else:
        if item not in animals:  # 동물이 아닐 경우
            correct_count += 1  # 연속 정답 수 증가
            score += 30        # 점수 30점 추가
            print("정답을 맞추셨습니다.")
        else:  # 동물일 경우
            print("틀리셨네요")  # 힌트 제공 없음 (규칙 미준수)

    # 보너스 점수 및 결과 출력 (논리 개선 필요)
    if correct_count == 3:  # 모든 문제 맞춘 경우
        score += 10         # 보너스 10점 추가
        print(f"모든 항목을 맞추셔서 10점의 가산점을 드려 최종 점수는 {score}입니다.")
    # elif total_attempt == 3:  # 3문제 완료 시 (논리 오류: while 조건과 중복)
    #     print(f"최종 점수는 {score}입니다.")  # 이 부분은 while 종료 후로 이동 필요

    total_attempt += 1  # 시도 횟수 증가

# while 루프 종료 후 결과 출력 (수정 제안)
if total_attempt == 3:
    print(f"퀴즈 종료! 당신의 최종 점수: {score}/90")
    if correct_count == 3:
        print("한 번도 틀리지 않으셔서 보너스 10점 포함!")
    else:
        print("다음에 다시 도전해 보세요!")