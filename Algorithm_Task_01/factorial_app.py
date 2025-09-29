import time

def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하십시오.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하십시오.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


def run_with_time(func, n: int):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

TEST_VALUES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def run_menu():
    while True:
        print("\n===== Factorial Tester =====")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("------------------------------")
        choice = input("선택: ").strip()

        if choice == "q":
            print("종료합니다.")
            break

        elif choice in {"1", "2", "3"}:
            n_str = input("n 값(정수, 0 이상)을 입력하십시오: ").strip()
            if not n_str.isdigit():
                print("정수(0 이상의 숫자)만 입력하십시오.")
                continue
            n = int(n_str)
            try:
                if choice == "1":
                    result, elapsed = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {result}")
                    print(f"실행 시간: {elapsed:.6f} s")
                elif choice == "2":
                    result, elapsed = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {result}")
                    print(f"실행 시간: {elapsed:.6f} s")
                else:
                    iter_res, iter_t = run_with_time(factorial_iter, n)
                    rec_res, rec_t = run_with_time(factorial_rec, n)
                    print(f"[반복] {n}! = {iter_res}")
                    print(f"[재귀] {n}! = {rec_res}")
                    if iter_res == rec_res:
                        print("결과 일치 여부: 일치")
                    else:
                        print("결과 일치 여부: 불일치")
                    print(f"[반복] 시간: {iter_t:.6f} s  |   [재귀] 시간: {rec_t:.6f} s")
            except ValueError as e:
                print(f"오류: {e}")

        elif choice == "4":
            print("[테스트 데이터 실행]")
            for n in TEST_VALUES:
                try:
                    iter_res, iter_t = run_with_time(factorial_iter, n)
                    rec_res, rec_t = run_with_time(factorial_rec, n)
                    print(f"n = {n}  |  same = {iter_res == rec_res}  |  iter = {iter_t:.6f} s, rec = {rec_t:.6f} s")
                    print(f"    {n}! = {iter_res}")
                except Exception as e:
                    print(f"예외 발생: {e}")
        else:
            print("잘못된 입력입니다. 다시 입력하십시오.")

if __name__ == "__main__":
    run_menu()