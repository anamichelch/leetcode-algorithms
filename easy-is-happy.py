def is_happy(n):
    while n != 4:
        list = [int(num) for num in str(n)]
        lenght = len(list)
        new_sum = 0
        for i in range(0, lenght):
            squared_digit = list[i] ** 2
            new_sum += squared_digit
            n = new_sum
            if n == 1:
                return True
    return False


print(is_happy(19))
print(is_happy(2))
print(is_happy(1))
print(is_happy(7))
