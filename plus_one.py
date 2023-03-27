def plus_one(digits: list) -> list:
    sum = ''
    final = []

    for i in digits:
        i = str(i)
        sum += i

    sum = int(sum) + 1

    for v in str(sum):
        final.append(int(v))

    return final


if __name__ == '__main__':
    digits = [9, 9]
    plus = plus_one(digits)
    print(plus)
