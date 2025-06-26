# 숫자 야구 게임이란?
# 규칙:
# 컴퓨터가 3자리 숫자(0~9, 중복 없음)를 랜덤 생성.
# 사용자가 숫자를 입력해 추측.
# 스트라이크(S): 숫자와 위치가 모두 맞음.
# 볼(B): 숫자는 맞지만 위치 다름.
# 아웃(O): 맞는 숫자 없음.
# 3 스트라이크 시 게임 종료.
# import random
# def generate_answer():
#     digits = list(range(10))  # 0부터 9까지의 숫자 리스트
#     random.shuffle(digits)    # 리스트를 무작위로 섞기
#     return digits[:3]         # 처음 3자리 반환 (중복 없음)
# computer 891

# user 815
# 2strike 1ball
# user 123
# 1ball 

# user 576 1out
# user 576 1out