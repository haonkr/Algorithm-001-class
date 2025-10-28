import random
import time
import matplotlib.pyplot as plt # type: ignore
from collections import deque

# ======================================================
# 1. 정렬 알고리즘
# ======================================================
def selection_sort(arr): # 선택 정렬
    a = arr[:] # 원본 복사
    n = len(a) # 배열 크기
    for i in range(n-1): # 1번째 위치에서 최소값 삽입
        least_idx = i # 최소값 인덱스
        for j in range(i + 1, n): # 미정렬된 구간 탐색
            if a[j] < a[least_idx]: # 더 작은 값을 발견
                least_idx = j # 작은 값 인덱스 갱신
        a[i], a[least_idx] = a[least_idx], a[i] # i번째 위치의 최소값 위치 교환
    return a


def insertion_sort(arr): # 삽입 정렬
    a = arr[:] # 원본 복사
    n = len(a) # 배열 크기
    for i in range(1, n): # 두 번째 요소부터 시작
        key = a[i] # 삽입할 원소
        j = i - 1 # 정렬된 구간의 마지막 인덱스
        while j >= 0 and a[j] > key: # 삽입할 위치 탐색
            a[j + 1] = a[j] # 요소를 한칸 뒤로 이동
            j -= 1 # 인덱스 감소
        a[j + 1] = key # 삽입
    return a

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
results = {name: [] for name in algorithms.keys()} # 결과 저장용 딕셔너리
repeat = 3  # 평균 반복 횟수

for n in sizes:
    print(f"\n데이터 크기 n={n}")
    data = [random.randint(1, 99999) for _ in range(n)] # 무작위 데이터 생성
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