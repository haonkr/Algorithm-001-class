# ===============================================================
# 탐색 알고리즘 성능 비교 
# 모든 함수는 동일한 매개변수 시그니처 (arr, key, low, high)
# 각 알고리즘의 평균 비교 횟수와 실행시간을 측정하여 그래프로 시각화
# ===============================================================
import random, time
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"   # 한글 폰트 지정

# 1. 순차 탐색 (Sequential Search): O(n)
def linear_search(arr, key, low = 0, high = None):
    if high is None:
        high = len(arr) - 1 # high 기본값 처리
    count = 0 # 비교 연산 횟수 카운트
    for i in range(low, high + 1): # low ~ high까지 순차 탐색
        count += 1 # 비교 횟수 증가
        if arr[i] == key: # 키를 찾으면
            return i, count # 인덱스와 비교 횟수 반환
        return -1, count # 못 찾으면 -1 반환
# 2. 이동 평균 탐색 (Sequential Search with Transpose): 평균 O(n)
def sequential_search_transpose(arr, key, low = 0, high = None):
    if high is None:
        high = len(arr) - 1 # high 기본값 처리
    count = 0 # 비교 연산 횟수 카운트
    for i in range(low, high + 1): # low ~ high까지 순차 탐색
        count += 1 # 비교 횟수 증가
        if arr[i] == key: # 키를 찾으면
            # 찾은 경우 바로 앞의 원소와 자리 교환
            if i > low: # 처 번째 원소가 아니라면
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= i # 인덱스 한칸 앞으로
            return i, count # 인덱스와 비교 횟수 반환
        return -1, count # 못 찾으면 -1 반환
# 3. 이진 탐색 (Binary Search): O(log n)
def binary_search_iter(arr, key, low = 0, high = None):
    if high is None:
        high = len(arr) - 1 # high 기본값 처리
    count = 0 # 비교 연산 횟수 카운트
    left, right = low, high # 탐색 구간 초기화
    mid = (left + right) // 2 # 중앙 인덱스 계산
    if arr[mid] == key: # 찾은 경우
        return mid, count
    elif arr[mid] < key: # 키가 더 크면 오른쪽 반 탐색
        left = mid + 1
    else: # 키가 더 작으면 왼쪽 반 탐색
        right = mid - 1
    return -1, count # 탐색 실패

# 4. 보간 탐색 (Interpolation Search)
def interpolation_search(arr, key, low = 0, high = None):
    if high is None:
        high = len(arr) - 1 # high 기본값 처리
    count = 0 # 비교 연산 횟수 카운트
    left, right = low, high # 탐색 구간 초기화
    mid = (left + right) // 2 # 중앙 인덱스 계산
    if arr[mid] == key: # 찾은 경우
        return mid, count
    elif arr[mid] < key: # 키가 더 크면 오른쪽 반 탐색
        left = mid + 1
    else: # 키가 더 작으면 왼쪽 반 탐색
        right = mid - 1
    return -1, count # 탐색 실패


# 5. 성능 테스트
n = 10000                                    # 데이터 크기
arr = sorted(random.sample(range(n * 3), n)) # 정렬된 랜덤 배열 생성 
targets = random.sample(arr, 1000)           #  1000개의 임의 target 값을 각 탐색 알고리즘으로 탐색

def measure(func, arr, targets): # 평균 비교 횟수와 평균 실행시간 측정
    total_time, total_cmp = 0, 0
    for t in targets:
        test_arr = arr[:]                   
        start = time.perf_counter()          # 탐색 시작 시간
        _, cmp_cnt = func(test_arr, t, 0, len(test_arr) - 1)
        total_time += time.perf_counter() - start
        total_cmp += cmp_cnt    
    return total_time / len(targets), total_cmp / len(targets) # 평균 시간(초)과 평균 비교 횟수 반환

linear_t, linear_c = measure(linear_search, arr, targets)
sequential_t, sequential_c = measure(sequential_search_transpose, arr, targets)
binary_t, binary_c = measure(binary_search_iter, arr, targets)
interp_t, interp_c = measure(interpolation_search, arr, targets)

print("=== 탐색 알고리즘 성능 비교 결과 ===")
print(f"순차 탐색 : 평균 {linear_c:.2f}회 비교, 평균시간 {linear_t*1e6:.2f} μs")
print(f"이동 평균 탐색 : 평균 {sequential_c:.2f}회 비교, 평균시간 {sequential_t*1e6:.2f} μs")
print(f"이진 탐색 : 평균 {binary_c:.2f}회 비교, 평균시간 {binary_t*1e6:.2f} μs")
print(f"보간 탐색 : 평균 {interp_c:.2f}회 비교, 평균시간 {interp_t*1e6:.2f} μs")

# 6. 시각화 (비교 횟수 및 실행 시간)
import numpy as np
labels = ["순차 탐색", "이동 평균 탐색", "이진 탐색", "보간 탐색"]
compare_counts = [linear_c, sequential_c, binary_c, interp_c]
times = [linear_t*1e6, sequential_t*1e6, binary_t*1e6, interp_t*1e6] 

x = np.arange(len(labels))
width = 0.35
fig, ax1 = plt.subplots(figsize=(9, 5))

# 왼쪽 y축: 비교 횟수
bars1 = ax1.bar(x - width/2, compare_counts, width,
                label="비교 횟수", color=["gray", "lightblue", "skyblue", "lightgreen"])
ax1.set_ylabel("평균 비교 횟수")
ax1.set_title("탐색 알고리즘 비교 (비교 연산 횟수 및 실행 시간, n=10,000, 1000회 평균)")
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.set_yscale("log")

# 오른쪽 y축: 실행 시간 
ax2 = ax1.twinx()
bars2 = ax2.bar(x + width/2, times, width, label="평균 실행 시간 (μs)", \
                color=["dimgray", "deepskyblue", "limegreen", "mediumseagreen"])
ax2.set_ylabel("평균 실행 시간 (μs)")
ax2.set_yscale("log")

fig.legend(loc="upper center", ncol=2)
plt.tight_layout()
plt.show()
