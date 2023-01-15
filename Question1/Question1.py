def solution(n):
    if n % 4 == 0:
        return "BUY"
    elif n % 2 == 0:
        return "PASS"
    else:
        return "SELL"

def main():
    n = int(input())
    print(solution(n))


if __name__ == "__main__":
    main()