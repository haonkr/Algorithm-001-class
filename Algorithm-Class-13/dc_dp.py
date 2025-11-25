# ===================================================================
# 알고리즘 설계 기법 : 분할과 정복 (Dvide & Conquer)
# ===================================================================
# 1. 배열(arr)의 합 구하기 문제 : 억지기법 vs. 분할 정복

def sum_bf(arr): # 시간복잡도 - O(n), n = len(arr), 공간복잡도 - O(1)
    """억지기법 - 단순 반복문"""
    total = 0
    for x in arr:
        total += x
    return total

def sum_dc(arr, left, right): # 시간복잡도 - O(n), 시스템 스택 호출 - (n)
    """분할정복 기반 재귀함수"""
    # 원소가 한 개인 경우 -> 이미 정복
    if left == right:
        return arr[left] # 종료 조건
    # 원소가 2개 이상인 경우 반으로 나누기
    mid = (left + right) // 2
    # 왼쪽 부분문제 배열의 합
    left_sum = sum_dc(arr, left, mid)
    # 오른쪽 부분문제 배열의 합
    right_sum = sum_dc(arr, mid + 1, right)
    # 병합 (두 개의 부분문제의 결과를 합침)
    return left_sum + right_sum

# 테스트
arr = [5, 3, 8, 4, 1, 6, 2, 7]
print("Iterative Sum = ", sum_bf(arr))
print("Divide & Conquer Sum = ", sum_dc(arr, 0, len(arr) - 1))
print("=" * 100)

# 2. 거듭제곱 계산 문제 : 억지기법 vs. 분할(축소)정복
def power_bf(x, n): # x^n = x * x * ... * x
    """억지기법 반복문 구조 : O(n)"""
    result = 1.0
    for _ in range(n):
        result *= x # x를 n번 곱함
    return result

def power_dc(x, n):
    """DC의 축소 정복 기반 재귀 구조 : O(log n)"""
    if n == 1: # 종료 조건
        return x
    elif n % 2 == 0: # n이 짝수
        return power_dc(x * x, n // 2) # 재귀 호출 - 절반 크기로 감소 - O(log n)
    else: # n이 홀수
        return x * power_dc(x * x, (n - 1) // 2) # 재귀 호출 - 절반 크기로 감소 - O(log n)
    
# 테스트 코드
x = 2.0
n = 10
print(f"억지기법 x의 n 거듭제곱({x}, {n}) = {power_bf(x, n)}")
print(f"축소정복 x의 n 거듭제곱({x}, {n}) = {power_dc(x, n)}")
print("=" * 100)