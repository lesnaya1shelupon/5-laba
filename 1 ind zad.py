import sys

if __name__ == '__main__':
    print("Введите 10 элементов: ")
    A = list(map(int, input().split()))
    new_list = A
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    f = 0
    n = 1
    k = []
    for i in A:
        if 8 < i < 18 and i / 10 == 1:
            f += 1
            n *= i
            k.append(i)
    print("Количество элементов больших 8 и меньших 18, кратное 10 =", f)
    print("Произведение новых элементов =", n)
    print(k)