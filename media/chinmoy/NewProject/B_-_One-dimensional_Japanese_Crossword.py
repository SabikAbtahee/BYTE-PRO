
if __name__ == '__main__':
    s = int(input())
    str = input()
    t = []
    for i in str:
        if(i=='W'): t.append('-')
        else: t.append(i)
    count = 0
    arr = []
    for i in t:
        if(i == '-'):
            if(count != 0):
                arr.append(count)
            count = 0

        else:
            count+=1
    if (count != 0):
        arr.append(count)
    print(len(arr))
    for i in arr:
        print(i,end=" ")
    print()

