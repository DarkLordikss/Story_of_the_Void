# -*- coding: utf8 -*-

from time import sleep
import sys
from random import randint

inp = 0
rand = 0
ok = False
hero = {
    'dark_end_count': 0,
    'destroyer': False,
    'timekeeper': False,
    'corridor': 0,
    'colors': False,
    'reality': 100}

def output_text(lines):         #Печатная машинка
    for line in lines:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.0)
            #sleep(0.02)        #Нормальная скорость
        print('')

def repl(need_ans, text, ans=None):                                                                                             #Реплика
    print('__________________________________________________________________________________________')
    output_text(text)
    print('__________________________________________________________________________________________')
    if need_ans:
        ans.append('\nДля выхода введите "Exit"')
        output_text(ans)
        print('__________________________________________________________________________________________')


def error():
        output_text(['Кажется, вы ошиблись^-^\n'])

#Выбор пути
def enity_choose_path():
    ok = False
    while not ok:
        repl(True, ['Вокруг тьма…',
                    'Лишь абсолютная непроглядная тьма, что заполняет все пространство вокруг.',
                    'Ты не чувствуешь абсолютно ничего, даже своего тела.',
                    'Даже время потеряло здесь свой ход… Пред Тобой являются два символа: Меч и Часы.',
                    'Вокруг по-прежнему ничего нет, но теперь ты можешь хотя бы ощущать свое тело.'],
                    ['\n|1| Выбрать Меч', '\n|2| Выбрать Часы'])
        inp = str(input())

        if inp == '1':
            repl(False, ['\nТы коснулся символа Меча и он тут же пропал.'])
            ok = True
            hero['destroyer'] = True
            return 'destroyer'
        elif inp == '2':
            repl(False, ['\nТы коснулся символа Часов и он тут же пропал. Твои глаза озарила яркая вспышка...'])
            ok = True
            hero['timekeeper'] = True
            return 'timekeeper'
        elif inp == 'Exit':
            sys.exit()
        else:
            error()

#Руны для разрушителя
def destroyer_and_runes():
    ok = False
    while not ok:
        repl(True ,['Твои глаза озарила яркая вспышка, и пред тобой предстало белое пространство,',
                    'похожее на комнату, а время вернуло свой ход. Не понимая, ни что ты за',
                    'существо, ни что находится вокруг Тебя, у Тебя есть лишь разум твой и воля твоя.',
                    'Ты решаешь, что нужно предпринять что-то.',
                    'За Тобой оказалось что-то напоминающее руны. Подойдя к рунам, ты разглядываешь их.'],
                    ['\n|1| Изучить руны внимательнее', '\n|2| Разбить руны'])
        inp = str(input())
        rand = randint(0, 12)

        if inp == '1' and rand != 4:
            repl(False, ['Ты собрал всю мощь Твоего сознания и стал внимательно вчитываться в руны,',
                        'но этого оказалось недостаточно и ничего не произошло.'])

        elif inp == '1' and rand == 4:
            repl(False, ['Ты собрал всю мощь Твоего сознания и стал внимательно вчитываться в руны.',
                        'Голос из глубин Твоего сознания советует тебе обвести их. Мысленно обведя руны,',
                        'Ты создал проход, ведущий к проходу с развилкой.'])
            hero['dark_end_count'] += 1
            ok = True

        elif inp == '2':
            repl(False, ['Ты собрал всю мощь Твоей воли и одним ударом разбил руны на призматические осколки бытия.',
                        'За преградой оказался проход, ведущий к развилке'])
            ok = True

        elif inp == 'Exit':
            sys.exit()

        else:
            error()
#Руны для хранителя
def timekeeper_and_runes():
        ok = False
        while not ok:
            repl(True ,['Твои глаза озарила яркая вспышка, и пред тобой предстало белое пространство,',
                        'похожее на комнату, а время вернуло свой ход. Не понимая, ни что ты за',
                        'существо, ни что находится вокруг Тебя, у Тебя есть лишь разум твой и воля твоя.',
                        'Ты решаешь, что нужно предпринять что-то.',
                        'За Тобой оказалось что-то напоминающее руны. Подойдя к рунам, ты разглядываешь их.'],
                        ['\n|1| Изучить руны внимательнее', '\n|2| Разбить руны'])
            inp = str(input())
            rand = randint(0, 12)

            if inp == '1':
                repl(False, ['Ты собрал всю мощь Твоего сознания и взлянул на руны через призматический осколок бытия, ',
                            'изучая каждую деталь их сущности. Под настиском потока разума руническая',
                            'защита пала и открылся путь с разилкой.'])
                ok = True

            elif inp == '2' and rand == 4:
                repl(False, ['Ты собрал всю мощь Твоей воли и направил ее на руны.',
                            'Ты почувствовал как что-то на грани Твоего сознания многократно усилилило',
                            'Твою атаку. Руны не выдуржали такого и разлетелись на сотни призматических осколков бытия',
                            'Впереди Тебя ждет развилка.'])
                hero['dark_end_count'] += 1
                ok = True

            elif inp == '2' and rand != 4:
                repl(False, ['Ты собрал всю мощь Твоей воли, но этого оказалось недостаточно.',
                            'Руны даже не откликнулись на попытку атаковать их.'])

            elif inp == 'Exit':
                sys.exit()

            else:
                error()
