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

# ======================================================
# 알고리즘 설계 전략 : 분활과 정복 (Divide & Conquer)
# ======================================================
# 1. k번째 작은 수를 찾는 문제 (k-th smallest element)
# 1. 분할 함수 정의 - 퀵 정렬의 분할 함수 사용
def partition(A, left, right):
    pivot = A[left] # pivot 설정
    i = left + 1 # 왼쪽 서브리스트 포인터
    j = right # 오른쪽 서브리스트 포인터

    while True:
        while i <= j and A[i] <= pivot:
            i += 1

        while i <= j and A[j] > pivot:
            j -= 1
        
        if i > j:
            break

        A[i], A[j] = A[j], A[i]
        
    A[left], A[j] = A[j], A[left]
    return j

# (1) 억지기법 : 정렬 이용, 시간복잡도는 O(n log n)
def kth_smallest_bf(arr, k):
    B = sorted(arr) # O(n log n)
    return B[k - 1] # k번째 작은 수의 인덱스 사용

# (2) 축소정복 전략 사용 - 재귀함수와 분할함수 이용
# - 시간복잡도 : 평균 O(n), 최악 O(n^2)
def quick_select(A, left, right, k):
    if left == right: # 함수 호출 종료
        return A[left]
    
    # 피벗을 배열 A의 첫번째 요소로 설정
    pos = partition(A, left, right)
    # pos는 0부터 시작하는 인덱스 - 순서로 변환시 pos + 1
    # k와 pos + 1을 비교
    if k + left == pos + 1: # case 1 - 피벗이 k번째인 경우
        return A[pos]
    elif k + left < pos + 1: # case 2 - k번째 작은 수가 피벗의 왼쪽에 나타나는 경우
        return quick_select(A, left, pos - 1, k)
    else: # case 3 - k번째 작은 수가 피벗의 오른쪽에 나타나는 경우 k를 갱신
        return quick_select(A, pos + 1, right, k - (pos + 1 - left))
    
# 테스트
A1 = [7, 2, 1, 8, 6, 3, 5, 4, 0]
A2 = A1.copy()
k = 3
print("억지기법 :", kth_smallest_bf(A1, k))
print("축소정복 :", quick_select(A2, 0, len(A2) - 1, k))
print("=" * 100)

# ======================================================
# 2. MergeSort 병합정렬
# 오름차순으로 정렬, 중복된 데이터 허용, 안정적 정렬, 추가 메모리 사용
# 시간 복잡도ㅗ : O(n log n)
#  1. 병합 함수
def merge(A, left, mid, right):
    # 1. 임시 리스트 생성 : 크기 = right - left + 1
    sorted_list = [0] * (right - left + 1)

    # 2. 두 부분 리스트의 시작 인덱스
    i = left # 왼쪽 부분 리스트 시작 index
    j = mid + 1 # 오른쪽 부분 리스트 시작 index
    k = 0 # 임시 리스트의 시작 index

    # 3. 두 정렬 리스트를 비교하여 임시 리스트에 기록
    while i  <= mid and j <= right: # O(n)
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i += 1
            k += 1
        else:
            sorted_list[k] = A[j]
            j += 1
            k += 1

    # 4. 왼쪽 부분 리스트가 남아 있는 경우 모두 복사
    while i <= mid:
        sorted_list[k] = A[i]
        i += 1
        k += 1
    # 4. 오른쪽 부분 리스트가 남아 있는 경우 모두 복사
    while j <= right:
        sorted_list[k] = A[j]
        j += 1
        k += 1

    # 5. 임시 리스트의 결과를 원래 리스트 A에 덮어쓰기
    for t in range(k):
        A[left + t] = sorted_list[t]

# 병합 정렬 함수
def merge_sort(A, left, right):
    if left < right: # 항목이 두 개 이상인 경우에만 분할 - O(log n)
        mid = (left + right) // 2
        # 왼쪽 부분 정렬
        merge_sort(A, left, mid)
        # 오른쪽 부분 정렬
        merge_sort(A, mid + 1, right)
        # 정렬된 두 부분 리스트를 병합 - O(n)
        merge(A, left, mid, right)

# 테스트
A = [38, 27, 43, 3, 9, 82, 10]
print("정렬 전:", A)
merge_sort(A, 0, len(A) - 1)
print("정렬 후:", A)
print("=" * 100)

# 프로그래밍 문제 1 : 병합 정렬 기반 중복 제거 알고리즘

# ======================================================
# 알고리즘 설계 전략 : 동적계획법(Dynamic Programming)
# ======================================================
# 1. fibonacci sequence (피보나치 수열) 문제
#  (1) 동적계획법 - 메모이제이션 방식 - top-down 방식 - 주어진 문제에서 작은 문제로 해결하는 방식

# 1. 전역 변수로 메모이제이션 배열 준비(0, 10까지)
mem = [None] * 11

def fib_dp_mem(n): # fib(n) = ?
    if mem[n] is None:
        if n < 2: # 처음 계산하는 값이면 기록
            mem[n] = n # fib(0) = 0, fib(1) = 1
        else: # 중복 계산 피함
            mem[n] = fib_dp_mem(n - 1) + fib_dp_mem(n  - 2)
    return mem[n]

# 테스트
print("n = 6 => fib(6) :", fib_dp_mem(6))
print("mem = ", mem[:7]) # 결과 수열 출력
print("=" * 100)

#  (2) 동적계획법 - 테이브화 방식 - bottom-up 방식 - 작은 문제부터 큰 문제로 주어진 문제를 해결하는 방식
# DP 테이블 생성 - 지역변수 처리, 반복문
# 시간복잡도 : O(n)
def fib_dp_tab(n):
    # 1. 1차원 리스트 준비
    table =[None] * (n + 1)
    table[0] = 0
    table[1] = 1

    # 2. 상향식으로 테이블  채우기
    for i in range(2, n + 1):
        table[i] = table[i - 1] +  table[i - 2]
    return table

# 테스트
table = fib_dp_tab(6)
print(table[6])
print("table =", table[:7])

# ======================================================
# 프로그래밍 문제 : 계단 오르는 방법의 수 계산하기
# ======================================================

# 2. 0/1 배낭 문제
# 시간복잡도 : O(nW)