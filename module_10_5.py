# Задача "Многопроцессное считывание":
from datetime import datetime
import multiprocessing

def read_info(name):
    # name - название файла
    all_data = [] # локальный список
    with open(name, 'r', encoding='utf-8') as file:  #  открытие файла
        while True:
            line = file.readline().strip() # Считывать информацию построчно (readline), пока считанная строка не окажется пустой
            all_data.append(line) # Во время считывания добавлять каждую строку в список all_data
            if not line:
                break

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
    start = datetime.now()
    for filename in filenames:
        read_info(filename)
    end = datetime.now()
    print(f'{end - start}')

# Многопроцессный
    with multiprocessing.Pool(processes=4) as pool:
        start_1 = datetime.now()
        pool.map(read_info, filenames)
        end_1 = datetime.now()
        print(f'{end_1 - start_1}')