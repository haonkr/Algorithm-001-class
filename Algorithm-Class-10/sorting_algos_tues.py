import random
import time
import matplotlib.pyplot as plt # type: ignore
from collections import deque
# ======================================================
# 1. 정렬 알고리즘
# ======================================================
def selection_sort(arr): # 선택정렬
    a = arr[:] # 원본 복사
    n = len(a)  # 배열 크기
    for i in range(n - 1): # i번째 위치에 최소값 삽입
        min_idx = i # 최소값 인덱스
        for j in range(i + 1, n): # 미정렬 구간 탐색
            if a[j] < a[min_idx]: # 더 작은 값 발견
                min_idx = j # 최소값 인덱스 갱신
        
        a[i], a[min_idx] = a[min_idx], a[i] # i번째 위치와 최소값 위치 교환
    return a # 반환

def insertion_sort(arr): # 삽입정렬
    a = arr[:] # 원본 복사
    n = len(a)  # 배열 크기
    for i in range(1, n): # 두 번째 원소부터 시작
        key = a[i] # 삽입할 원소
        j = i - 1 # 정렬된 구간의 마지막 인덱스
        while j >= 0 and a[j] > key: # 삽입할 위치 탐색
            a[j + 1] = a[j] # 원소를 한 칸씩 뒤로 이동
            j -= 1 # 인덱스 감소
        a[j + 1] = key # 삽입
    return a # 반환

def quick_sort(arr, left, right): # 퀵정렬
    # left, right는 정렬할 구간의 양 끝 인덱스
    def partition(A, left, right): # 분할 함수
        pivot = A[left] # pivot은 시작요소로 설정
        low = left + 1 # 피벗 다음부터 시작해서 피벗보다 작은 값 찾기
        high = right # 피벗보다 큰 값 찾기

        while low <= high: # 엇갈릴 때까지 반복
            while low <= right and A[low] < pivot:
                low += 1 # 오른쪽으로 이동
            while high >= left and A[high] > pivot:
                high -= 1 # 왼쪽으로 이동
            if low <= high: # 이 둘은 서로 반대편에 있어야 할 값이므로, 서로 교환
                A[low], A[high] = A[high], A[low] # 교환
                # 경계를 좁혀가면서 탐색을 계속
                low += 1
                high -= 1
            else: # 엇갈렸다면
                break
        A[left], A[high] = A[high], A[left] # 피벗과 high 위치 교환 - 피벗 제자리로 놓기
        return high # 피벗의 최종 위치(분할 기준)
    
    if left < right: # 정렬할 요소가 2개 이상인 경우
        q = partition(arr, left, right) # 피벗의 분할 위치 찾고
        quick_sort(arr, left, q - 1) # 왼쪽 부분 배열 재귀적 정렬
        quick_sort(arr, q + 1, right) # 오른쪽 부분 배열 정렬
    
    return arr

def radix_sort(arr, bucket_size = 10): # 기수정렬
    queues = [] # 버킷(큐) 리스트 초기화
    for _ in range(bucket_size): # 버캣 개수만큼 덱 추가
        queues.append(deque()) # 덱 추가
    
    n = len(arr) # 배열 입력 크기
    factor = 1 # 자리수 기준(1의 자리, 10의 자리, 100의 자리 ...)
    max_val = max(arr) # 최대값 찾기
    while max_val // factor > 0: # 최대값의 모든 자리수에 대해 반복
        for i in range(n): # 배열의 모든 원소에 대해
            digit = (arr[i] // factor) % bucket_size # 현재 자리수의 값 추출
            queues[digit].append(arr[i]) # 해당 버킷에 원소 추가
        
        idx = 0 # 배열 인덱스 초기화
        for b in range(bucket_size): # 각 버킷에서 원소 꺼내기
            while queues[b]: # 버킷이 비어있지 않으면
                arr[idx] = queues[b].popleft() # 원소 꺼내서 배열에 저장
                idx += 1 # 배열 인덱스 증가
        
        print(f"기수정렬 중간 단계 (factor = {factor}): {arr[:100]} ...") # 중간 단계 출력 (처음~100개만)
        factor *= bucket_size # 다음 자리수로 이동 - 10배 증가
    return arr

def list_sorted(arr): # 리스트의 sort에 메소드
    return arr.sort(reverse = False) # 기본 오름차순 정렬

def python_sorted(arr): # 내장 정렬 함수
    return sorted(arr) # 기본 오름차순 정렬

def lambda_sorted(arr): # 람다 함수 사용 정렬
    return sorted(arr, key = lambda x : x, reverse = False) # 복잡한 객체(튜플, 딕셔너리)를 정렬
    # ex : x = ("kim", 90), ("park", 80), lambda x : x[1] 점수로 정렬

# ======================================================
# 2. 실행 시간 측정 함수
# ======================================================
def measure_time(sort_func, data):
    arr = data[:]  
    start = time.time()
    if sort_func == quick_sort:
        sort_func(arr, 0, len(arr) - 1)
    else:
        sort_func(arr)
    return time.time() - start

# ======================================================
# 3. 알고리즘 목록
# ======================================================
algorithms = {
    "선택정렬": selection_sort,
    "삽입정렬": insertion_sort,
    "퀵정렬": quick_sort,
    "기수정렬": radix_sort,
    "lambda": lambda_sorted,
    "sorted()": python_sorted,
    "sort()": list_sorted,    
}

# ======================================================
# 4. 입력 크기별 실행 시간 측정
# ======================================================
sizes = [100, 1000, 10000, 100000, 1000000, 10000000]  # 테스트할 입력 크기
# results = {name: [] for name in algorithms.keys()} # 결과 저장용 딕셔너리
results = {}
for name in algorithms.keys():
    results[name] = []

repeat = 3  # 평균 반복 횟수

for n in sizes:
    print(f"\n데이터 크기 n={n}")
    # data = [random.randint(1, 99999) for _ in range(n)] # 무작위 데이터 생성
    data = []
    for _ in range(n):
        data.append(random.randint(1, 99999)) # 1 ~ 99999 사이의 난수 정수 생성 - 균등분포
        
    for name, func in algorithms.items(): # 각 알고리즘에 대해
        # 느린 정렬은 대규모 입력 생략
        if name in ["삽입정렬", "선택정렬"] and n > 1000: # 1천 초과 시 생략
            results[name].append(None) # 결과에 None 추가
            print(f"  {name:}: (생략)") # 출력
            continue # 생략
        times = [measure_time(func, data) for _ in range(repeat)] # 실행 시간 측정
        avg_time = sum(times) / len(times) # 평균 시간 계산
        results[name].append(avg_time) # 결과 저장
        print(f"  {name:}: {avg_time:.6f}초 (평균 {repeat}회)") # 출력

# ======================================================
# 5. 선 그래프 (로그 스케일)
# ======================================================
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트 설정 (Windows)
plt.figure(figsize=(10, 6)) # 그래프 크기 설정
for name, times in results.items(): # 각 알고리즘에 대해
    valid_sizes = [s for s, t in zip(sizes, times) if t is not None] # None이 아닌 크기만 선택
    valid_times = [t for t in times if t is not None] # None이 아닌 시간만 선택
    plt.plot(valid_sizes, valid_times, marker='o', label=name) # 선 그래프 그리기

plt.title("정렬 알고리즘별 실행 시간 비교 (입력 1백~1천만)", fontsize=14)
plt.xlabel("입력 크기 (n)")
plt.ylabel("평균 실행 시간 (초, log scale)")
plt.yscale("log") # 
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()