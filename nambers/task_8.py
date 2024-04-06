import random


def ex_8():
    test_list = {
        'data': [],
        'answer': []
    }

    fp = {
        "A | B": None,
        "A": 2500,
        "B": 2000,
        "A & B": 500
    }

    unknow = random.choice(list(fp))

    fp['A'] = random.randint(10, 30) * 100
    fp['B'] = random.randint(10, 30) * 100
    fp['A & B'] = random.randint(500, (min(fp['A'], fp['B'])) / 2)
    fp['A | B'] = fp['A'] + fp['B'] - fp['A & B']

    answer = fp[unknow]
    fp[unknow] = None

    test_list['data'] = [
        'В языке запросов поискового сервера для обозначения логической операции «ИЛИ» используется символ «|», '
        'а для логической операции «И» – символ «&».\n'
        'В таблице приведены запросы и количество найденных по ним страниц некоторого сегмента сети Интернет.', fp,
        f'Какое количество страниц (в тысячах) будет найдено по запросу {unknow}',
        'Считается, что все запросы выполнялись практически одновременно, так что набор страниц, содержащих все искомые'
        'слова, не изменялся за время выполнения запросов.']
    test_list['answer'] = [answer]

    return test_list


print(ex_8())
