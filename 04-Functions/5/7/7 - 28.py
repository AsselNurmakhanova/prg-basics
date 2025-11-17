def f(dice):
    dice = str(dice)
    if not dice:
        return 0  # пустая строка
    count = 1       # текущая последовательность начинается с 1
    max_count = 1   # максимальная последовательность тоже минимум 1
    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
    return max_count
