import random
import time

start_time = time.time()
rand_num = random.randint(1, 150)
new_arr = []

for i in range(rand_num):
    new_arr.append(random.randint(1, 121))

print(f'Не отсортированный список: {new_arr}')


def sorting(arr):
    if len(arr) <= 1:
        return arr

    point_in_middle = arr[len(arr) // 2]
    left = [i for i in arr if i < point_in_middle]
    middle = [i for i in arr if i == point_in_middle]
    right = [i for i in arr if i > point_in_middle]

    return sorting(left) + middle + sorting(right)


new_arr = sorting(new_arr)
print(f'Отсортированный список: {new_arr}')

rand_choice = random.choice(new_arr)


def bin_sarch(arr, num):
    low, high = 0, len(arr) - 1
    counter = 0
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        counter += 1
        if mid_val == num:
            print('Производили поиск числа: ', num)
            print('Кол-во попыток:', counter)
            return f'Индекс найденного числа: {mid}'
        elif num < mid_val:
            high = mid - 1
        elif num > mid_val:
            low = mid + 1

    return -1


print(bin_sarch(new_arr, rand_choice))
end_time = time.time()
print(f'Программа отработала за {end_time-start_time}')
