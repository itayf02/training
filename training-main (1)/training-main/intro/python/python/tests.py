for num in range(1000, 3001):
    flag = True
    num_temp = num
    while num_temp > 0:
        if (num_temp % 10) % 2 != 0:
            flag = False

