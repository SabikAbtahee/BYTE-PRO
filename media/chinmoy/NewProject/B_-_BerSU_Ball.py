


if __name__ == '__main__':

    lenA = int(input())
    a = list(map(int, input().split()))

    lenB = int(input())
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    x = lenA
    if(lenA>lenB): x = lenB

    count = 0

    # print(b)
    for i in range(x):
        if(abs(a[i]-b[i])==1 or abs(a[i]-b[i])==0):
            count+=1
            # b.remove(b[i])

    print(count,end='')
