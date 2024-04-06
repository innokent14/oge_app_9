import random


def ex_5():
    test_list = {
        'data': [],
        'answer': []
    }

    prog = ""
    for i in range(5):
        prog += f'{random.randint(1, 2)}'

    start_int = random.randint(1, 10)

    num = {
        '1': random.randint(2, 10),
        '2': random.randint(2, 10)
    }

    answer = start_int
    for i in prog:
        if i == '1':
            answer += num['1']
        else:
            answer *= num['2']

    test_list['data'] = ['У исполнителя Омега две команды, которым присвоены номера:', f'1. прибавь {num["1"]};',  f'1.умножь на b;', f'Выполняя первую из них, Омега увеличивает число на экране на {num["1"]}, а выполняя вторую, делит это число на b.\n Программа для исполнителя Омега— это последовательность номеров команд. Известно, что программа {prog} переводит число {start_int} в число {answer}. Определите значение b.']
    test_list['answer'] = [num['2']]

    return test_list


print(ex_5())
