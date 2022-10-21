import re
import numpy as np

def task1():
    x = int(input())
    sqr = x ** 2
    print(sqr)

def task2():
    string = input()
    lowercase_n = 0
    for ch in string:
        if ch >= 'a' and ch <= 'z':
            lowercase_n += 1
    print(lowercase_n)

def task3():
    words = map(str, input().split())
    words_n = sum(1 for word in filter(lambda w: re.match("Abo", w), words))
    print(words_n)

def task4(generator):
    words = filter(lambda w: re.search("sus", w), generator)
    return words

def task5(list_of_smth):
    output_list = list()
    for index in range(4, len(list_of_smth) - 5, 5):
        output_list.append(list_of_smth[index])
    print(*output_list)

def task6(list1, list2, list3, list4):
    print(*((set(list1) | set(list2)) & (set(list3) | set(list4))))

def task7():
    np.random.seed(13)
    matrix = np.random.randint(65, size=64).reshape(8, 8)
    minor = np.linalg.det(np.vstack([matrix[:6], matrix[7]])[:, 1:])
    return (matrix, minor)

# def task8(f, min_x, max_x, N, min_y, max_y):
#     # TODO: ...

# def task9(data, x_array, y_array, threshold):
#     # TODO: ...

# def task10(list_of_smth, n):
#     # TODO: ...

# def task11(filename="infile.csv"):
#     # TODO: ...

# def task12(filename="video-games.csv"):
#     # TODO: ...
