p = 1
is_prime = True

while(True):
    is_prime = True

    # p가 100보다 커지면 종료
    if p > 100:
        break

    # 만약 p가 소수가 아니라면 반복문 pass
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            p += 1
            is_prime = False
            break
    
    if not is_prime:
        continue

    # p가 소수라면 1~p-1 중 제곱해서 p로 나누었을 때 나머지가 2인지 확인하여 출력
    for a in range(1, p):
        if (a * a) % p == 2:
            print(f"p: {p}, a: {a}")
            break
    p += 1