# 1. Bruteforce algorithm: 문자열 매칭 문제
def string_matching(text, pattern):
    n = len(text) # 텍스트 길이
    m = len(pattern) # 패턴 길이

    for i in range(n - m + 1): # 텍스트의 각 위치에서 : O(n - m + 1) == O(n)
        j = 0 # 패턴의 시작 위치
        while j < m and text[i + j] == pattern[j]: # 패턴의 각 문자와 비교 : O(m)
            j += 1 # 패턴의 다음 문자로 이동
        if j == m : # 모든 패턴의 문자 일치
            return i # 일치하는 부분 텍스트 문자열의 시작 위치 반환
    return -1

# 테스트 코드
# text = "HELLO WORLD"
# pattern = "LO"
# result = string_matching(text, pattern)
# if result != -1:
#     print(f"패턴이 텍스트에서 위치 {result}에서 발견")
# else:
#     print("패턴이 텍스트에서 발견되지 않았음")

# 문자열 매칭 문제 수정 : 전부 매칭 찾기
def string_matching_all(text, pattern):
    n = len(text) # 텍스트 길이
    m = len(pattern) # 패턴 길이
    matches = [] # 복수 개 매칭 위치 저장

    for i in range(n - m + 1): # 텍스트의 각 위치에서 : O(n - m + 1) == O(n)
        j = 0 # 패턴의 시작 위치
        while j < m and text[i + j] == pattern[j]: # 패턴의 각 문자와 비교 : O(m)
            j += 1 # 패턴의 다음 문자로 이동
        if j == m : # 모든 패턴의 문자 일치
            matches.append(i) # 매칭 위치 저장
    return matches

# 테스트 코드
text = "ABABDABACDABABABCABABABABCABABABABCABABCA"
pattern = "ABABCABAB"
result = string_matching_all(text, pattern)
print(result)