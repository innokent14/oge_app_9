import random


def ex_10():
    test_list = {
        'data': [],
        'answer': []
    }

    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)

    max_num = max(a, b, c)

    ba_2 = bin(a)[2:]
    ob_8 = oct(b)[2:]
    hc_16 = hex(c)[2:]

    test_list['data'] = ['Среди приведенных ниже трех чисел, записанных в различных системах счисления, найдите '
                         'максимальное и запишите его в ответе в десятичной системе счисления. В ответе запишите '
                         'только число, основание системы счисления указывать не нужно.', ba_2, ob_8, hc_16]
    test_list['answer'] = [max_num]

    return test_list


print(ex_10())
