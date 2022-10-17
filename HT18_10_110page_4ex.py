n = int(input("Введите сколько чисел вы хотите ввести: "))
just = 0 
arr_positive = []
arr_negative = []
while n > just: 
    just += 1 
    x = int(input("Введите число, не равное нулю: "))

    if x > 0:
        arr_positive.append(x)
        sum_positive = sum(arr_positive)
    else:
        arr_negative.append(x)
        sum_negative = sum(arr_negative)
print("Сумма положительных чисел: ", sum_positive)
print("Сумма отрицательных чисел: ", sum_negative)