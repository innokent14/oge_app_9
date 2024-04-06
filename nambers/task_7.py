import random

urls = ['http://unicornpark.com/magical.doc', 'http://fairyland.org/enchanted.doc',
        'http://wizardrealm.net/spell.doc', 'http://mythicalcreatures.com/dragon.doc',
        'http://enchantedforest.org/mystical.doc', 'http://fantasyisland.net/magic.doc',
        'http://magicworld.org/spellbound.doc', 'http://mythicalbeasts.com/phoenix.doc',
        'http://fabledland.net/legendary.doc', 'http://mysticalrealm.org/witchcraft.doc',
        'http://wonderland.com/fantastical.txt', 'http://enchantedgarden.org/enchanted.doc',
        'http://dragonisle.net/mystical.doc', 'http://fairytaleland.com/fable.doc',
        'http://witchinghour.org/spell.doc', 'http://mythicbeasts.net/phoenix.doc',
        'http://magicalforest.com/magical.doc', 'http://fantasyworld.org/magic.doc',
        'http://enchantedkingdom.net/enchanted.doc', 'http://mysticalcreatures.com/mystical.doc',
        'http://fabledrealm.org/fable.doc', 'http://wonderlandisland.net/fantastical.doc',
        'http://mythicalworld.org/dragon.doc', 'http://fairylandpark.com/fairy.doc',
        'http://wizardingrealm.net/spell.doc', 'http://mythicalgarden.com/phoenix.doc',
        'http://enchantedisland.org/magic.doc', 'http://fantasyforest.net/fantasy.doc',
        'http://magicalisland.com/magical.doc', 'http://fabledgarden.org/fable.doc',
        'http://wonderlandworld.net/fantastical.doc', 'http://mythicalpark.com/dragon.doc',
        'http://fairylandrealm.org/fairy.doc', 'http://wizardinggarden.net/spell.doc',
        'http://mythicalisland.org/phoenix.doc', 'http://enchantedforestpark.com/magic.doc',
        'http://fantasyisland.org/fantasy.doc', 'http://magicalworld.net/magical.doc',
        'http://fabledrealm.com/fable.doc', 'http://wonderlandgarden.org/fantastical.doc',
        'http://mythicalkingdom.net/dragon.doc', 'http://fairylandforest.com/fairy.doc',
        'http://wizardingisland.org/spell.doc', 'http://mythicalgarden.net/phoenix.doc',
        'http://enchantedpark.org/magic.doc', 'http://fantasyrealm.net/fantasy.doc',
        'http://magicalisland.com/magical.doc', 'http://fabledforest.org/fable.doc',
        'http://wonderlandworld.net/fantastical.doc', 'http://mythicalpark.com/dragon.doc']


def ex_7():
    text_list = {
        'data': [],
        'answer': []
    }

    url = random.choice(urls)

    point_1 = url.find('.')
    point_2 = url.rfind('.')

    file_name = url[point_1 + 5:point_2:]
    double_slash = url[4:7:]
    point_text = url[point_2::]
    http = url[0:4:]
    point_site = url[point_1:point_1 + 4:]
    slash = url[point_1 + 4:point_1 + 5:]
    site_name = url[7:point_1:]

    text_list['data'] = [f'Доступ к файлу {file_name}, находящемуся на сервере {site_name}, осуществляется по протоколу http. Фрагменты адреса файла закодированы буквами от А до Ж. Запишите последовательность этих букв, кодирующую адрес указанного файла в сети Интернет.', f'A) {file_name}', f'Б) {double_slash}',
                         f'B) {point_text}', f'Г) {http}', f'Д) {point_site}', f'Е) {slash}', f'Ж) {site_name}']
    text_list['answer'] = [url]

    return text_list


print(ex_7())