#Коридоры
def corridors():
    ok = False
    while not ok:
        repl(True, ['Пред Тобой предстали 3 коридора, покрытые легкой белой пеленой.',
                    'Наблюдая за каждым из них Ты замечаешь, что в первом коридоре слышен приглушенный',
                    'металлический скрежет, во втором царит абсолютная тишина, и оттуда веет прохладой,',
                    'а из третьего слышится тихое щелканье и стук.'],
                    ['\n|1| Выбрать первый коридор, \n|2| Выбрать второй коридор, \n|3| Выбрать третий коридор,'])
        inp = str(input())

        if inp == '1':
            repl(False, ['Вы вошли в первый коридор.'])
            hero['corridor'] = 1
            ok = True
        elif inp == '2':
            repl(False, ['Вы вошли во второй коридор.'])
            hero['corridor'] = 2
            ok = True
        elif inp == '3':
            repl(False, ['Вы вошли в третий коридор.'])
            hero['corridor'] = 3
            ok = True
        elif inp == 'Exit':
            sys.exit()

        else:
            error()
def death():
    repl(False, ['Ты почувствал как из тебя вырывают разум,',
                'а Ты распадаешься на осколки. Но это лишь начало Конца.'])
    output_text(['Нажмите Enter для выхода'])
    inp = input()
    sys.exit()
#Смерть во 2 коридоре
def corridor_2_death():
    if hero['dark_end_count'] > 0:
        repl(False, ['Зайдя во второй коридор, Ты потерял возможность контролировать себя.',
                    '"Наконец-то ты пришел..." - прозвучало это в Твоей голове.',
                    'Тебя окутал холод и, разум оставил Тебя.'])
        output_text(['Нажмите Enter для выхода'])
        inp = input()
        sys.exit()
    else:
        death()
#Загадка первого коридора
def corridor_1_colors():
    ok = False
    while not ok:
        repl(True ,['За пеленой первого коридора тебя ожидал странный механизм, который',
                    'который находился среди наполненного Хаоса этого места. С одной',
                    'стороны его находились шесть квадратов: красный, желтый и зеленый, а',
                    'под ними в квадратах соответсвенно символы GBR. С другой же стороны',
                    'Находились черный, желтый и зеленый квадраты соответсвенно. Под ними',
                    'есть 3 пустых квадрата. Напрямую в разум Твой машина передала сообщение:',
                    '"Не забывай что Тьма - это Свет. Все подвержено инверсии". Ты решаешь',
                    'начертить символы в пустых квадратах.'], ['Введи последовательность'])
        inp = str(input())

        if inp == 'WBR':
            repl(False, ['Символы пред тобой вспыхнули и исчезли. Призматические стены впереди',
                        'открыли тебе путь вперед. Ты идешь все дальше и дальше в Бездну Сознания...'])
            ok = True
            hero['colors'] = True

        elif inp == 'Exit':
            sys.exit()

        else:
            repl(False, ['Комбинация оказалась неверной, и то, что ты вычертил пропало, но Воля Твоя',
                        'не дает Тебе сдаться, и ты пробуешь вновь. Твоя Реальность пострадала.'])
            hero['reality'] -= 20
            if hero['reality'] <= 0:
                death()
