def main():
    import sys

    m, n = map(int, input().split())

    l = []
    for i in range(m, n + 1):
        a, b, c = str(i)
        if i == (int(a) ** 3 + int(b) ** 3 + int(c) ** 3):
            l.append(i)

    if l is not None:
        for i in l:
            print(i, end=' ')
    else:
        print('no')


main()