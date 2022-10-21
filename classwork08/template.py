import re
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

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
#     plot = plt.subplot()

# def task9(data, x_array, y_array, threshold):
#     # TODO: ...

# def task10(list_of_smth, n):
#     # TODO: ...

# def task11(filename="infile.csv"):
#     # TODO: ...

def task12(filename="video-games.csv"):
    data = pd.read_csv(filename)
    return dict(
        n_games = len(data),
        by_years = data.groupby(['year']).agg(games_per_year=('title', len)),
        mean_price = data.groupby(['publisher']).agg(mean_price=('price', 'mean')),
        age_max_price = data.loc[data.groupby(['age_raiting'])['price'].transform(max) == data['price']],
        mean_raiting_1_2 = data.groupby(['max_players']).agg({'review_raiting': 'mean'})
    )

print(task12()['mean_raiting_1_2'])
