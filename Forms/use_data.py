def save_data(n):
    with open('data/res.txt', 'a') as file:
        file.write(f'{str(int(round(n, 0)))}\n')


def take_data():
    with open('data/res.txt', 'r+') as file:
        return max([int(i) for i in file.readlines()])

