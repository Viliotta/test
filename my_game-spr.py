import random

comp_score=0
player_score=0
print('Камень давит ножницы, ножницы режут бумагу, бумага накрывает камень.')
comp_attack=['камень','ножницы','бумага']



while True:
    print('У вас:', player_score,'\nУ компьютера:', comp_score)
    player=input('Выберите: камень, ножницы или бумага (выйти)?').lower()
    comp=random.choice(comp_attack)
    print('Твой выбор:', player, '\nВыбор компьютера:', comp)
    if player == comp:
        print('Ничья!')
    elif player=='бумага':
        if comp=='камень':
            print('Ты победил!')
            player_score+=1
        else:
            print('Победил компьютер!')
            comp_score+=1
    elif player=='камень':
        if comp=='ножницы':
            print('Ты победил!')
            player_score+=1
        else:
            print('Победил компьютер!')
            comp_score+=1
    elif player=='ножницы':
        if comp=='бумага':
            print('Ты победил!')
            player_score+=1
        else:
            print('Победил компьютер!')
            comp_score+=1
    elif player=='выйти':
        print('Вы вышли из игры')
        break
    else:
        print('Произошла ошибка..')
    if (player_score==10):
        print('\t\t\tТЫ ВЫЙГРАЛ, ПОЗДРАВЛЯЮ!')
    elif (comp_score==10):
        print('\t\t\tТЫ ПРОИГРАЛ, ПОПРОБУЙ СНОВА!')
        
