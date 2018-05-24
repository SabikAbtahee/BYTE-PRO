
if __name__ == '__main__':
    str = input().lower()
    vowel = ['a','e','i','o','u','y']
    str2 = []
    for i in str:
        if(i not in vowel):  str2.append(i)

    for i in str2:
        print(".",end="")
        print(i,end="")

    print()
