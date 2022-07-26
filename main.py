def draw_new(field):
    for i in range(9):
        field.append('-')
    draw(field)

def draw(field):
    print(' ', '1', '2', '3')
    print('1', field[0], field[1], field[2])
    print('2', field[3], field[4], field[5])
    print('3', field[6], field[7], field[8])

def choice(player, field):
    choice_test = False
    print('Ход игрока ', player)
    while not choice_test:
        s = input('Введите координаты ячейки: ',).replace(' ', '')
        if s.isnumeric():
            s = list(map(int, s))
            coord = (s[0] - 1) + (s[0] - 1) * 2 + (s[1]-1)
            if (len(s) != 2) or (not int(s[0]) in range(1,4)) or (not int(s[1]) in range(1,4)):
                print('Введены неверные координаты')
            elif field[coord] != '-':
                print('Данные координаты заняты')
            else:
                choice_test = True
                return coord
        else:
            print('При вводе координат вы должны использовать только цифры')

def filling(player, field, coord):
    if player == 1:
        field[coord] = 'x'
    else:
        field[coord] = 'o'
    print()
    draw(field)

def win_detector(field):
    win_combinations = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_combinations:
        if (field[i[0]] == field[i[1]] == field[i[2]] == 'x') or (field[i[0]] == field[i[1]] == field[i[2]] == 'o'):
            return True
    return False

def play():
    count = 0
    field = []
    player = 1
    win = False
    draw_new(field)
    while not win:
        filling(player, field, choice(player, field))
        win = win_detector(field)
        count += 1
        if win:
            print(f'Игрок {player} выиграл!!!!')
        elif count == 9:
            print('Ничья!')
            win = True
        else:
            if player == 1:
                player = 2
            else:
                player = 1

repit = 'y'
while repit == 'y':
    play()
    repit = input('Начать новую игру? (y/n) ', )