if __name__ == '__main__':
    n, m = map(int, input().split())
    poland,empty = {},{}

    for _ in range(n):
        st = str(input())
        poland[st] = 1
    for _ in range(m):
        st = str(input())
        empty[st] = 1


    turn = 1

    common_count = 0
    for i in poland:
        if empty.get(i) != None:
            common_count += 1

    n = n - common_count
    m = m - common_count

    if common_count % 2 == 0:
        turn = 1
    else:
        turn = 2

    if turn == 1:
        if n > m:
            print("YES")

        else:
            print("NO")

    else:
        if m > n:
            print("NO")
        else:
            print("YES")