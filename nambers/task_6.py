import random


def ex_6():
    test_list = {
        'data': ['/'],
        'answer': ['/']
    }

    operator_1 = random.choice(['>', '<'])
    operator_2 = random.choice(['and', 'or'])
    integer = random.randint(-10, 15)

    list_count = [(random.randint(1, 20), random.randint(1, 20)) for i in range(9)]

    cmd_python = (f's = int(input())\nt = int(input())\nif s '
                  f'{operator_1} {integer} {operator_2} t {operator_1} {integer}:\nprint("YES")\nelse:\nprint("NO")')

    cmd_basic = (f'DIM s, t AS INTEGER\nINPUT s\nINPUT t\nIF s {operator_1} {integer}'
                 f' {operator_2.upper()} t {operator_1} {integer} THEN\nPRINT ‘YES’\nELSE\nPRINT ‘NO’\nENDIF')

    cmd_pascal = (f'var s, t: integer;\nbegin\nreadln(s);\nreadln(t);\nif (s {operator_1} {integer}) {operator_2} (t '
                  f'{operator_1} {integer})\nthen writeln("YES")\nelse writeln("NO")\nend.')

    cmd_c = ('#include <iostream>\nusing namespace std;\nint main() {\nint s, t;\nint s, t;\ncin >> t;'
             f'\nif (s {operator_1} {integer} {"&&" if operator_2 == "and" else "||"} t {operator_1} {integer})'
             '\ncout << "YES";\nelse\ncout << "NO";\nreturn 0;\n}')

    cmd_algorithmic = (f'алг\nнач\nцел s, t\nввод s\nввод t\nесли s {operator_1} {integer}'
                       f' {"и" if operator_2 == "and" else "или"} t {operator_1} {integer}'
                       f'\n то вывод "YES"\nиначе вывод "NO"\nвсе\nкон')

    # print(cmd_algorithmic)
    # print(cmd_c)
    # print(cmd_pascal)
    # print(cmd_python)
    # print(cmd_basic)

    count = 0
    for s, t in list_count:
        cmd = f'count + 1 if {s} {operator_1} {integer} {operator_2} {t} {operator_1} {integer} else count'
        count = eval(cmd)

    test_list['data'] = ['Ниже приведена программа, записанная на пяти языках программирования',
                         {'Aлгоритмический язык': cmd_algorithmic, 'c++': cmd_c, 'Паскаль': cmd_pascal,
                          'Python': cmd_python, 'Бэйсик': cmd_basic},
                         'Было проведено 9 запусков программы, при которых в качестве значений переменных s и t '
                         'вводились следующие пары чисел:', list_count]
    test_list['answer'] = [count]

    return test_list


ex_6()

