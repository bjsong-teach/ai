# FourCal 클래스: 두 숫자를 입력받아 사칙연산을 수행하는 계산기 클래스
class FourCal:
    # setdata 메서드: 두 숫자를 객체의 속성으로 저장
    # self: 객체 자신을 참조
    # first, second: 저장할 두 숫자
    def setdata(self, first, second):
        self.first = first    # 첫 번째 숫자를 객체의 first 속성에 저장
        self.second = second  # 두 번째 숫자를 객체의 second 속성에 저장
    
    # add 메서드: 두 숫자의 덧셈 결과를 반환
    def add(self):
        return self.first + self.second  # first와 second를 더한 값을 반환
    
    # mul 메서드: 두 숫자의 곱셈 결과를 반환
    def mul(self):
        return self.first * self.second  # first와 second를 곱한 값을 반환
    
    # sub 메서드: 두 숫자의 뺄셈 결과를 반환
    def sub(self):
        return self.first - self.second  # first에서 second를 뺀 값을 반환
    
    # div 메서드: 두 숫자의 나눗셈 결과를 반환
    def div(self):
        if self.second == 0:  # 두 번째 숫자가 0인지 확인 (0으로 나누기 방지)
            return 0          # 0으로 나누려 하면 0을 반환
        return self.first / self.second  # first를 second로 나눈 값을 반환