#представление как должно выглядить
matrix1 = [
    [' ', '0', '1', '2'],
    ['0', '-', '-', '-'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-']
]

#матрица с которой будем работать
matrix = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

#попытался представить алгоритм без привязки к размеру матрицы 3x3

def stop_game(matrix):
    return all('-' not in el for el in matrix)

def input_data(per_size, per_size_view, type_x_o = 'horizontal'):
    while True:
        value = input(f'Введите координату { "горизонтали" if type_x_o == "horizontal" else "вертикали"} [{per_size_view}]:')
        if value not in per_size:
            print('Ошибка ввода')
        else:
            return value

def print_matrix(matrix):
    print(' '.join(f'  {i}' if i == 0 else str(i) for i in range(len(matrix))))
    i = 0
    for row in matrix:
        print(str(i)+' '+' '.join(row))
        i += 1

def check_matrix(matrix, value):
    for row in matrix:
        if all(value == el for el in row): 
            return True
    for row in zip(*matrix): #транспонирование матрицы чтобы работать через итераторы, возможно лучше было 2 цикла и if с индексами
        if all(value == el for el in row): 
            return True
#    for i in range(len(matrix)):
#        for j in range(len(matrix[i])):
#            if matrix[i][j] == value and ...        

    if all(matrix[i][i] == value for i in range(len(matrix))):
        return True
    if all(matrix[i][len(matrix)-1-i] == value for i in range(len(matrix))):
        return True

    return False
            
switch_x_o = 'O'
per_check = False
per_size_view = (", ".join(str(i) for i in range(len(matrix))))
per_size = [str(i) for i in range(len(matrix))]

#while not check_matrix(matrix, switch_x_o) and not stop_game(matrix):  
#так как возможен вариант когда всё поле занято, но есть победная комбинация то будем использовать доп переменную чтобы после не вызывать функции снова и не тратить ресурсы
while not per_check and not stop_game(matrix):
    switch_x_o = 'X' if switch_x_o == 'O' else 'O'
    print_matrix(matrix)
    print(f'Сейчас ходит игрок {switch_x_o}')

    while True:
        
        x = input_data(per_size, per_size_view)
        y = input_data(per_size, per_size_view, 'vertical')

        if matrix[int(y)][int(x)] == '-':
            matrix[int(y)][int(x)] = switch_x_o
            per_check = check_matrix(matrix, switch_x_o)
            break
        else:
            print('Эта позиция уже занята, попробуйте снова')

print_matrix(matrix)

if not per_check:  #из-за этого условия вводилась доп переменная, проверка принична завершения игры
    print('Игра окончена, больше ходов нет')
else:
    print(f'Победил {switch_x_o}')