#Битва в 3 коридоре
def corridor_3_fight():
    ok = False
    win = False
    enemy_reality = 100
    while not ok:
        repl(False, ['Ты зашел за пелену третьего коридора и увидел пред собой астральную сущность,',
                    'которая, только завидев тебя сразу бросилась в атаку. Своим Разумом и Волей ты',
                    'вступаешь в бой'])
        while not win:
            if hero['reality'] > 0 and enemy_reality > 0:
                repl(True, ['Реальность Часового - ', str(enemy_reality),'Реальность Сущности - ', str(hero['reality']),
                            '\nТы стоишь напротив Часового, готовясь его атаковать.'],
                           ['\n|1| Атаковать в лоб',
                            '\n|2| Отвлечь и атаковать',
                            '\n|2| Попытаться отразить атаку врага'])
                inp = str(input())

                if inp == '1':
                    repl(False, ['Ты обменялся атаками с Часовым.'])
                    hero['reality'] -= 20
                    enemy_reality -= 15
                elif inp == '2':
                    rand = randint(0, 10)
                    if rand > 3:
                        repl(False, ['Ты успешно атаковал врага своей Волей.'])
                        enemy_reality -= 10
                    else:
                        repl(False, ['Атака прошла неудачно и Ты повредил свой Разум'])
                        hero['reality'] -= 10
                elif inp == '3':
                    rand = randint(0, 10)
                    if rand > 7:
                        repl(False, ['Ты успешно отразил врага своим Разумом.'])
                        enemy_reality -= 25
                    else:
                            repl(False, ['Тебе не удалось отразить атаку, и Ты повредил свой разум'])
                            hero['reality'] -= 40
                elif inp == 'Exit':
                    sys.exit()
                else:
                    error()
            elif hero['reality'] > 0 and enemy_reality <= 0:
                repl(False, ['Ты успешно победил Часового и, теперь ты можешь продлжить'],
                            ['свой путь в Бездну Сознания...'])
                win = True
                ok = True
            else:
                death()
#Концовка уничтожителя
def destroy():
    repl(False, ['Одним небольшим усилием Воли Ты разрушил то, что создало и',
                 'поддерживало этото мир. И вся вина за это лишь на тебе, Сущность.',
                 'Надеюсь, ты готов к последствиям своих действий...'])
    output_text(['Нажмите Enter для выхода'])
    inp = input()
    sys.exit()
#Неудачная концовка разрушителя
def destroy_fault():
    repl(False, ['Твоей Воли недостаточно чтобы разрушить столь могущественный',
                 'артефакт. В ответ на Твою агрессию он низверг Тебя из этого мира.',
                 'Знай же цену своих действий.'])
    output_text(['Нажмите Enter для выхода'])
    inp = input()
    sys.exit()
#Концовка улучшения
def upgrade():
    repl(False, ['Силой своего Разума ты запустил механизм, и он начал менять реальность',
                 'вокруг. Мир стал приобретать большую материальность и реальность.',
                 'Я благодарен Тебе, Хранитель.'])
    output_text(['Нажмите Enter для выхода'])
    inp = input()
    sys.exit()
#Неудачная концовка улучшения
def upgrade_fault():
    repl(False, ['Ты попытался запустить древний механизм, но силы Твоего разума недостаточно',
                 'для этого. Потеряв свои последние силы и Реальность, ты пал ниц и слился м пустотой...',
                 'Я сожалею о твоей участи, Разрушитель.'])
    output_text(['Нажмите Enter для выхода'])
    inp = input()
    sys.exit()
#Ядро
def core():
    ok = False
    while not ok:
        repl(True, ['Ты идешь по бесконечно длинному ослепляюще-белому пути. Ты чувствуешь',
                    'близость Безны. Спустя определенное количество циклов, Ты дошел до',
                    'небольшого ромбического устройства. Deus machina. Устройство для',
                    'создания и уничтожения Бытия прямо пред Тобой. Сделай свой выбор.'],
                    ['\n|1| Уничтожить Deus machina', '\n|2| Активировать Deus Machina'])
        inp = str(input())
        if inp == '1' and hero['destroyer'] == True:
            destroy()
            ok = True
        if inp == '1' and hero['destroyer'] != True:
            destroy_fault()
            ok = True
        if inp == '2' and hero['timekeeper'] == True:
            upgrade()
            ok = True
        if inp == '2' and hero['timekeeper'] != True:
            upgrade_fault()
            ok = True
        elif inp == 'Exit':
            sys.exit()
        else:
            error()

#Ход сюжета
if __name__ == "__main__":
    if enity_choose_path() == 'destroyer':
        destroyer_and_runes()
    else:
        timekeeper_and_runes()
    corridors()
    if hero['corridor'] == 1:
        corridor_1_colors()
        core()
    elif hero['corridor'] == 2:
        corridor_2_death()
    elif hero['corridor'] == 3:
        corridor_3_fight()
