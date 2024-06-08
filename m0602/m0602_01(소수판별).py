"""소수 판별 함수"""
from itertools import combinations          # 중복허용(X), 순서의미(O) 인 조합을 import

# 1. ------------------------------------------------------------------------------------
def numb(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):      # math를 사용하지 않고 (num//2)+1 까지로 설정
            if num%n == 0:
                return False
        
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))        # nums배열을 3개씩 조합 후 list로 변경
    for i in cmb:
        if numb(sum(i)):       # cmb를 하나씩 가져와 sum한 값을 소수 판별 함수로 넘겨줌
            answer += 1                     # return 값이 True이면 count(=answer) +1
    
    return answer

# 2. ------------------------------------------------------------------------------------
# for-else: for문 반복 끝난 후, else문 실행.
def solution(nums):
    answer = 0
    for a in cb(nums, 3):  # nums배열을 3개씩 조합
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

# 3. ------------------------------------------------------------------------------------
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        # **0.5 =루트(sqrt)
        # 소수 판정법: 자연수n에 대해 1보다 크고 루트 n이하인 모든 자연수로 나눠지지 않으면 소수임.
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])